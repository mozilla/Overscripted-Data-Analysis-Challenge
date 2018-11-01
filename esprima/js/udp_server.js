"use strict";
/*
 * Respond to commands over a websocket to relay UDP commands to a local program
 */

var socketio = require('socket.io');
var io;

var dgram = require('dgram');
var fs = require('fs');

exports.listen = function(server) {
        io = socketio.listen(server);
        io.set('log level 1');

        io.sockets.on('connection', function(socket) {
                handleCommand(socket);
        });
};

function handleCommand(socket) {
        // Pased string of comamnd to relay
        socket.on('audio', function(data) {
                console.log('Audio command: ' + data);

                // Info for connecting to the local process via UDP
                var PORT = 8088;
                var HOST = '192.168.7.2';
                var buffer = new Buffer(data);

                var client = dgram.createSocket('udp4');
                client.send(buffer, 0, buffer.length, PORT, HOST, function(err, bytes) {
                        if (err)
                                throw err;
                        console.log('UDP message sent to ' + HOST +':'+ PORT);
                });

                client.on('listening', function () {
                        var address = client.address();
                        console.log('UDP Client: listening on ' + address.address + ":" + address.port);
                });
                // Handle an incoming message over the UDP from the local application.
                client.on('message', function (message, remote) {
                        console.log("UDP Client: message Rx" + remote.address + ':' + remote.port +' - ' + message);

                        var reply = message.toString('utf8');

                        var words = reply.split(' ');
                        var channel = words[0];
                        var value = words[1];

                        socket.emit(channel, value);
                        socket.emit('commandReply', reply);

                        client.close();
                });
                client.on("UDP Client: close", function() {
                        console.log("closed");
                });
                client.on("UDP Client: error", function(err) {
                        console.log("error: ",err);
                });
        });

        // heartbeat
        socket.on('serverStatus', function(data) {

                // ping server
                fs.readFile('/proc/uptime', function(err, fileData) {
                        if (err) {
                                console.log('Error: file not found');
                        } else {
                                var reply = fileData.toString('utf8').split(' ')[0];
                                socket.emit('uptime', reply);
                        }
                })

                // ping program
                // copy paste because I'm lazy (cough 2 days late)
                var PORT = 8088;
                var HOST = '192.168.7.2';
                var buffer = new Buffer(data);

                var client = dgram.createSocket('udp4');
                client.send(buffer, 0, buffer.length, PORT, HOST, function(err, bytes) {
                        if (err)
                                throw err;
                        console.log('Pinging program: ' + HOST +':'+ PORT);
                });

                client.on('listening', function () {
                        var address = client.address();
                        console.log('Listening for ping response: ' + address.address + ":" + address.port);
                });
                // Handle an incoming message over the UDP from the local application.
                client.on('message', function (message, remote) {

                        var reply = message.toString('utf8');
                        var words = reply.split(' ');
                        var channel = words[0];
                        var vals = words[1];

                        socket.emit(channel, vals);
                });
        });
};
