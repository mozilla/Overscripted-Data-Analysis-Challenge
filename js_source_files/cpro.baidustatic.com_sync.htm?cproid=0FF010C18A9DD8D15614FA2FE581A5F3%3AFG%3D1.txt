<!DOCTYPE html>
<html>
    
    <head></head>
    
    <body>
        <script type="text/javascript">
            var sendByIframe = function (b) {
                    var c = document.createElement("iframe");
                    c.style.display = "none";
                    c.setAttribute("src", b);
                    document.body.insertBefore(c, document.body.firstChild)
                },
                getCookie = function (b, c) {
                    var a;
                    c = c || window;
                    var d = RegExp("(^| )" + b + "=([^;]*)(;|$)").exec(c.document.cookie);
                    d && (a = d[2]);
                    return a
                },
                setCookie = function (b, c, a) {
                    a = a || {};
                    var d = a.expires;
                    "number" == typeof a.expires && (d = new Date, d.setTime(d.getTime() + a.expires));
                    document.cookie = b + "=" + c + (a.path ? "; path=" + a.path : "") + (d ? "; expires=" + d.toGMTString() : "") + (a.domain ? "; domain=" + a.domain : "") + (a.secure ? "; secure" : "")
                },
                getUrlParam = function (b) {
                    b = RegExp("(^|&)" + b + "=([^&]*)(&|$)", "i");
                    b = window.location.search.substr(1).match(b);
                    return null != b ? decodeURIComponent(b[2]) : null
                },
                currentDomain = document.domain.toLowerCase(),
                referDomain = (document.referrer ? document.referrer.match(/.*\:\/\/([^\/]*).*/i)[1] : "").toLowerCase(),
                urlCproId = getUrlParam("CPROID"),
                cookieCproId = getCookie("CPROID"),
                targetCproId;
            urlCproId && "cpro.baidustatic.com" === currentDomain && "cpro.baidu.com" === referDomain ? (cookieCproId ? targetCproId = cookieCproId : (setCookie("CPROID", urlCproId, {
                expires: (new Date).setFullYear(2042)
            }), targetCproId = urlCproId), targetCproId && sendByIframe("//cpro.baidu.com/sync.htm?cproid=" + encodeURIComponent(targetCproId))) : urlCproId && "cpro.baidu.com" === currentDomain && "cpro.baidustatic.com" === referDomain && setCookie("CPROID", urlCproId, {
                expires: (new Date).setFullYear(2042)
            });

            var referDomainRegEx=/(^|\.)pos\.baidu\.com$/gi;
            urlCproId && ("cpro.baidustatic.com" === currentDomain && referDomainRegEx.test(referDomain) ) && (cookieCproId ? targetCproId = cookieCproId : (targetCproId = urlCproId, setCookie("CPROID", urlCproId, {
                expires: (new Date).setFullYear(2042)
            })), targetCproId && sendByIframe("//pos.baidu.com/sync_pos.htm?cproid=" + encodeURIComponent(targetCproId)));
        </script>
    </body>

</html>