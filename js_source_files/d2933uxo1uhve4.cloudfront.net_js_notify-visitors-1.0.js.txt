var nv = nv || function () {
    (window['nv'].q = window['nv'].q || []).push(arguments)
}; 
nv.l = new Date;
(function () {
    if(window.notify_visitors.auth.bid && window.notify_visitors.auth.bid == 1845 && window.location.host != "indusforex.indusind.com" && window.location.host != "m.indusind.com"){
        return false;
    }
    //check if heatmap js executed then return false
    if (window._nv_hm) {
        return false;
    }

    var nv = nv || function () { (window.nv.q = window.nv.q || []).push(arguments) }; nv.l = new Date; 
    window.notify_visitors = function () { 
        var e = { ab_overlay: !1, auth: 
            { bid_e: window.notify_visitors.auth.bid_e, bid: window.notify_visitors.auth.bid, t: window.notify_visitors.auth.t } 
        }; 
        return e.data = { bid_e: e.auth.bid_e, bid: e.auth.bid, t: e.auth.t, iFrame: window !== window.parent, trafficSource: document.referrer, link_referrer: document.referrer, pageUrl: document.location, path: location.pathname, domain: location.origin, gmOffset: 60 * (new Date).getTimezoneOffset() * -1, screenWidth: screen.width, screenHeight: screen.height, cookieData: document.cookie,tokens:window.notify_visitors.tokens?JSON.stringify(window.notify_visitors.tokens):'',ruleData:window.notify_visitors.ruleData?JSON.stringify(window.notify_visitors.ruleData):'' }, e.options = function (t) { t && "object" == typeof t ? e.ab_overlay = t.ab_overlay : console.log("Not a valid option") }, e.tokens = function (t) { e.data.tokens = t && "object" == typeof t ? JSON.stringify(t) : "" }, e.ruleData = function (t) { e.data.ruleData = t && "object" == typeof t ? JSON.stringify(t) : "" }, e.getParams = function (e) { url = window.location.href.toLowerCase(), e = e.replace(/[\[\]]/g, "\\$&").toLowerCase(); var t = new RegExp("[?&]" + e + "(=([^&#]*)|&|#|$)").exec(url); return t && t[2] ? decodeURIComponent(t[2].replace(/\+/g, " ")) : "" }, e.init = function () { if (e.auth && (e.data.storage = e.browserStorage(), e.js_callback = "nv_json1", !e.data.iFrame && "noapi" !== e.getParams("nvcheck"))) { var t = "?"; if (e.ab_overlay) { var n = document.createElement("style"), o = "body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}", a = document.getElementsByTagName("head")[0]; n.setAttribute("id", "_nv_hm_hidden_element"), n.setAttribute("type", "text/css"), n.styleSheet ? n.styleSheet.cssText = o : n.appendChild(document.createTextNode(o)), a.appendChild(n), setTimeout(function () { var e = this.document.getElementById("_nv_hm_hidden_element"); if (e) try { e.parentNode.removeChild(e) } catch (t) { e.remove() } }, 2e3) } for (var r in e.data) e.data.hasOwnProperty(r) && (t += encodeURIComponent(r) + "=" + encodeURIComponent(e.data[r]) + "&"); e.load("https://www.notifyvisitors.com/ext/v1/settings" + t) } }, e.browserStorage = function () { var t = { session: e.storage("sessionStorage"), local: e.storage("localStorage") }; return JSON.stringify(t) }, e.storage = function (e) { var t = {}; return window[e].length > 0 && Object.keys(window[e]).forEach(function (n) { -1 !== n.indexOf("_nv_") && (t[n] = window[e][n]) }), t }, e.load = function (e) { var t = document, n = t.createElement("script"); n.src = e, n.type = "text/javascript", t.body ? t.body.appendChild(n) : t.head.appendChild(n) }, e }();
        
    window.notify_visitors.options({
        ab_overlay: false
    });
      
    window.notify_visitors.init();
})();
