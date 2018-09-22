(function(){var g,k=this;function l(a){return"string"==typeof a}
function m(a){a=a.split(".");for(var b=k,c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function aa(){}
function n(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function p(a){var b=n(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function q(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
var r="closure_uid_"+(1E9*Math.random()>>>0),t=0;function ba(a,b,c){return a.call.apply(a.bind,arguments)}
function ca(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function u(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?u=ba:u=ca;return u.apply(null,arguments)}
function da(a,b){for(var c in b)a[c]=b[c]}
var ea=Date.now||function(){return+new Date};
function w(a,b){var c=a.split("."),d=k;c[0]in d||!d.execScript||d.execScript("var "+c[0]);for(var e;c.length&&(e=c.shift());)c.length||void 0===b?d[e]&&d[e]!==Object.prototype[e]?d=d[e]:d=d[e]={}:d[e]=b}
function x(a,b){function c(){}
c.prototype=b.prototype;a.J=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.R=function(a,c,f){for(var e=Array(arguments.length-2),d=2;d<arguments.length;d++)e[d-2]=arguments[d];return b.prototype[c].apply(a,e)}}
;var fa=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(l(a))return l(b)&&1==b.length?a.indexOf(b,0):-1;
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},y=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=l(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)};
function ha(a,b){a:{var c=a.length;for(var d=l(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:l(a)?a.charAt(c):a[c]}
function ia(a){return Array.prototype.concat.apply([],arguments)}
function z(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
;function ja(a,b){this.c=a;this.f=b;this.b=0;this.a=null}
ja.prototype.get=function(){if(0<this.b){this.b--;var a=this.a;this.a=a.next;a.next=null}else a=this.c();return a};var ka=/&/g,la=/</g,ma=/>/g,na=/"/g,oa=/'/g,pa=/\x00/g,qa=/[\x00&<>"']/;var A;a:{var ra=k.navigator;if(ra){var sa=ra.userAgent;if(sa){A=sa;break a}}A=""};function ta(a){var b=B,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
;function ua(a){k.setTimeout(function(){throw a;},0)}
var C;
function va(){var a=k.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&-1==A.indexOf("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow;a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host;a=u(function(a){if(("*"==d||a.origin==d)&&
a.data==c)this.port1.onmessage()},this);
b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});
if("undefined"!==typeof a&&-1==A.indexOf("Trident")&&-1==A.indexOf("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var a=c.F;c.F=null;a()}};
return function(a){d.next={F:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");
b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};
document.documentElement.appendChild(b)}:function(a){k.setTimeout(a,0)}}
;function D(){this.b=this.a=null}
var wa=new ja(function(){return new E},function(a){a.reset()});
D.prototype.add=function(a,b){var c=wa.get();c.set(a,b);this.b?this.b.next=c:this.a=c;this.b=c};
D.prototype.remove=function(){var a=null;this.a&&(a=this.a,this.a=this.a.next,this.a||(this.b=null),a.next=null);return a};
function E(){this.next=this.b=this.a=null}
E.prototype.set=function(a,b){this.a=a;this.b=b;this.next=null};
E.prototype.reset=function(){this.next=this.b=this.a=null};function xa(a){F||ya();G||(F(),G=!0);za.add(a,void 0)}
var F;function ya(){if(-1!=String(k.Promise).indexOf("[native code]")){var a=k.Promise.resolve(void 0);F=function(){a.then(Aa)}}else F=function(){var a=Aa;
"function"!=n(k.setImmediate)||k.Window&&k.Window.prototype&&-1==A.indexOf("Edge")&&k.Window.prototype.setImmediate==k.setImmediate?(C||(C=va()),C(a)):k.setImmediate(a)}}
var G=!1,za=new D;function Aa(){for(var a;a=za.remove();){try{a.a.call(a.b)}catch(c){ua(c)}var b=wa;b.f(a);100>b.b&&(b.b++,a.next=b.a,b.a=a)}G=!1}
;function H(){this.c=this.c;this.f=this.f}
H.prototype.c=!1;H.prototype.dispose=function(){this.c||(this.c=!0,this.A())};
H.prototype.A=function(){if(this.f)for(;this.f.length;)this.f.shift()()};function Ba(a,b){var c,d;var e=document;e=b||e;if(e.querySelectorAll&&e.querySelector&&a)return e.querySelectorAll(""+(a?"."+a:""));if(a&&e.getElementsByClassName){var f=e.getElementsByClassName(a);return f}f=e.getElementsByTagName("*");if(a){var h={};for(c=d=0;e=f[c];c++){var v=e.className,R;if(R="function"==typeof v.split)R=0<=fa(v.split(/\s+/),a);R&&(h[d++]=e)}h.length=d;return h}return f}
function Ca(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;var I="StopIteration"in k?k.StopIteration:{message:"StopIteration",stack:""};function J(){}
J.prototype.next=function(){throw I;};
J.prototype.m=function(){return this};
function Da(a){if(a instanceof J)return a;if("function"==typeof a.m)return a.m(!1);if(p(a)){var b=0,c=new J;c.next=function(){for(;;){if(b>=a.length)throw I;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function Ea(a,b){if(p(a))try{y(a,b,void 0)}catch(c){if(c!==I)throw c;}else{a=Da(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==I)throw c;}}}
function Fa(a){if(p(a))return z(a);a=Da(a);var b=[];Ea(a,function(a){b.push(a)});
return b}
;var Ga=k.JSON.stringify;function K(a){H.call(this);this.l=1;this.g=[];this.h=0;this.a=[];this.b={};this.o=!!a}
x(K,H);g=K.prototype;g.subscribe=function(a,b,c){var d=this.b[a];d||(d=this.b[a]=[]);var e=this.l;this.a[e]=a;this.a[e+1]=b;this.a[e+2]=c;this.l=e+3;d.push(e);return e};
function Ha(a,b,c){var d=L;if(a=d.b[a]){var e=d.a;(a=ha(a,function(a){return e[a+1]==b&&e[a+2]==c}))&&d.D(a)}}
g.D=function(a){var b=this.a[a];if(b){var c=this.b[b];if(0!=this.h)this.g.push(a),this.a[a+1]=aa;else{if(c){var d=fa(c,a);0<=d&&Array.prototype.splice.call(c,d,1)}delete this.a[a];delete this.a[a+1];delete this.a[a+2]}}return!!b};
g.H=function(a,b){var c=this.b[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.o)for(e=0;e<c.length;e++){var h=c[e];Ia(this.a[h+1],this.a[h+2],d)}else{this.h++;try{for(e=0,f=c.length;e<f;e++)h=c[e],this.a[h+1].apply(this.a[h+2],d)}finally{if(this.h--,0<this.g.length&&0==this.h)for(;c=this.g.pop();)this.D(c)}}return 0!=e}return!1};
function Ia(a,b,c){xa(function(){a.apply(b,c)})}
g.clear=function(a){if(a){var b=this.b[a];b&&(y(b,this.D,this),delete this.b[a])}else this.a.length=0,this.b={}};
g.A=function(){K.J.A.call(this);this.clear();this.g.length=0};function Ja(){}
;function M(){}
x(M,Ja);M.prototype.clear=function(){var a=Fa(this.m(!0)),b=this;y(a,function(a){b.remove(a)})};function N(a){this.a=a}
x(N,M);function Ka(a){if(a.a)try{a.a.setItem("__sak","1"),a.a.removeItem("__sak")}catch(b){}}
g=N.prototype;g.set=function(a,b){try{this.a.setItem(a,b)}catch(c){if(0==this.a.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
g.get=function(a){a=this.a.getItem(a);if(!l(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
g.remove=function(a){this.a.removeItem(a)};
g.m=function(a){var b=0,c=this.a,d=new J;d.next=function(){if(b>=c.length)throw I;var d=c.key(b++);if(a)return d;d=c.getItem(d);if(!l(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
g.clear=function(){this.a.clear()};
g.key=function(a){return this.a.key(a)};function La(){var a=null;try{a=window.localStorage||null}catch(b){}this.a=a}
x(La,N);function Ma(){var a=null;try{a=window.sessionStorage||null}catch(b){}this.a=a}
x(Ma,N);var Na=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function Oa(a){var b=a.match(Na);a=b[1];var c=b[2],d=b[3];b=b[4];var e="";a&&(e+=a+":");d&&(e+="//",c&&(e+=c+"@"),e+=d,b&&(e+=":"+b));return e}
function Pa(a,b,c){if("array"==n(b))for(var d=0;d<b.length;d++)Pa(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function Qa(a){var b=[],c;for(c in a)Pa(c,a[c],b);return b.join("&")}
var Ra=/#|$/;var O=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};w("yt.config_",O);function Sa(a){var b=arguments;if(1<b.length)O[b[0]]=b[1];else{b=b[0];for(var c in b)O[c]=b[c]}}
;function Ta(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Ua(b)}}:a}
function Ua(a,b){var c=m("yt.logging.errors.log");c?c(a,b,void 0,void 0,void 0):(c=[],c="ERRORS"in O?O.ERRORS:c,c.push([a,b,void 0,void 0,void 0]),Sa("ERRORS",c))}
;var Va=0;w("ytDomDomGetNextId",m("ytDomDomGetNextId")||function(){return++Va});var Wa={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function P(a){this.type="";this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;if(a=a||window.event){this.a=a;for(var b in a)b in Wa||(this[b]=a[b]);(b=a.target||a.srcElement)&&3==b.nodeType&&(b=b.parentNode);this.target=b;if(b=a.relatedTarget)try{b=b.nodeName?b:null}catch(c){b=null}else"mouseover"==this.type?b=a.fromElement:"mouseout"==
this.type&&(b=a.toElement);this.relatedTarget=b;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey}}
P.prototype.preventDefault=function(){this.a&&(this.a.returnValue=!1,this.a.preventDefault&&this.a.preventDefault())};
P.prototype.stopPropagation=function(){this.a&&(this.a.cancelBubble=!0,this.a.stopPropagation&&this.a.stopPropagation())};
P.prototype.stopImmediatePropagation=function(){this.a&&(this.a.cancelBubble=!0,this.a.stopImmediatePropagation&&this.a.stopImmediatePropagation())};var B=m("ytEventsEventsListeners")||{};w("ytEventsEventsListeners",B);var Xa=m("ytEventsEventsCounter")||{count:0};w("ytEventsEventsCounter",Xa);function Ya(a,b,c,d){d=void 0===d?!1:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return ta(function(e){return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&e[4]==!!d})}
function Za(a){a&&("string"==typeof a&&(a=[a]),y(a,function(a){if(a in B){var b=B[a],d=b[0],e=b[1],f=b[3];b=b[4];d.removeEventListener?d.removeEventListener(e,f,b):d.detachEvent&&d.detachEvent("on"+e,f);delete B[a]}}))}
function $a(a,b,c){var d=void 0===d?!1:d;if(a&&(a.addEventListener||a.attachEvent)){var e=Ya(a,b,c,d);if(!e){e=++Xa.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var h=f?function(d){d=new P(d);if(!Ca(d.relatedTarget,function(b){return b==a}))return d.currentTarget=a,d.type=b,c.call(a,d)}:function(b){b=new P(b);
b.currentTarget=a;return c.call(a,b)};
h=Ta(h);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),a.addEventListener(b,h,d)):a.attachEvent("on"+b,h);B[e]=[a,b,c,h,d]}}}
;function ab(a){"function"==n(a)&&(a=Ta(a));return window.setInterval(a,250)}
;var bb={};function cb(a){return bb[a]||(bb[a]=String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()}))}
;var Q={},S=[],L=new K,db={};function eb(){y(S,function(a){a()})}
function fb(a,b){b||(b=document);var c=z(b.getElementsByTagName("yt:"+a)),d="yt-"+a,e=b||document;d=z(e.querySelectorAll&&e.querySelector?e.querySelectorAll("."+d):Ba(d,b));return ia(c,d)}
function T(a,b){return"yt:"==a.tagName.toLowerCase().substr(0,3)?a.getAttribute(b):a?a.dataset?a.dataset[cb(b)]:a.getAttribute("data-"+b):null}
function gb(a,b){L.H.apply(L,arguments)}
;function hb(a){this.b=a||{};this.f={};this.c=this.a=!1;a=document.getElementById("www-widgetapi-script");if(this.a=!!("https:"==document.location.protocol||a&&0==a.src.indexOf("https:"))){a=[this.b,window.YTConfig||{},this.f];for(var b=0;b<a.length;b++)a[b].host&&(a[b].host=a[b].host.replace("http://","https://"))}}
var U=null;function V(a,b){for(var c=[a.b,window.YTConfig||{},a.f],d=0;d<c.length;d++){var e=c[d][b];if(void 0!=e)return e}return null}
function ib(a,b,c){U||(U={},$a(window,"message",u(a.g,a)));U[c]=b}
hb.prototype.g=function(a){if(a.origin==V(this,"host")||a.origin==V(this,"host").replace(/^http:/,"https:")){try{var b=JSON.parse(a.data)}catch(c){return}this.c=!0;this.a||0!=a.origin.indexOf("https:")||(this.a=!0);if(a=U[b.id])a.B=!0,a.B&&(y(a.u,a.C,a),a.u.length=0),a.I(b)}};function W(a,b,c){this.h=this.a=this.b=null;this.g=this[r]||(this[r]=++t);this.c=0;this.B=!1;this.u=[];this.f=null;this.l=c;this.o={};c=document;if(a=l(a)?c.getElementById(a):a)if(c="iframe"==a.tagName.toLowerCase(),b.host||(b.host=c?Oa(a.src):"https://www.youtube.com"),this.b=new hb(b),c||(b=jb(this,a),this.h=a,(c=a.parentNode)&&c.replaceChild(b,a),a=b),this.a=a,this.a.id||(a=b=this.a,a=a[r]||(a[r]=++t),b.id="widget"+a),Q[this.a.id]=this,window.postMessage){this.f=new K;kb(this);b=V(this.b,"events");
for(var d in b)b.hasOwnProperty(d)&&this.addEventListener(d,b[d]);for(var e in db)lb(this,e)}}
g=W.prototype;g.M=function(a,b){this.a.width=a;this.a.height=b;return this};
g.L=function(){return this.a};
g.I=function(a){this.s(a.event,a)};
g.addEventListener=function(a,b){var c=b;"string"==typeof b&&(c=function(){window[b].apply(window,arguments)});
this.f.subscribe(a,c);mb(this,a);return this};
function lb(a,b){var c=b.split(".");if(2==c.length){var d=c[1];a.l==c[0]&&mb(a,d)}}
g.K=function(){this.a.id&&(Q[this.a.id]=null);var a=this.f;a&&"function"==typeof a.dispose&&a.dispose();if(this.h){a=this.a;var b=a.parentNode;b&&b.replaceChild(this.h,a)}else(a=this.a)&&a.parentNode&&a.parentNode.removeChild(a);U&&(U[this.g]=null);this.b=null;a=this.a;for(var c in B)B[c][0]==a&&Za(c);this.h=this.a=null};
g.v=function(){return{}};
function X(a,b,c){c=c||[];c=Array.prototype.slice.call(c);b={event:"command",func:b,args:c};a.B?a.C(b):a.u.push(b)}
g.s=function(a,b){if(!this.f.c){var c={target:this,data:b};this.f.H(a,c);gb(this.l+"."+a,c)}};
function jb(a,b){for(var c=document.createElement("iframe"),d=b.attributes,e=0,f=d.length;e<f;e++){var h=d[e].value;null!=h&&""!=h&&"null"!=h&&c.setAttribute(d[e].name,h)}c.setAttribute("frameBorder",0);c.setAttribute("allowfullscreen",1);c.setAttribute("gesture","media");c.setAttribute("allow","encrypted-media");c.setAttribute("title","YouTube "+V(a.b,"title"));(d=V(a.b,"width"))&&c.setAttribute("width",d);(d=V(a.b,"height"))&&c.setAttribute("height",d);var v=a.v();v.enablejsapi=window.postMessage?
1:0;window.location.host&&(v.origin=window.location.protocol+"//"+window.location.host);v.widgetid=a.g;window.location.href&&y(["debugjs","debugcss"],function(a){var b=window.location.href;var c=b.search(Ra);b:{var d=0;for(var e=a.length;0<=(d=b.indexOf(a,d))&&d<c;){var f=b.charCodeAt(d-1);if(38==f||63==f)if(f=b.charCodeAt(d+e),!f||61==f||38==f||35==f)break b;d+=e+1}d=-1}if(0>d)b=null;else{e=b.indexOf("&",d);if(0>e||e>c)e=c;d+=a.length+1;b=decodeURIComponent(b.substr(d,e-d).replace(/\+/g," "))}null===
b||(v[a]=b)});
c.src=V(a.b,"host")+a.w()+"?"+Qa(v);return c}
g.G=function(){this.a&&this.a.contentWindow?this.C({event:"listening"}):window.clearInterval(this.c)};
function kb(a){ib(a.b,a,a.g);a.c=ab(u(a.G,a));$a(a.a,"load",u(function(){window.clearInterval(this.c);this.c=ab(u(this.G,this))},a))}
function mb(a,b){a.o[b]||(a.o[b]=!0,X(a,"addEventListener",[b]))}
g.C=function(a){a.id=this.g;a.channel="widget";a=Ga(a);var b=this.b;var c=Oa(this.a.src);b=0==c.indexOf("https:")?[c]:b.a?[c.replace("http:","https:")]:b.c?[c]:[c,c.replace("http:","https:")];if(!this.a.contentWindow)throw Error("The YouTube player is not attached to the DOM.");for(c=0;c<b.length;c++)try{this.a.contentWindow.postMessage(a,b[c])}catch(d){if(d.name&&"SyntaxError"==d.name)Ua(d,"WARNING");else throw d;}};Ka(new La);Ka(new Ma);function nb(a){return(0==a.search("cue")||0==a.search("load"))&&"loadModule"!=a}
function ob(a){return 0==a.search("get")||0==a.search("is")}
;function Y(a,b){if(!a)throw Error("YouTube player element ID required.");var c={title:"video player",videoId:"",width:640,height:360};b&&da(c,b);W.call(this,a,c,"player");this.i={};this.j={}}
x(Y,W);function pb(a){if("iframe"!=a.tagName.toLowerCase()){var b=T(a,"videoid");b&&(b={videoId:b,width:T(a,"width"),height:T(a,"height")},new Y(a,b))}}
g=Y.prototype;g.w=function(){return"/embed/"+V(this.b,"videoId")};
g.v=function(){var a=V(this.b,"playerVars");if(a){var b={},c;for(c in a)b[c]=a[c];a=b}else a={};window!=window.top&&document.referrer&&(a.widget_referrer=document.referrer.substring(0,256));return a};
g.I=function(a){var b=a.event;a=a.info;switch(b){case "apiInfoDelivery":if(q(a))for(var c in a)this.i[c]=a[c];break;case "infoDelivery":qb(this,a);break;case "initialDelivery":window.clearInterval(this.c);this.j={};this.i={};rb(this,a.apiInterface);qb(this,a);break;default:this.s(b,a)}};
function qb(a,b){if(q(b))for(var c in b)a.j[c]=b[c]}
function rb(a,b){y(b,function(a){this[a]||("getCurrentTime"==a?this[a]=function(){var a=this.j.currentTime;if(1==this.j.playerState){var b=(ea()/1E3-this.j.currentTimeLastUpdated_)*this.j.playbackRate;0<b&&(a+=Math.min(b,1))}return a}:nb(a)?this[a]=function(){this.j={};
this.i={};X(this,a,arguments);return this}:ob(a)?this[a]=function(){var b=0;
0==a.search("get")?b=3:0==a.search("is")&&(b=2);return this.j[a.charAt(b).toLowerCase()+a.substr(b+1)]}:this[a]=function(){X(this,a,arguments);
return this})},a)}
g.P=function(){var a=parseInt(V(this.b,"width"),10);var b=parseInt(V(this.b,"height"),10);var c=V(this.b,"host")+this.w();qa.test(c)&&(-1!=c.indexOf("&")&&(c=c.replace(ka,"&amp;")),-1!=c.indexOf("<")&&(c=c.replace(la,"&lt;")),-1!=c.indexOf(">")&&(c=c.replace(ma,"&gt;")),-1!=c.indexOf('"')&&(c=c.replace(na,"&quot;")),-1!=c.indexOf("'")&&(c=c.replace(oa,"&#39;")),-1!=c.indexOf("\x00")&&(c=c.replace(pa,"&#0;")));a='<iframe width="'+a+'" height="'+b+'" src="'+c+'" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>';
return a};
g.O=function(a){return this.i.namespaces?a?this.i[a].options||[]:this.i.namespaces||[]:[]};
g.N=function(a,b){if(this.i.namespaces&&a&&b)return this.i[a][b]};function Z(a,b){var c={title:"Thumbnail",videoId:"",width:120,height:68};b&&da(c,b);W.call(this,a,c,"thumbnail")}
x(Z,W);function sb(a){if("iframe"!=a.tagName.toLowerCase()){var b=T(a,"videoid");if(b){b={videoId:b,events:{}};b.width=T(a,"width");b.height=T(a,"height");b.thumbWidth=T(a,"thumb-width");b.thumbHeight=T(a,"thumb-height");b.thumbAlign=T(a,"thumb-align");var c=T(a,"onclick");c&&(b.events.onClick=c);new Z(a,b)}}}
Z.prototype.w=function(){return"/embed/"+V(this.b,"videoId")};
Z.prototype.v=function(){return{player:0,thumb_width:V(this.b,"thumbWidth"),thumb_height:V(this.b,"thumbHeight"),thumb_align:V(this.b,"thumbAlign")}};
Z.prototype.s=function(a,b){Z.J.s.call(this,a,b?b.info:void 0)};w("YT.PlayerState.UNSTARTED",-1);w("YT.PlayerState.ENDED",0);w("YT.PlayerState.PLAYING",1);w("YT.PlayerState.PAUSED",2);w("YT.PlayerState.BUFFERING",3);w("YT.PlayerState.CUED",5);w("YT.get",function(a){return Q[a]});
w("YT.scan",eb);w("YT.subscribe",function(a,b,c){L.subscribe(a,b,c);db[a]=!0;for(var d in Q)lb(Q[d],a)});
w("YT.unsubscribe",function(a,b,c){Ha(a,b,c)});
w("YT.Player",Y);w("YT.Thumbnail",Z);W.prototype.destroy=W.prototype.K;W.prototype.setSize=W.prototype.M;W.prototype.getIframe=W.prototype.L;W.prototype.addEventListener=W.prototype.addEventListener;Y.prototype.getVideoEmbedCode=Y.prototype.P;Y.prototype.getOptions=Y.prototype.O;Y.prototype.getOption=Y.prototype.N;S.push(function(a){a=fb("player",a);y(a,pb)});
S.push(function(){var a=fb("thumbnail");y(a,sb)});
"undefined"!=typeof YTConfig&&YTConfig.parsetags&&"onload"!=YTConfig.parsetags||eb();var tb=m("onYTReady");tb&&tb();var ub=m("onYouTubeIframeAPIReady");ub&&ub();var vb=m("onYouTubePlayerAPIReady");vb&&vb();}).call(this);
