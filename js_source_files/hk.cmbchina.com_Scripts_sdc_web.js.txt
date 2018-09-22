
var gDomain="sdc.cmbchina.com";	// SDC Production Mode Domain
var gDcsId="dcs5w0txb10000wocrvqy1nqm_6n1p";
var gFpc="WTFPC";
var gConvert=true;
var gWTIDJS=window.document.createElement("script"); 

window.document.getElementsByTagName("head")[0].appendChild(gWTIDJS); 

if ((typeof(gConvert)!="undefined")&&gConvert&&(document.cookie.indexOf(gFpc+"=")==-1)&&(document.cookie.indexOf("WTLOPTOUT=")==-1)){
 gWTIDJS.src="http"+(window.location.protocol.indexOf('https:')==0?'s':'')+"://"+gDomain+"/"+gDcsId+"/wtid.js"; 
}

setTimeout('setsdcjs()',0);
function setsdcjs(){   
    var jDomain="fx.cmbchina.com";
   var js_path="/scripts/sdc_cmb.js";
   var domain="http"+(window.location.protocol.indexOf('https:')==0?'s':'')+"://"+jDomain;
   var SDC_js=document.createElement("script");
   SDC_js.src=domain+js_path;
   var headElem=document.getElementsByTagName("head")[0];
   headElem.appendChild(SDC_js);   
}