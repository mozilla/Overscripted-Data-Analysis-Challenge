// START OF Advanced SmartSource Data Collector TAG
//modified for cmbchina 20121116(zhengzy)
// Version: cmbchina.1.0.02
var gService = false;
var gTimeZone = 8;
// Code section for Enable First-Party Cookie Tracking
function dcsCookie(){
	if (typeof(dcsOther)=="function"){
		dcsOther();
	}
	else if (typeof(dcsPlugin)=="function"){
		dcsPlugin();
	}
	else if (typeof(dcsFPC)=="function"){
		dcsFPC(gTimeZone);
	}
}
function dcsGetCookie(name){
	var pos=document.cookie.indexOf(name+"=");
	if (pos!=-1){
		var start=pos+name.length+1;
		var end=document.cookie.indexOf(";",start);
		if (end==-1){
			end=document.cookie.length;
		}
		return unescape(document.cookie.substring(start,end));
	}
	return null;
}
function dcsGetCrumb(name,crumb){
	var aCookie=dcsGetCookie(name).split(":");
	for (var i=0;i<aCookie.length;i++){
		var aCrumb=aCookie[i].split("=");
		if (crumb==aCrumb[0]){
			return aCrumb[1];
		}
	}
	return null;
}
function dcsGetIdCrumb(name,crumb){
	var cookie=dcsGetCookie(name);
	var id=cookie.substring(0,cookie.indexOf(":lv="));
	var aCrumb=id.split("=");
	for (var i=0;i<aCrumb.length;i++){
		if (crumb==aCrumb[0]){
			return aCrumb[1];
		}
	}
	return null;
}
function dcsFPC(offset){
	if (typeof(offset)=="undefined"){
		return;
	}
	if (document.cookie.indexOf("WTLOPTOUT=")!=-1){
		return;
	}
	var name=gFpc;
	var dCur=new Date();
	var adj=(dCur.getTimezoneOffset()*60000)+(offset*3600000);
	dCur.setTime(dCur.getTime()+adj);
	var dExp=new Date(dCur.getTime()+315360000000);
	var dSes=new Date(dCur.getTime());
	WT.co_f=WT.vt_sid=WT.vt_f=WT.vt_f_a=WT.vt_f_s=WT.vt_f_d=WT.vt_f_tlh=WT.vt_f_tlv="";
	if (document.cookie.indexOf(name+"=")==-1){
		if ((typeof(gWtId)!="undefined")&&(gWtId!="")){
			WT.co_f=gWtId;
		}
		else if ((typeof(gTempWtId)!="undefined")&&(gTempWtId!="")){
			WT.co_f=gTempWtId;
			WT.vt_f="1";
		}
		else{
			WT.co_f="2";
			var cur=dCur.getTime().toString();
			for (var i=2;i<=(32-cur.length);i++){
				WT.co_f+=Math.floor(Math.random()*16.0).toString(16);
			}
			WT.co_f+=cur;
			WT.vt_f="1";
		}
		if (typeof(gWtAccountRollup)=="undefined"){
			WT.vt_f_a="1";
		}
		WT.vt_f_s=WT.vt_f_d="1";
		WT.vt_f_tlh=WT.vt_f_tlv="0";
	}
	else{
		var id=dcsGetIdCrumb(name,"id");
		var lv=parseInt(dcsGetCrumb(name,"lv"));
		var ss=parseInt(dcsGetCrumb(name,"ss"));
		if ((id==null)||(id=="null")||isNaN(lv)||isNaN(ss)){
			return;
		}
		WT.co_f=id;
		var dLst=new Date(lv);
		WT.vt_f_tlh=Math.floor((dLst.getTime()-adj)/1000);
		dSes.setTime(ss);
		if ((dCur.getTime()>(dLst.getTime()+1800000))||(dCur.getTime()>(dSes.getTime()+28800000))){
			WT.vt_f_tlv=Math.floor((dSes.getTime()-adj)/1000);
			dSes.setTime(dCur.getTime());
			WT.vt_f_s="1";
		}
		if ((dCur.getDay()!=dLst.getDay())||(dCur.getMonth()!=dLst.getMonth())||(dCur.getYear()!=dLst.getYear())){
			WT.vt_f_d="1";
		}
	}
	WT.co_f=escape(WT.co_f);
	WT.vt_sid=WT.co_f+"."+(dSes.getTime()-adj);
	var expiry="; expires="+dExp.toGMTString();
	document.cookie=name+"="+"id="+WT.co_f+":lv="+dCur.getTime().toString()+":ss="+dSes.getTime().toString()+expiry+"; path=/"+(((typeof(gFpcDom)!="undefined")&&(gFpcDom!=""))?("; domain="+gFpcDom):(""));
	if (document.cookie.indexOf(name+"=")==-1){
		WT.co_f=WT.vt_sid=WT.vt_f_s=WT.vt_f_d=WT.vt_f_tlh=WT.vt_f_tlv="";
		WT.vt_f=WT.vt_f_a="2";
	}
}

//var gFpc="WT_FPC";

function dcsMultiTrack(){
	if (arguments.length%2==0){
		for (var i=0;i<arguments.length;i+=2){
			if (arguments[i].indexOf('WT.')==0){
				WT[arguments[i].substring(3)]=arguments[i+1];
			}
			else if (arguments[i].indexOf('DCS.')==0){
				DCS[arguments[i].substring(4)]=arguments[i+1];
			}
			else if (arguments[i].indexOf('DCSext.')==0){
				DCSext[arguments[i].substring(7)]=arguments[i+1];
			}
		}
		var dCurrent=new Date();
		DCS.dcsdat=dCurrent.getTime();
		dcsFunc("dcsCookie");
		dcsTag();
	}
}

function dcsAdv(){
	dcsFunc("dcsET");
	dcsFunc("dcsCookie");
	dcsFunc("dcsAdSearch");
	dcsFunc("dcsTP");
}
// END OF Advanced SmartSource Data Collector TAG

// START OF Basic SmartSource Data Collector TAG
var gImages=new Array;
var gIndex=0;
var DCS=new Object();
var WT=new Object();
var DCSext=new Object();
var gQP=new Array();
var gI18n=true;
var gDomain="sdc.cmbchina.com"; 
var gDcsId="dcs5w0txb10000wocrvqy1nqm_6n1p";
var gDCSQQImg=new Image(); 
if (window.RegExp){
	var RE={"%09":/\t/g,"%20":/ /g,"%23":/\#/g,"%26":/\&/g,"%2B":/\+/g,"%3F":/\?/g,"%5C":/\\/g,"%22":/\"/g,"%7F":/\x7F/g,"%A0":/\xA0/g};
	var I18NRE={"%25":/\%/g};
}

function dcsVar(){
	var dCurrent=new Date();
	WT.tz=dCurrent.getTimezoneOffset()/60*-1;		
	if (WT.tz==0){
		WT.tz="0";
	}
	WT.bh=dCurrent.getHours();
	WT.ul=navigator.appName=="Netscape"?navigator.language:navigator.userLanguage;
	if (typeof(screen)=="object"){
		WT.cd=navigator.appName=="Netscape"?screen.pixelDepth:screen.colorDepth;
		WT.sr=screen.width+"x"+screen.height;
	}
	if (typeof(navigator.javaEnabled())=="boolean"){
		WT.jo=navigator.javaEnabled()?"Yes":"No";
	}
	if (document.title){
		WT.ti=gI18n?dcsEscape(dcsEncode(document.title),I18NRE):document.title;
	}
	WT.js="Yes";
/*
	if (document.body&&document.body.addBehavior){
		document.body.addBehavior("#default#clientCaps");
		WT.ct=document.body.connectionType||"unknown";
		document.body.addBehavior("#default#homePage");
		WT.hp=document.body.isHomePage(location.href)?"1":"0";
	}
	else{
		WT.ct="unknown";
	}
*/
	if (parseInt(navigator.appVersion)>3){
		if ((navigator.appName=="Microsoft Internet Explorer")&&document.body){
			WT.bs=document.body.offsetWidth+"x"+document.body.offsetHeight;
		}
		else if (navigator.appName=="Netscape"){
			WT.bs=window.innerWidth+"x"+window.innerHeight;
		}
	}
	WT.fi="No";
	if (window.ActiveXObject){
		for(var i=10;i>0;i--){
			try{
				var flash = new ActiveXObject("ShockwaveFlash.ShockwaveFlash."+i);
				WT.fi="Yes";
				WT.fv=i+".0";
				break;
			}
			catch(e){
			}
		}
	}
	else if (navigator.plugins&&navigator.plugins.length){
		for (var i=0;i<navigator.plugins.length;i++){
			if (navigator.plugins[i].name.indexOf('Shockwave Flash')!=-1){
				WT.fi="Yes";
				WT.fv=navigator.plugins[i].description.split(" ")[2];
				break;
			}
		}
	}
	if (gI18n){
		WT.em=(typeof(encodeURIComponent)=="function")?"uri":"esc";
		if (typeof(document.defaultCharset)=="string"){
			WT.le=document.defaultCharset;
		} 
		else if (typeof(document.characterSet)=="string"){
			WT.le=document.characterSet;
		}
	}
	WT.tv="8.0.2";
//	WT.sp="@@SPLITVALUE@@";
	DCS.dcsdat=dCurrent.getTime();
	DCS.dcssip=window.location.hostname;
	DCS.dcsuri=window.location.pathname;
	if (window.location.search){
		DCS.dcsqry=window.location.search;
		if (gQP.length>0){
			for (var i=0;i<gQP.length;i++){
				var pos=DCS.dcsqry.indexOf(gQP[i]);
				if (pos!=-1){
					var front=DCS.dcsqry.substring(0,pos);
					var end=DCS.dcsqry.substring(pos+gQP[i].length,DCS.dcsqry.length);
					DCS.dcsqry=front+end;
				}
			}
		}
	}
	if ((window.document.referrer!="")&&(window.document.referrer!="-")){
		if (!(navigator.appName=="Microsoft Internet Explorer"&&parseInt(navigator.appVersion)<4)){
			//DCS.dcsref=gI18n?dcsEscape(window.document.referrer, I18NRE):window.document.referrer;
			DCS.dcsref=gI18n?dcsEscape(trim(window.document.referrer), I18NRE):trim(window.document.referrer);
		}
	}
}

function dcsA(N,V){
	return "&"+N+"="+dcsEscape(V, RE);
}

function dcsEscape(S, REL){
	if (typeof(REL)!="undefined"){
		var retStr = new String(S);
		for (var R in REL){
			retStr = retStr.replace(REL[R],R);
		}
		return retStr;
	}
	else{
		return escape(S);
	}
}

function dcsLoadHref(evt){
	if ((typeof(gHref)!="undefined")&&(gHref.length>0)){
		window.location=gHref;
		gHref="";
	}
}
function dcsCreateImage(dcsSrc){
	if (document.images){
		gImages[gIndex]=new Image;
		if ((typeof(gHref)!="undefined")&&(gHref.length>0)){
			gImages[gIndex].onload=gImages[gIndex].onerror=dcsLoadHref;
		}
		gImages[gIndex].src=dcsSrc;
		gIndex++;
	}
	else{ 
		gDCSQQImg.border=0;
		gDCSQQImg.name="DCSIMG";
		gDCSQQImg.width=1;
		gDCSQQImg.height=1;
		gDCSQQImg.src=dcsSrc; 
	}
}

function dcsEncode(S){
	return (typeof(encodeURIComponent)=="function")?encodeURIComponent(S):escape(S);
}

function dcsMeta(){
	var elems;
	if (document.all){
		elems=document.all.tags("meta");
	}
	else if (document.documentElement){
		elems=document.getElementsByTagName("meta");
	}
	if (typeof(elems)!="undefined"){
		var length=elems.length;
		for (var i=0;i<length;i++){
			var name=elems.item(i).name;
			var content=elems.item(i).content;
			var equiv=elems.item(i).httpEquiv;
			if (name.length>0){
				if (name.indexOf("WT.")==0){
					WT[name.substring(3)]=content;
				}
				else if (name.indexOf("DCSext.")==0){
					DCSext[name.substring(7)]=content;
				}
				else if (name.indexOf("DCS.")==0){
					DCS[name.substring(4)]=content;
				}
			}
			else if (gI18n&&(equiv=="Content-Type")){
				var pos=content.toLowerCase().indexOf("charset=");
				if (pos!=-1){
					WT.mle=content.substring(pos+8);
				}
			}
		}
	}
}
function dcsTag(){
	if (document.cookie.indexOf("WTLOPTOUT=")!=-1){
		return;
	}
	if(DCS.dcsref&&DCS.dcsref.length>1024)
	{
	    if(DCS.dcsref.indexOf('?')>0) DCS.dcsref = DCS.dcsref.substring(0,DCS.dcsref.indexOf('?'));
	}
	var P="http"+(window.location.protocol.indexOf('https:')==0?'s':'')+"://"+gDomain+(gDcsId==""?'':'/'+gDcsId)+"/dcs.gif?";
	for (var N in DCS){
		if (DCS[N]) {
			P+=dcsA(N,DCS[N]);
		}
	}
	var keys=["co_f","vt_sid","vt_f_tlv"];
	for (var i=0;i<keys.length;i++){
		var key=keys[i];
		if (WT[key]){
			P+=dcsA("WT."+key,WT[key]);
			delete WT[key];
		}
	}
	for (N in WT){
		if (WT[N]) {
			P+=dcsA("WT."+N,dcsCode(WT[N]));
		}
	}
	for (N in DCSext){
		if (DCSext[N]) {
			P+=dcsA(N,DCSext[N]);
		}
	}
	if (P.length>2048&&navigator.userAgent.indexOf('MSIE')>=0){
		P=P.substring(0,2040)+"&WT.tu=1";
	}
	dcsCreateImage(P);
}


function dcsFunc(func){
	if (typeof(window[func])=="function"){
		window[func]();
	}
}
function dcsCode(txt)
{
    if(/.*[\u0391-\uFFE5]+.*$/.test(txt))
        return gI18n?dcsEscape(dcsEncode(txt),I18NRE):dcsEncode(txt);
    else if(dcsIsExec(txt,"%..%.."))
        return gI18n?dcsEscape(txt,I18NRE):txt;
    else  return txt;
}
function dcsIsExec(str, regstr)
{
    var reg=new RegExp(regstr);
    
    if(reg.exec(str)) return true;
    else return false;
}
function dcsGetValue(obj,name)
{
    if(obj.attributes[name]!=null) 
        return obj.attributes[name].nodeValue;
    else if(obj.attributes[name.toLowerCase()]!=null) 
        return obj.attributes[name.toLowerCase()].nodeValue;
    else
        return "";
}
function autoclick() {
    var object = new Array();
    //IE
    if (window.attachEvent) {
        if(document)
        {
            document.detachEvent('onclick', documentClick);
            document.attachEvent('onclick', documentClick);
        }
    }

    //firefox
    else if (window.addEventListener) {
        if(document)
        {
            document.addEventListener('click', documentClick, false);
        }
    }
}
function documentClick(evt)
{
	var target;
    //firefox
    if (window.addEventListener) target = evt.target;
    //IE
    if (window.attachEvent) target = window.event.srcElement;
    
	var objecturl;
	var columnname;
	var objectname;
	var objecttype;
	var pagetitle = gI18n?dcsEscape(dcsEncode(document.title),I18NRE):document.title;
	var ip = window.location.hostname;
	var click = 'click';
	
	if (target.tagName == 'IMG')
	{
		target = target.parentElement;
	}
	if (target.tagName == 'A')
	{			
		objecturl = target.href;
		columnname = dcsCode(dcsGetValue(target,"cname"));
		objectname = dcsCode(dcsGetValue(target,"oname"));
		objecttype = dcsCode(dcsGetValue(target,"otype"));			
	}
	else if (target.tagName == 'INPUT')
	{
		objecturl = 'NOTSET';
		columnname = dcsCode(dcsGetValue(target,"cname"));
		objectname = dcsCode(dcsGetValue(target,"oname"));
		objecttype = dcsCode(dcsGetValue(target,"otype"));	
	}	
	if (columnname != null && columnname != '' && columnname != 'undefined')
	{   		
		dcsMultiTrack('DCS.dcssip',ip,'DCS.dcsuri',objecturl,'WT.ti',objectname,'DCSext.wt_click',click, 'DCSext.wt_cname', columnname, 'DCSext.wt_otype', objecttype, 'DCSext.wt.domain', ip, 'DCSext.wt_ptitle', pagetitle);						
	}	
}

function init()
{
    
	dcsVar();
	dcsMeta();
	dcsFunc("dcsAdv");
	dcsTag();		
	
}
init();
autoclick();

function RedirectUrl(adcolumn, adname, adurl)
{		
	var ADColumn = gI18n?dcsEscape(dcsEncode(adcolumn),I18NRE):adcolumn;	
	var ADName = gI18n?dcsEscape(dcsEncode(adname),I18NRE):adname;	
	var ip = window.location.hostname;
	var pagetitle = gI18n?dcsEscape(dcsEncode(document.title),I18NRE):document.title;
	
	dcsMultiTrack('DCS.dcssip',ip,'DCS.dcsuri',adurl,'WT.ti',ADName,'DCSext.wt_click',"adclick", 'DCSext.wt_cname', ADColumn, 'DCSext.wt_otype', "advtype", 'DCSext.wt.domain', ip, 'DCSext.wt_ptitle', pagetitle);							
	window.open(adurl);
}

function trim(s)
{
    var str = new String(s);
    return str.replace(/(^\s*)|(\s*$)/g, '');
} 