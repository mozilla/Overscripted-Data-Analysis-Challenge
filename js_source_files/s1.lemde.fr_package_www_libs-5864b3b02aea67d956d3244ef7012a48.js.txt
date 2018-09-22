/**
 * Package www/libs
 * lmd/module/capping-sensibilisation
 * hgn/www/templates/module/evenementiel/sensibilisation/banner.html.mu.js@abs
 * jquery.noconflict
 * domReady
 * template
 * hoganpower
 * lib/jquery/plugin/jquery.waypoint
 * lib/jquery/plugin/jquery.prettydate
 * lib/jquery/plugin/jquery.mousewheel
 * lib/jquery/plugin/jquery.cookie
 * lib/jquery/plugin/jquery.spin
 * lib/jquery/plugin/jquery.ajah
 * lib/jquery/plugin/jquery.lazyload
 * hogan
 * lib/crypto/core/md5
 * lib/object-path
 * lib/hashes
 */

/* -- start module lmd/module/capping-sensibilisation -- */
define("lmd/module/capping-sensibilisation",["hoganpower!/templates/module/evenementiel/sensibilisation/banner.html.mu@www"],function(e){"use strict";var n,t,r=document.querySelector(".top_container_article");r&&(r.innerHTML=e.render(),t=document.getElementById("js-blocker-banner"),n=document.createElement("span"),n.className="fermer",n.innerHTML="×",t.appendChild(n),n.addEventListener("click",function(){t.style.display="none"}))});
/* -- end module lmd/module/capping-sensibilisation -- */
/* -- start module hgn/www/templates/module/evenementiel/sensibilisation/banner.html.mu.js@abs -- */
define("hgn/www/templates/module/evenementiel/sensibilisation/banner.html.mu.js@abs",function(){return function(c,p,i){var _=this;_.b(i=i||"");_.b("\n" + i);_.b("<div id=\"js-blocker-banner\" class=\"bandeau-bloqueur-article\">");_.b("\n" + i);_.b("    <figure id=\"illustration-formelle\">");_.b("\n" + i);_.b("        <img src=\"http://s1.lemde.fr/medias/web/img/evenementiel/sensibilisation/jerome-fenoglio.jpg\" alt=\"Jérôme Fenoglio\" width=\"102\" height=\"128\" />");_.b("\n" + i);_.b("        <figcaption>Jérôme Fenoglio, <br>directeur du Monde</figcaption>");_.b("\n" + i);_.b("    </figure>");_.b("\n" + i);_.b("\n" + i);_.b("    <div class=\"contenu-soutien\">");_.b("\n" + i);_.b("        <strong>Il semblerait que vous utilisiez un logiciel destiné à bloquer les publicités.</strong>");_.b("\n" + i);_.b("        <p>");_.b("\n" + i);_.b("        En bloquant la publicité, vous privez Le Monde.fr de sa principale source de revenus.<br>");_.b("\n" + i);_.b("        Si vous appréciez notre contenu, si vous aimez Le Monde.fr, soutenez-nous en désactivant votre adblock ou en vous abonnant à 1€ pour 3 mois. Merci&nbsp;!");_.b("\n" + i);_.b("        </p>");_.b("\n" + i);_.b("    </div>");_.b("\n" + i);_.b("    <div class=\"contenu-pedago\">");_.b("\n" + i);_.b("        <strong>Il semblerait que vous utilisiez un bloqueur de publicité.</strong>");_.b("\n" + i);_.b("        <p>Le Monde.fr est financé par la publicité, celle-ci nous permet de vous proposer nos contenus gratuitement.</p>");_.b("\n" + i);_.b("    </div>");_.b("\n" + i);_.b("\n" + i);_.b("    <div class=\"bloqueur-cta\">");_.b("\n" + i);_.b("        <a href=\"/modele-economique/tuto/\"");_.b("\n" + i);_.b("           title=\"Comment désactiver son adblocker pour un site spécifique\" class=\"btn btn_bleu\">");_.b("\n" + i);_.b("            Je désactive mon bloqueur de publicité");_.b("\n" + i);_.b("        </a>");_.b("\n" + i);_.b("        <b>ou</b>");_.b("\n" + i);_.b("        <a href=\"https://checkout.lemonde.fr/glm_onestepcheckout/onestep/#xtor=AL-360-[B_Soutien]\"");_.b("\n" + i);_.b("           title=\"Offre spéciale d’abonnement au Monde.fr\" class=\"btn btn_abo contenu-soutien\">");_.b("\n" + i);_.b("            Je m’abonne à 1€ pour 3 mois");_.b("\n" + i);_.b("        </a>");_.b("\n" + i);_.b("        <a href=\"https://checkout.lemonde.fr/glm_onestepcheckout/onestep/#xtor=AL-360-[B_Pedago]\"");_.b("\n" + i);_.b("           title=\"Offre spéciale d’abonnement au Monde.fr\" class=\"btn btn_abo contenu-pedago\">");_.b("\n" + i);_.b("            Je m’abonne à 1€ pour 3 mois");_.b("\n" + i);_.b("        </a>");_.b("\n" + i);_.b("    </div>");_.b("\n" + i);_.b("</div>");_.b("\n");return _.fl();;}})
/* -- end module hgn/www/templates/module/evenementiel/sensibilisation/banner.html.mu.js@abs -- */
/* -- start module jquery.noconflict -- */
/**
 * Custom jQuery loader to handle the lib without exposing $ to global scope
 *
 * Install:
 * Add this config in require config:
 *
 * map: {
 *   "*": {
 *     "jquery": "noconflict"
 *   },
 *   "noconflict": {
 *     "jquery": "jquery"
 *   }
 * }
 *
 * For ie <= 8, jquery 1.11.0 is loaded
 * For other, overly bloated & highfaluting Web browsers, we use 2.x.x
 *
 */

var jqyreu = jqyreu || {
   v: (window.getElementsByClassName) ? 'jquery': 'jquery.fallback',
   j: window.$ || window.jQuery
};

define("jquery.noconflict",[jqyreu.v], function ($) {
   // Our own
   var localjQuery = $.noConflict(true);

   // Restore backups
   window.$ = window.jQuery = jqyreu.j;

   // Use the right stuff
   return localjQuery;
});

/* -- end module jquery.noconflict -- */
/* -- start module domReady -- */
/**
 * @license RequireJS domReady 2.0.0 Copyright (c) 2010-2012, The Dojo Foundation All Rights Reserved.
 * Available via the MIT or new BSD license.
 * see: http://github.com/requirejs/domReady for details
 */
/*jslint */
/*global require: false, define: false, requirejs: false,
  window: false, clearInterval: false, document: false,
  self: false, setInterval: false */


define("domReady",function () {
    'use strict';

    var isBrowser = typeof window !== "undefined" && window.document,
        isPageLoaded = !isBrowser,
        doc = isBrowser ? document : null,
        readyCalls = [],
        isTop, testDiv, scrollIntervalId;

    function runCallbacks(callbacks) {
        var i;
        for (i = 0; i < callbacks.length; i++) {
            callbacks[i](doc);
        }
    }

    function callReady() {
        var callbacks = readyCalls;

        if (isPageLoaded) {
            //Call the DOM ready callbacks
            if (callbacks.length) {
                readyCalls = [];
                runCallbacks(callbacks);
            }
        }
    }

    /**
     * Sets the page as loaded.
     */
    function pageLoaded() {
        if (!isPageLoaded) {
            isPageLoaded = true;
            if (scrollIntervalId) {
                clearInterval(scrollIntervalId);
            }

            callReady();
        }
    }

    if (isBrowser) {
        if (document.addEventListener) {
            //Standards. Hooray! Assumption here that if standards based,
            //it knows about DOMContentLoaded.
            document.addEventListener("DOMContentLoaded", function(){setTimeout(pageLoaded, 1);}, false);
            window.addEventListener("load", pageLoaded, false);
        } else if (window.attachEvent) {
            window.attachEvent("onload", pageLoaded);

            testDiv = document.createElement('div');
            try {
                isTop = window.frameElement === null;
            } catch(e) {}

            //DOMContentLoaded approximation that uses a doScroll, as found by
            //Diego Perini: http://javascript.nwbox.com/IEContentLoaded/,
            //but modified by other contributors, including jdalton
            if (testDiv.doScroll && isTop && window.external) {
                scrollIntervalId = setInterval(function () {
                    try {
                        testDiv.doScroll();
                        pageLoaded();
                    } catch (e) {}
                }, 30);
            }
        }
        
        var isMSIE = /*@cc_on!@*/0;

        //Check if document already complete, and if so, just trigger page load
        //listeners. Latest webkit browsers also use "interactive", and
        //will fire the onDOMContentLoaded before "interactive" but not after
        //entering "interactive" or "complete". More details:
        //http://dev.w3.org/html5/spec/the-end.html#the-end
        //http://stackoverflow.com/questions/3665561/document-readystate-of-interactive-vs-ondomcontentloaded
        if (document.readyState === "complete" ||
            (document.readyState === "interactive" && !isMSIE)) {
            pageLoaded();
        }
    }

    /** START OF PUBLIC API **/

    /**
     * Registers a callback for DOM ready. If DOM is already ready, the
     * callback is called immediately.
     * @param {Function} callback
     */
    function domReady(callback) {
        if (isPageLoaded) {
            callback(doc);
        } else {
            readyCalls.push(callback);
        }
        return domReady;
    }

    domReady.version = '2.0.0';

    /**
     * Loader Plugin API method
     */
    domReady.load = function (name, req, onLoad, config) {
        if (config.isBuild) {
            onLoad(null);
        } else {
            domReady(onLoad);
        }
    };

    /** END OF PUBLIC API **/

    return domReady;
});
/* -- end module domReady -- */
/* -- start module template -- */
/**
 * Template plugin
 * @TODO possibilité de charger des partials et des layouts
 * 
 * <example>
 * require(["template!/templates/module/general/live-player.html.mu"], function (html) {
 *    console.log(html); 
 * });
 * </example>
 */
define("template",["jquery", "lib/crypto/core/md5", "lmd/core/conf"], function ($, md5, conf)
{
   var template = {
      version: '0.0.42',

      /**
       * @type string   url
       * @type function callback
       * @return void
       */
      get: function (url, callback)
      {
         $.ajax({
            url: "http://" + conf.www.location.hostname + url,
            type: "GET",
            dataType: "jsonp text",
            jsonpCallback : "cb" + md5(url),
            cache : true,
            timeout : 5000
            }).done(callback);
      },

      /**
       * @see http://requirejs.org/docs/plugins.html#apiload
       * @type string   name     "/templates/foo/bar.html.mu"
       * @type req      object   local require
       * @type function onLoad   when loading is done
       * @type config   object
       * @return void
       */
      load: function (name, req, onLoad, config)
      {
         template.get(name, onLoad);
      }
   };
   
   
   return template;
});
/* -- end module template -- */
/* -- start module hoganpower -- */
define("hoganpower",function (require) {
        'use strict';

        var conf = require('lmd/core/conf');
        var hogan = require('hogan');

        // We don’t do specific templates for wwws or other obscure places
        var validApps = { 'www': true, 'abonnes': true, 'mobile': true, 'common': true, 'api': true };
        var defaultApp = 'www';
        var absPath = '//' + conf.medias.location.hostname + '/';

        // requirejs configuration (undocumented); hope this doesn’t move over time
        var requireKnownPaths = window.requirejs.s.contexts._.config.paths;

        return {
            /** version, required by requirejs */
            version: '0.0.2',
            load: loadTemplate
        };

        /**
         * @see http://requirejs.org/docs/plugins.html#apiload
         * @type string name '/templates/foo/bar.html.mu'
         * @type req object local require
         * @type function onLoad when loading is done
         * @type config object
         * JShint note: function signature is from requirejs
         */
        function loadTemplate(name, req, onLoad, config) { /* jshint ignore:line */
            var appMatches = name.match(/([^@]*)@([^@]*)/);
            var app;
            var path;

            if (appMatches) {
                name = appMatches[1];
                if (validApps[appMatches[2]]) {
                    app = appMatches[2];
                }
            }

            app = app || validApp();

            path = makePath(app, name);

            require([path], function (tpl) {
                onLoad(new hogan.Template(tpl));
            });
        }

        /**
         * Takes the current app from configuration and returns
         * something relevant as app for the template path
         * @return string
         */
        function validApp() {
            return validApps[conf.current.app] && conf.current.app || defaultApp;
        }

        /**
         * Builds the final template require path
         * Two possible cases: either require will be able to resolve template
         * paths, either not — in which case we require the full URL
         * @param string app The application (see validApps)
         * @param string name The significant path to the template file
         * @return string The require URL
         */
        function makePath(app, name) {
            var path = 'hgn/' + app + name + '.js';
            var reqPath = path + '@abs';
            if (typeof requireKnownPaths[reqPath] === 'string') {
                return reqPath;
            } else {
                return absPath + path;
            }
        };
    }
);

/* -- end module hoganpower -- */
/* -- start module lib/jquery/plugin/jquery.waypoint -- */
// Generated by CoffeeScript 1.4.0

/*
 jQuery Waypoints - v2.0.2
 Copyright (c) 2011-2013 Caleb Troughton
 Dual licensed under the MIT license and GPL license.
 https://github.com/imakewebthings/jquery-waypoints/blob/master/licenses.txt
 */

define("lib/jquery/plugin/jquery.waypoint",["jquery"], function (jQuery) {
   var __indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; },
      __slice = [].slice;

   (function ($) {
      var $w, Context, Waypoint, allWaypoints, contextCounter, contextKey, contexts, isTouch, jQMethods, methods, resizeEvent, scrollEvent, waypointCounter, waypointKey, wp, wps;
      $w = $(window);
      isTouch = __indexOf.call(window, 'ontouchstart') >= 0;
      allWaypoints = {
         horizontal:{},
         vertical:{}
      };
      contextCounter = 1;
      contexts = {};
      contextKey = 'waypoints-context-id';
      resizeEvent = 'resize.waypoints';
      scrollEvent = 'scroll.waypoints';
      waypointCounter = 1;
      waypointKey = 'waypoints-waypoint-ids';
      wp = 'waypoint';
      wps = 'waypoints';
      Context = (function () {

         function Context($element) {
            var _this = this;
            this.$element = $element;
            this.element = $element[0];
            this.didResize = false;
            this.didScroll = false;
            this.id = 'context' + contextCounter++;
            this.oldScroll = {
               x:$element.scrollLeft(),
               y:$element.scrollTop()
            };
            this.waypoints = {
               horizontal:{},
               vertical:{}
            };
            $element.data(contextKey, this.id);
            contexts[this.id] = this;
            $element.bind(scrollEvent, function () {
               var scrollHandler;
               if (!(_this.didScroll || isTouch)) {
                  _this.didScroll = true;
                  scrollHandler = function () {
                     _this.doScroll();
                     return _this.didScroll = false;
                  };
                  return window.setTimeout(scrollHandler, $[wps].settings.scrollThrottle);
               }
            });
            $element.bind(resizeEvent, function () {
               var resizeHandler;
               if (!_this.didResize) {
                  _this.didResize = true;
                  resizeHandler = function () {
                     $[wps]('refresh');
                     return _this.didResize = false;
                  };
                  return window.setTimeout(resizeHandler, $[wps].settings.resizeThrottle);
               }
            });
         }

         Context.prototype.doScroll = function () {
            var axes,
               _this = this;
            axes = {
               horizontal:{
                  newScroll:this.$element.scrollLeft(),
                  oldScroll:this.oldScroll.x,
                  forward:'right',
                  backward:'left'
               },
               vertical:{
                  newScroll:this.$element.scrollTop(),
                  oldScroll:this.oldScroll.y,
                  forward:'down',
                  backward:'up'
               }
            };
            if (isTouch && (!axes.vertical.oldScroll || !axes.vertical.newScroll)) {
               $[wps]('refresh');
            }
            $.each(axes, function (aKey, axis) {
               var direction, isForward, triggered;
               triggered = [];
               isForward = axis.newScroll > axis.oldScroll;
               direction = isForward ? axis.forward : axis.backward;
               $.each(_this.waypoints[aKey], function (wKey, waypoint) {
                  var _ref, _ref1;
                  if ((axis.oldScroll < (_ref = waypoint.offset) && _ref <= axis.newScroll)) {
                     return triggered.push(waypoint);
                  } else if ((axis.newScroll < (_ref1 = waypoint.offset) && _ref1 <= axis.oldScroll)) {
                     return triggered.push(waypoint);
                  }
               });
               triggered.sort(function (a, b) {
                  return a.offset - b.offset;
               });
               if (!isForward) {
                  triggered.reverse();
               }
               return $.each(triggered, function (i, waypoint) {
                  if (waypoint.options.continuous || i === triggered.length - 1) {
                     return waypoint.trigger([direction]);
                  }
               });
            });
            return this.oldScroll = {
               x:axes.horizontal.newScroll,
               y:axes.vertical.newScroll
            };
         };

         Context.prototype.refresh = function () {
            var axes, cOffset, isWin,
               _this = this;
            isWin = $.isWindow(this.element);
            cOffset = this.$element.offset();
            this.doScroll();
            axes = {
               horizontal:{
                  contextOffset:isWin ? 0 : cOffset.left,
                  contextScroll:isWin ? 0 : this.oldScroll.x,
                  contextDimension:this.$element.width(),
                  oldScroll:this.oldScroll.x,
                  forward:'right',
                  backward:'left',
                  offsetProp:'left'
               },
               vertical:{
                  contextOffset:isWin ? 0 : cOffset.top,
                  contextScroll:isWin ? 0 : this.oldScroll.y,
                  contextDimension:isWin ? $[wps]('viewportHeight') : this.$element.height(),
                  oldScroll:this.oldScroll.y,
                  forward:'down',
                  backward:'up',
                  offsetProp:'top'
               }
            };
            return $.each(axes, function (aKey, axis) {
               return $.each(_this.waypoints[aKey], function (i, waypoint) {
                  var adjustment, elementOffset, oldOffset, _ref, _ref1;
                  adjustment = waypoint.options.offset;
                  oldOffset = waypoint.offset;
                  elementOffset = $.isWindow(waypoint.element) ? 0 : waypoint.$element.offset()[axis.offsetProp];
                  if ($.isFunction(adjustment)) {
                     adjustment = adjustment.apply(waypoint.element);
                  } else if (typeof adjustment === 'string') {
                     adjustment = parseFloat(adjustment);
                     if (waypoint.options.offset.indexOf('%') > -1) {
                        adjustment = Math.ceil(axis.contextDimension * adjustment / 100);
                     }
                  }
                  waypoint.offset = elementOffset - axis.contextOffset + axis.contextScroll - adjustment;
                  if ((waypoint.options.onlyOnScroll && (oldOffset != null)) || !waypoint.enabled) {
                     return;
                  }
                  if (oldOffset !== null && (oldOffset < (_ref = axis.oldScroll) && _ref <= waypoint.offset)) {
                     return waypoint.trigger([axis.backward]);
                  } else if (oldOffset !== null && (oldOffset > (_ref1 = axis.oldScroll) && _ref1 >= waypoint.offset)) {
                     return waypoint.trigger([axis.forward]);
                  } else if (oldOffset === null && axis.oldScroll >= waypoint.offset) {
                     return waypoint.trigger([axis.forward]);
                  }
               });
            });
         };

         Context.prototype.checkEmpty = function () {
            if ($.isEmptyObject(this.waypoints.horizontal) && $.isEmptyObject(this.waypoints.vertical)) {
               this.$element.unbind([resizeEvent, scrollEvent].join(' '));
               return delete contexts[this.id];
            }
         };

         return Context;

      })();
      Waypoint = (function () {

         function Waypoint($element, context, options) {
            var idList, _ref;
            options = $.extend({}, $.fn[wp].defaults, options);
            if (options.offset === 'bottom-in-view') {
               options.offset = function () {
                  var contextHeight;
                  contextHeight = $[wps]('viewportHeight');
                  if (!$.isWindow(context.element)) {
                     contextHeight = context.$element.height();
                  }
                  return contextHeight - $(this).outerHeight();
               };
            }
            this.$element = $element;
            this.element = $element[0];
            this.axis = options.horizontal ? 'horizontal' : 'vertical';
            this.callback = options.handler;
            this.context = context;
            this.enabled = options.enabled;
            this.id = 'waypoints' + waypointCounter++;
            this.offset = null;
            this.options = options;
            context.waypoints[this.axis][this.id] = this;
            allWaypoints[this.axis][this.id] = this;
            idList = (_ref = $element.data(waypointKey)) != null ? _ref : [];
            idList.push(this.id);
            $element.data(waypointKey, idList);
         }

         Waypoint.prototype.trigger = function (args) {
            if (!this.enabled) {
               return;
            }
            if (this.callback != null) {
               this.callback.apply(this.element, args);
            }
            if (this.options.triggerOnce) {
               return this.destroy();
            }
         };

         Waypoint.prototype.disable = function () {
            return this.enabled = false;
         };

         Waypoint.prototype.enable = function () {
            this.context.refresh();
            return this.enabled = true;
         };

         Waypoint.prototype.destroy = function () {
            delete allWaypoints[this.axis][this.id];
            delete this.context.waypoints[this.axis][this.id];
            return this.context.checkEmpty();
         };

         Waypoint.getWaypointsByElement = function (element) {
            var all, ids;
            ids = $(element).data(waypointKey);
            if (!ids) {
               return [];
            }
            all = $.extend({}, allWaypoints.horizontal, allWaypoints.vertical);
            return $.map(ids, function (id) {
               return all[id];
            });
         };

         return Waypoint;

      })();
      methods = {
         init:function (f, options) {
            var _ref;
            if (options == null) {
               options = {};
            }
            if ((_ref = options.handler) == null) {
               options.handler = f;
            }
            this.each(function () {
               var $this, context, contextElement, _ref1;
               $this = $(this);
               contextElement = (_ref1 = options.context) != null ? _ref1 : $.fn[wp].defaults.context;
               if (!$.isWindow(contextElement)) {
                  contextElement = $this.closest(contextElement);
               }
               contextElement = $(contextElement);
               context = contexts[contextElement.data(contextKey)];
               if (!context) {
                  context = new Context(contextElement);
               }
               return new Waypoint($this, context, options);
            });
            $[wps]('refresh');
            return this;
         },
         disable:function () {
            return methods._invoke(this, 'disable');
         },
         enable:function () {
            return methods._invoke(this, 'enable');
         },
         destroy:function () {
            return methods._invoke(this, 'destroy');
         },
         prev:function (axis, selector) {
            return methods._traverse.call(this, axis, selector, function (stack, index, waypoints) {
               if (index > 0) {
                  return stack.push(waypoints[index - 1]);
               }
            });
         },
         next:function (axis, selector) {
            return methods._traverse.call(this, axis, selector, function (stack, index, waypoints) {
               if (index < waypoints.length - 1) {
                  return stack.push(waypoints[index + 1]);
               }
            });
         },
         _traverse:function (axis, selector, push) {
            var stack, waypoints;
            if (axis == null) {
               axis = 'vertical';
            }
            if (selector == null) {
               selector = window;
            }
            waypoints = jQMethods.aggregate(selector);
            stack = [];
            this.each(function () {
               var index;
               index = $.inArray(this, waypoints[axis]);
               return push(stack, index, waypoints[axis]);
            });
            return this.pushStack(stack);
         },
         _invoke:function ($elements, method) {
            $elements.each(function () {
               var waypoints;
               waypoints = Waypoint.getWaypointsByElement(this);
               return $.each(waypoints, function (i, waypoint) {
                  waypoint[method]();
                  return true;
               });
            });
            return this;
         }
      };
      $.fn[wp] = function () {
         var args, method;
         method = arguments[0], args = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
         if (methods[method]) {
            return methods[method].apply(this, args);
         } else if ($.isFunction(method)) {
            return methods.init.apply(this, arguments);
         } else if ($.isPlainObject(method)) {
            return methods.init.apply(this, [null, method]);
         } else if (!method) {
            return $.error("jQuery Waypoints needs a callback function or handler option.");
         } else {
            return $.error("The " + method + " method does not exist in jQuery Waypoints.");
         }
      };
      $.fn[wp].defaults = {
         context:window,
         continuous:true,
         enabled:true,
         horizontal:false,
         offset:0,
         triggerOnce:false
      };
      jQMethods = {
         refresh:function () {
            return $.each(contexts, function (i, context) {
               return context.refresh();
            });
         },
         viewportHeight:function () {
            var _ref;
            return (_ref = window.innerHeight) != null ? _ref : $w.height();
         },
         aggregate:function (contextSelector) {
            var collection, waypoints, _ref;
            collection = allWaypoints;
            if (contextSelector) {
               collection = (_ref = contexts[$(contextSelector).data(contextKey)]) != null ? _ref.waypoints : void 0;
            }
            if (!collection) {
               return [];
            }
            waypoints = {
               horizontal:[],
               vertical:[]
            };
            $.each(waypoints, function (axis, arr) {
               $.each(collection[axis], function (key, waypoint) {
                  return arr.push(waypoint);
               });
               arr.sort(function (a, b) {
                  return a.offset - b.offset;
               });
               waypoints[axis] = $.map(arr, function (waypoint) {
                  return waypoint.element;
               });
               return waypoints[axis] = $.unique(waypoints[axis]);
            });
            return waypoints;
         },
         above:function (contextSelector) {
            if (contextSelector == null) {
               contextSelector = window;
            }
            return jQMethods._filter(contextSelector, 'vertical', function (context, waypoint) {
               return waypoint.offset <= context.oldScroll.y;
            });
         },
         below:function (contextSelector) {
            if (contextSelector == null) {
               contextSelector = window;
            }
            return jQMethods._filter(contextSelector, 'vertical', function (context, waypoint) {
               return waypoint.offset > context.oldScroll.y;
            });
         },
         left:function (contextSelector) {
            if (contextSelector == null) {
               contextSelector = window;
            }
            return jQMethods._filter(contextSelector, 'horizontal', function (context, waypoint) {
               return waypoint.offset <= context.oldScroll.x;
            });
         },
         right:function (contextSelector) {
            if (contextSelector == null) {
               contextSelector = window;
            }
            return jQMethods._filter(contextSelector, 'horizontal', function (context, waypoint) {
               return waypoint.offset > context.oldScroll.x;
            });
         },
         enable:function () {
            return jQMethods._invoke('enable');
         },
         disable:function () {
            return jQMethods._invoke('disable');
         },
         destroy:function () {
            return jQMethods._invoke('destroy');
         },
         extendFn:function (methodName, f) {
            return methods[methodName] = f;
         },
         _invoke:function (method) {
            var waypoints;
            waypoints = $.extend({}, allWaypoints.vertical, allWaypoints.horizontal);
            return $.each(waypoints, function (key, waypoint) {
               waypoint[method]();
               return true;
            });
         },
         _filter:function (selector, axis, test) {
            var context, waypoints;
            context = contexts[$(selector).data(contextKey)];
            if (!context) {
               return [];
            }
            waypoints = [];
            $.each(context.waypoints[axis], function (i, waypoint) {
               if (test(context, waypoint)) {
                  return waypoints.push(waypoint);
               }
            });
            waypoints.sort(function (a, b) {
               return a.offset - b.offset;
            });
            return $.map(waypoints, function (waypoint) {
               return waypoint.element;
            });
         }
      };
      $[wps] = function () {
         var args, method;
         method = arguments[0], args = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
         if (jQMethods[method]) {
            return jQMethods[method].apply(null, args);
         } else {
            return jQMethods.aggregate.call(null, method);
         }
      };
      $[wps].settings = {
         resizeThrottle:100,
         scrollThrottle:30
      };

      return $w.load(function () {
         return $[wps]('refresh');
      });

   })(jQuery);

   return jQuery.fn.waypoint;
});


/* -- end module lib/jquery/plugin/jquery.waypoint -- */
/* -- start module lib/jquery/plugin/jquery.prettydate -- */
/**
 * Formattage de la date
 * du type "il y a ..."
 */
define("lib/jquery/plugin/jquery.prettydate",["jquery", "lib/date/core/iso8601"], function(jQuery, Date){
(function ($)
{
   $.prettyDate = {

      template:function (source, params) {
         if (arguments.length === 1)
         {
            return function () {
               var args = $.makeArray(arguments);
               args.unshift(source);
               return $.prettyDate.template.apply(this, args);
            };
         }
         if (arguments.length > 2 && params.constructor !== Array) {
            params = $.makeArray(arguments).slice(1);
         }
         if (params.constructor !== Array) {
            params = [ params ];
         }
         $.each(params, function (i, n) {
            source = source.replace(new RegExp("\\{" + i + "\\}", "g"), n);
         });
         return source;
      },

      // Takes an ISO time and returns a string representing how
      // long ago the date represents.
      format:function (time) {

         var date = new Date(Date.parse(time) || ""),
             diff = (new Date().getTime() - date.getTime()) / 1000,
             day_diff = Math.floor(diff / 86400);

         if (isNaN(day_diff) || day_diff <= 0)
         {
            return;
         }

         var messages = $.prettyDate.messages;

         return(diff < 60 && messages.now) ||
               (diff < 120 && messages.minute) ||
               (diff < 3600 && messages.minutes(Math.floor(diff / 60))) ||
               (diff < 7200 && messages.hour) ||
               (diff < 86400 && messages.hours(Math.floor(diff / 3600))) ||
               (day_diff === 1 && messages.yesterday) ||
               (day_diff < 7 && messages.days(day_diff)) ||
               (day_diff < 42 && messages.weeks(Math.ceil(day_diff / 7))) ||
               false;
      }

   };

   $.prettyDate.messages = {
      now:"à l'instant",
      minute:"il y a 1 minute",
      minutes:$.prettyDate.template("il y a {0} minutes"),
      hour:"il y a 1 heure",
      hours:$.prettyDate.template("il y a {0} heures"),
      yesterday:"Hier",
      days:$.prettyDate.template("il y a {0} jours"),
      weeks:$.prettyDate.template("il y a {0} semaines")
   };

   $.fn.prettyDate = function (options) {

      options = $.extend({
         value:function () {
            return $(this).data(options.data);
         },
         interval:10000,
         data:"date-iso"
      }, options);

      var elements = this;

      function format() {
         elements.each(function () {
            var date = $.prettyDate.format(options.value.apply(this));
            if (date && $(this).text() !== date)
            {
               $(this).text(date);
            }
         });
      }

      format();

      if (options.interval) {
         setInterval(format, options.interval);
      }

      return this;
   };

})(jQuery);

return jQuery.fn.prettyDate;
});
/* -- end module lib/jquery/plugin/jquery.prettydate -- */
/* -- start module lib/jquery/plugin/jquery.mousewheel -- */
/*! Copyright (c) 2010 Brandon Aaron (http://brandonaaron.net)
 * Licensed under the MIT License (LICENSE.txt).
 *
 * Thanks to: http://adomas.org/javascript-mouse-wheel/ for some pointers.
 * Thanks to: Mathias Bank(http://www.mathias-bank.de) for a scope bug fix.
 * Thanks to: Seamus Leahy for adding deltaX and deltaY
 *
 * Version: 3.0.4
 *
 * Requires: 1.2.2+
 */
define("lib/jquery/plugin/jquery.mousewheel",["jquery"], function (jQuery) {

   "use strict";

   (function ($) {

   var types = ['DOMMouseScroll', 'mousewheel'];

   $.event.special.mousewheel = {
       setup: function () {
           if ( this.addEventListener ) {
               for ( var i=types.length; i; ) {
                   this.addEventListener( types[--i], handler, false );
               }
           } else {
               this.onmousewheel = handler;
           }
       },

       teardown: function() {
           if ( this.removeEventListener ) {
               for ( var i=types.length; i; ) {
                   this.removeEventListener( types[--i], handler, false );
               }
           } else {
               this.onmousewheel = null;
           }
       }
   };

   $.fn.extend({
       mousewheel: function(fn) {
           return fn ? this.bind("mousewheel", fn) : this.trigger("mousewheel");
       },

       unmousewheel: function(fn) {
           return this.unbind("mousewheel", fn);
       }
   });


   function handler(event) {
       var orgEvent = event || window.event, args = [].slice.call( arguments, 1 ), delta = 0, returnValue = true, deltaX = 0, deltaY = 0;
       event = $.event.fix(orgEvent);
       event.type = "mousewheel";

       // Old school scrollwheel delta
       if ( event.wheelDelta ) { delta = event.wheelDelta/120; }
       if ( event.detail     ) { delta = -event.detail/3; }

       // New school multidimensional scroll (touchpads) deltas
       deltaY = delta;

       // Gecko
       if ( orgEvent.axis !== undefined && orgEvent.axis === orgEvent.HORIZONTAL_AXIS ) {
           deltaY = 0;
           deltaX = -1*delta;
       }

       // Webkit
       if ( orgEvent.wheelDeltaY !== undefined ) { deltaY = orgEvent.wheelDeltaY/120; }
       if ( orgEvent.wheelDeltaX !== undefined ) { deltaX = -1*orgEvent.wheelDeltaX/120; }

       // Add event and delta to the front of the arguments
       args.unshift(event, delta, deltaX, deltaY);

       return $.event.handle.apply(this, args);
   }

   })(jQuery);


});
/* -- end module lib/jquery/plugin/jquery.mousewheel -- */
/* -- start module lib/jquery/plugin/jquery.cookie -- */
/*!
 * jQuery Cookie Plugin
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2011, Klaus Hartl
 * Dual licensed under the MIT or GPL Version 2 licenses.
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.opensource.org/licenses/GPL-2.0
 */
define("lib/jquery/plugin/jquery.cookie",["jquery"], function(jQuery){
(function($) {
    $.cookie = function(key, value, options) {

        // key and at least value given, set cookie...
        if (arguments.length > 1 && (!/Object/.test(Object.prototype.toString.call(value)) || value === null || value === undefined)) {
            options = $.extend({}, options);

            if (value === null || value === undefined) {
                options.expires = -1;
            }

            if (typeof options.expires === 'number') {
                var days = options.expires, t = options.expires = new Date();
                t.setDate(t.getDate() + days);
            }

            value = String(value);

            return (document.cookie = [
                encodeURIComponent(key), '=', options.raw ? value : encodeURIComponent(value),
                options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
                options.path    ? '; path=' + options.path : '',
                options.domain  ? '; domain=' + options.domain : '',
                options.secure  ? '; secure' : ''
            ].join(''));
        }

        // key and possibly options given, get cookie...
        options = value || {};
        var decode = options.raw ? function(s) { return s; } : decodeURIComponent;

        var pairs = document.cookie.split('; ');
        for (var i = 0, pair; pair = pairs[i] && pairs[i].split('='); i++) {
            if (decode(pair[0]) === key) return decode(pair[1] || ''); // IE saves cookies with empty string as "c; ", e.g. without "=" as opposed to EOMB, thus pair[1] may be undefined
        }
        return null;
    };
})(jQuery);

return jQuery.cookie;

});
/* -- end module lib/jquery/plugin/jquery.cookie -- */
/* -- start module lib/jquery/plugin/jquery.spin -- */
/**
 * Plugin spin
 * permettant d'ajouter un throbber
 */
define("lib/jquery/plugin/jquery.spin",["jquery"], function(jQuery){
//fgnass.github.com/spin.js#v1.2.3
(function(a,b,c){function n(a){var b={x:a.offsetLeft,y:a.offsetTop};while(a=a.offsetParent)b.x+=a.offsetLeft,b.y+=a.offsetTop;return b}function m(a){for(var b=1;b<arguments.length;b++){var d=arguments[b];for(var e in d)a[e]===c&&(a[e]=d[e])}return a}function l(a,b){for(var c in b)a.style[k(a,c)||c]=b[c];return a}function k(a,b){var e=a.style,f,g;if(e[b]!==c)return b;b=b.charAt(0).toUpperCase()+b.slice(1);for(g=0;g<d.length;g++){f=d[g]+b;if(e[f]!==c)return f}}function j(a,b,c,d){var g=["opacity",b,~~(a*100),c,d].join("-"),h=.01+c/d*100,j=Math.max(1-(1-a)/b*(100-h),a),k=f.substring(0,f.indexOf("Animation")).toLowerCase(),l=k&&"-"+k+"-"||"";e[g]||(i.insertRule("@"+l+"keyframes "+g+"{"+"0%{opacity:"+j+"}"+h+"%{opacity:"+a+"}"+(h+.01)+"%{opacity:1}"+(h+b)%100+"%{opacity:"+a+"}"+"100%{opacity:"+j+"}"+"}",0),e[g]=1);return g}function h(a){for(var b=1,c=arguments.length;b<c;b++)a.appendChild(arguments[b]);return a}function g(a,c){var d=b.createElement(a||"div"),e;for(e in c)d[e]=c[e];return d}var d=["webkit","Moz","ms","O"],e={},f,i=function(){var a=g("style");h(b.getElementsByTagName("head")[0],a);return a.sheet||a.styleSheet}(),o=function r(a){if(!this.spin)return new r(a);this.opts=m(a||{},r.defaults,p)},p=o.defaults={lines:12,length:7,width:5,radius:10,color:"#000",speed:1,trail:100,opacity:.25,fps:20},q=o.prototype={spin:function(a){this.stop();var b=this,c=b.el=l(g(),{position:"relative"}),d,e;a&&(a.insertBefore(c,a.firstChild||null),e=n(a),d=n(c),l(c,{left:(a.offsetWidth>>1)-d.x+e.x+"px",top:(a.offsetHeight>>1)-d.y+e.y+"px"})),c.setAttribute("aria-role","progressbar"),b.lines(c,b.opts);if(!f){var h=b.opts,i=0,j=h.fps,k=j/h.speed,m=(1-h.opacity)/(k*h.trail/100),o=k/h.lines;(function p(){i++;for(var a=h.lines;a;a--){var d=Math.max(1-(i+a*o)%k*m,h.opacity);b.opacity(c,h.lines-a,d,h)}b.timeout=b.el&&setTimeout(p,~~(1e3/j))})()}return b},stop:function(){var a=this.el;a&&(clearTimeout(this.timeout),a.parentNode&&a.parentNode.removeChild(a),this.el=c);return this}};q.lines=function(a,b){function e(a,d){return l(g(),{position:"absolute",width:b.length+b.width+"px",height:b.width+"px",background:a,boxShadow:d,transformOrigin:"left",transform:"rotate("+~~(360/b.lines*c)+"deg) translate("+b.radius+"px"+",0)",borderRadius:(b.width>>1)+"px"})}var c=0,d;for(;c<b.lines;c++)d=l(g(),{position:"absolute",top:1+~(b.width/2)+"px",transform:b.hwaccel?"translate3d(0,0,0)":"",opacity:b.opacity,animation:f&&j(b.opacity,b.trail,c,b.lines)+" "+1/b.speed+"s linear infinite"}),b.shadow&&h(d,l(e("#000","0 0 4px #000"),{top:"2px"})),h(a,h(d,e(b.color,"0 0 1px rgba(0,0,0,.1)")));return a},q.opacity=function(a,b,c){b<a.childNodes.length&&(a.childNodes[b].style.opacity=c)},function(){var a=l(g("group"),{behavior:"url(#default#VML)"}),b;if(!k(a,"transform")&&a.adj){for(b=4;b--;)i.addRule(["group","roundrect","fill","stroke"][b],"behavior:url(#default#VML)");q.lines=function(a,b){function k(a,d,i){h(f,h(l(e(),{rotation:360/b.lines*a+"deg",left:~~d}),h(l(g("roundrect",{arcsize:1}),{width:c,height:b.width,left:b.radius,top:-b.width>>1,filter:i}),g("fill",{color:b.color,opacity:b.opacity}),g("stroke",{opacity:0}))))}function e(){return l(g("group",{coordsize:d+" "+d,coordorigin:-c+" "+ -c}),{width:d,height:d})}var c=b.length+b.width,d=2*c,f=e(),i=~(b.length+b.radius+b.width)+"px",j;if(b.shadow)for(j=1;j<=b.lines;j++)k(j,-2,"progid:DXImageTransform.Microsoft.Blur(pixelradius=2,makeshadow=1,shadowopacity=.3)");for(j=1;j<=b.lines;j++)k(j);return h(l(a,{margin:i+" 0 0 "+i,zoom:1}),f)},q.opacity=function(a,b,c,d){var e=a.firstChild;d=d.shadow&&d.lines||0,e&&b+d<e.childNodes.length&&(e=e.childNodes[b+d],e=e&&e.firstChild,e=e&&e.firstChild,e&&(e.opacity=c))}}else f=k(a,"animation")}(),a.Spinner=o})(window,document);

(
function ($) {
  $.fn.spin = function (options) {
     var width, height, left, top;

     return this.each(function () {
        var spinBlock = $('<div></div>'),
            hgt = $(this).height(),
            hgt_ok = (parseInt(hgt) > 40) ? hgt : 40;
        spinBlock.removeAttr("id");
        spinBlock.removeAttr("class");
        spinBlock.height(hgt_ok);
        spinBlock.width($(this).width());
        spinBlock.addClass("spin-block");
        spinBlock.css('padding-top', $(this).css('padding-top'));
        spinBlock.css('padding-right', $(this).css('padding-right'));
        spinBlock.css('padding-bottom', $(this).css('padding-bottom'));
        spinBlock.css('padding-left', $(this).css('padding-left'));
        spinBlock.css('margin-top', $(this).css('margin-top'));
        spinBlock.css('margin-right', $(this).css('margin-right'));
        spinBlock.css('margin-bottom', $(this).css('margin-bottom'));
        spinBlock.css('margin-left', $(this).css('margin-left'));

        $(this).hide();

        var spRadius = 10,
            spWidth = 4,
            spLength = 7,
            spLines = 14,
            spSpeed = 1.9,
            spColor = '#464F57';

        if (options) {
           if (typeof options.height != "undefined") {
              spinBlock.height(options.height)
           }

           if (typeof options.width != "undefined") {
              spinBlock.css('width', options.width);
           }

           if (typeof options.spRadius != "undefined") {
              spRadius = options.spRadius;
           }

           if (typeof options.spWidth != "undefined") {
              spWidth = options.spWidth;
           }

           if (typeof options.spLength != "undefined") {
              spLength = options.spLength;
           }

           if (typeof options.spLines != "undefined") {
              spLines = options.spLines;
           }

           if (typeof options.spSpeed != "undefined") {
              spSpeed = options.spSpeed;
           }

           if (typeof options.spColor != "undefined") {
              spColor = options.spColor;
           }
        }

        //spinBlock.css("background", "#ccc");

        var data = $(this).data();

        if (typeof data === "undefined" || data === null || !data) {
           return false;
        }

        data.spinBlock = spinBlock;

        var spinnerOpts = {
              lines: spLines, // The number of lines to draw
              length: spLength, // The length of each line
              width: spWidth, // The line thickness
              radius: spRadius, // The radius of the inner circle
              color: spColor, // #rgb or #rrggbb
              speed: spSpeed, // Rounds per second
              trail: 60, // Afterglow percentage
              shadow: false, // Whether to render a shadow
              hwaccel: false // Whether to use hardware acceleration
            };

        data.spinner = new Spinner(spinnerOpts).spin(spinBlock.get(0));
        data.$spinner = $(data.spinner.el);

        $(data.spinner.el).css("left", spinBlock.width() / 2);
        $(data.spinner.el).css("top", spinBlock.height() / 2);

        $(this).after(spinBlock);
     });
  };

  $.fn.unspin = function () {
     return this.each(function () {
        var data = $(this).data();

        if (typeof data.spinBlock != "undefined" &&
            typeof data.spinBlock.processed === "undefined") {
           data.spinBlock.hide();
           $(this).fadeIn();
           data.spinBlock.processed = true;
        }
     });
  };
}(jQuery));

return jQuery.fn.unspin;
});
/* -- end module lib/jquery/plugin/jquery.spin -- */
/* -- start module lib/jquery/plugin/jquery.ajah -- */
/**
 * Todo (lorsque cela sera necessaire):
 * Actuellement, il est possible de lancer une callback apres le chargement de l'ajah:
 * $("body").ajah({url: "lemonde.fr"}).done(function () { console.log("Ajah charge!");});
 * Sauf si on joue l'ajah sur un groupe d'elements:
 * $("div").ajah(...).done(); ne marchera pas.
 */
define("lib/jquery/plugin/jquery.ajah",["jquery"], function(jQuery){
(function ($) {

   var ajah = function (node, opts) {
      var defaults = { 'cached' : true },
          options = $.extend(defaults, opts);

      // hacky plugin, to force CDN cache
      var ajahXhr = $.ajax({
                              url : options.url,
                              cache : options.cached,
                              success : function (html) {
                                 $(node).replaceWith(html);
                              }
                           });
      return ajahXhr;
   };

   $.fn.ajah = function (opts) {
      var i, cnt;
      if ((cnt = this.length) > 1) {
         for (i = 0; i < cnt; i = i + 1) {
            return ajah(this, opts);
         }
      } else {
         return ajah(this, opts);
      }
   };

   return $.fn.ajah;

})(jQuery);

return jQuery.fn.ajah;

});
/* -- end module lib/jquery/plugin/jquery.ajah -- */
/* -- start module lib/jquery/plugin/jquery.lazyload -- */
/*
 * Lazy Load - jQuery plugin for lazy loading images
 *
 * Copyright (c) 2007-2012 Mika Tuupola
 *
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 *
 * Project home:
 *   http://www.appelsiini.net/projects/lazyload
 *
 * Version:  1.7.0
 *
 */
define("lib/jquery/plugin/jquery.lazyload",["jquery"], function(jQuery){
(function($, window) {

    var $window = $(window);

    $.fn.lazyload = function(options) {
        var settings = {
            threshold       : 0,
            failure_limit   : 0,
            event           : "scroll",
            effect          : "show",
            container       : window,
            data_attribute  : "original",
            skip_invisible  : true,
            appear          : null,
            load            : null
        };

        if(options) {
            /* Maintain BC for a couple of version. */
            if (undefined !== options.failurelimit) {
                options.failure_limit = options.failurelimit;
                delete options.failurelimit;
            }
            if (undefined !== options.effectspeed) {
                options.effect_speed = options.effectspeed;
                delete options.effectspeed;
            }
            $.extend(settings, options);
        }

        /* Fire one scroll event per scroll. Not one scroll event per image. */
        var elements = this;
        if (0 == settings.event.indexOf("scroll")) {
            $(settings.container).bind(settings.event, function(event) {
                var counter = 0;
                elements.each(function() {
                    $this = $(this);
                    if (settings.skip_invisible && !$this.is(":visible")) return;
                    if ($.abovethetop(this, settings) ||
                        $.leftofbegin(this, settings)) {
                            /* Nothing. */
                    } else if (!$.belowthefold(this, settings) &&
                        !$.rightoffold(this, settings)) {
                            $this.trigger("appear");
                    } else {
                        if (++counter > settings.failure_limit) {
                            return false;
                        }
                    }
                });
            });
        }

        this.each(function() {
            var self = this;
            var $self = $(self);

            self.loaded = false;

            /* When appear is triggered load original image. */
            $self.one("appear", function() {
                if (!this.loaded) {
                    if (settings.appear) {
                        var elements_left = elements.length;
                        settings.appear.call(self, elements_left, settings);
                    }
                    $("<img />")
                        .bind("load", function() {
                            $self
                                .hide()
                                .attr("src", $self.data(settings.data_attribute))
                                [settings.effect](settings.effect_speed);
                            self.loaded = true;

                            /* Remove image from array so it is not looped next time. */
                            var temp = $.grep(elements, function(element) {
                                return !element.loaded;
                            });
                            elements = $(temp);

                            if (settings.load) {
                                var elements_left = elements.length;
                                settings.load.call(self, elements_left, settings);
                            }
                        })
                        .attr("src", $self.data(settings.data_attribute));
                };
            });

            /* When wanted event is triggered load original image */
            /* by triggering appear.                              */
            if (0 != settings.event.indexOf("scroll")) {
                $self.bind(settings.event, function(event) {
                    if (!self.loaded) {
                        $self.trigger("appear");
                    }
                });
            }
        });

        /* Check if something appears when window is resized. */
        $window.bind("resize", function(event) {
            $(settings.container).trigger(settings.event);
        });

        /* Force initial check if images should appear. */
        $(settings.container).trigger(settings.event);

        return this;

    };

    /* Convenience methods in jQuery namespace.           */
    /* Use as  $.belowthefold(element, {threshold : 100, container : window}) */

    $.belowthefold = function(element, settings) {
        if (settings.container === undefined || settings.container === window) {
            var fold = $window.height() + $window.scrollTop();
        } else {
            var fold = $(settings.container).offset().top + $(settings.container).height();
        }
        return fold <= $(element).offset().top - settings.threshold;
    };

    $.rightoffold = function(element, settings) {
        if (settings.container === undefined || settings.container === window) {
            var fold = $window.width() + $window.scrollLeft();
        } else {
            var fold = $(settings.container).offset().left + $(settings.container).width();
        }
        return fold <= $(element).offset().left - settings.threshold;
    };

    $.abovethetop = function(element, settings) {
        if (settings.container === undefined || settings.container === window) {
            var fold = $window.scrollTop();
        } else {
            var fold = $(settings.container).offset().top;
        }
        return fold >= $(element).offset().top + settings.threshold  + $(element).height();
    };

    $.leftofbegin = function(element, settings) {
        if (settings.container === undefined || settings.container === window) {
            var fold = $window.scrollLeft();
        } else {
            var fold = $(settings.container).offset().left;
        }
        return fold >= $(element).offset().left + settings.threshold + $(element).width();
    };

    $.inviewport = function(element, settings) {
         return !$.rightofscreen(element, settings) && !$.leftofscreen(element, settings) &&
                !$.belowthefold(element, settings) && !$.abovethetop(element, settings);
     };

    /* Custom selectors for your convenience.   */
    /* Use as $("img:below-the-fold").something() */

    $.extend($.expr[':'], {
        "below-the-fold" : function(a) { return $.belowthefold(a, {threshold : 0, container: window}) },
        "above-the-top"  : function(a) { return !$.belowthefold(a, {threshold : 0, container: window}) },
        "right-of-screen": function(a) { return $.rightoffold(a, {threshold : 0, container: window}) },
        "left-of-screen" : function(a) { return !$.rightoffold(a, {threshold : 0, container: window}) },
        "in-viewport"    : function(a) { return !$.inviewport(a, {threshold : 0, container: window}) },
        /* Maintain BC for couple of versions. */
        "above-the-fold" : function(a) { return !$.belowthefold(a, {threshold : 0, container: window}) },
        "right-of-fold"  : function(a) { return $.rightoffold(a, {threshold : 0, container: window}) },
        "left-of-fold"   : function(a) { return !$.rightoffold(a, {threshold : 0, container: window}) }
    });

})(jQuery, window);
});
/* -- end module lib/jquery/plugin/jquery.lazyload -- */
/* -- start module hogan -- */
/*
 *  Copyright 2011 Twitter, Inc.
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */



var Hogan = {};

(function (Hogan, useArrayBuffer) {
  Hogan.Template = function (renderFunc, text, compiler, options) {
    this.r = renderFunc || this.r;
    this.c = compiler;
    this.options = options;
    this.text = text || '';
    this.buf = (useArrayBuffer) ? [] : '';
  }

  Hogan.Template.prototype = {
    // render: replaced by generated code.
    r: function (context, partials, indent) { return ''; },

    // variable escaping
    v: hoganEscape,

    // triple stache
    t: coerceToString,

    render: function render(context, partials, indent) {
      return this.ri([context], partials || {}, indent);
    },

    // render internal -- a hook for overrides that catches partials too
    ri: function (context, partials, indent) {
      return this.r(context, partials, indent);
    },

    // tries to find a partial in the curent scope and render it
    rp: function(name, context, partials, indent) {
      var partial = partials[name];

      if (!partial) {
        return '';
      }

      if (this.c && typeof partial == 'string') {
        partial = this.c.compile(partial, this.options);
      }

      return partial.ri(context, partials, indent);
    },

    // render a section
    rs: function(context, partials, section) {
      var tail = context[context.length - 1];

      if (!isArray(tail)) {
        section(context, partials, this);
        return;
      }

      for (var i = 0; i < tail.length; i++) {
        context.push(tail[i]);
        section(context, partials, this);
        context.pop();
      }
    },

    // maybe start a section
    s: function(val, ctx, partials, inverted, start, end, tags) {
      var pass;

      if (isArray(val) && val.length === 0) {
        return false;
      }

      if (typeof val == 'function') {
        val = this.ls(val, ctx, partials, inverted, start, end, tags);
      }

      pass = (val === '') || !!val;

      if (!inverted && pass && ctx) {
        ctx.push((typeof val == 'object') ? val : ctx[ctx.length - 1]);
      }

      return pass;
    },

    // find values with dotted names
    d: function(key, ctx, partials, returnFound) {
      var names = key.split('.'),
          val = this.f(names[0], ctx, partials, returnFound),
          cx = null;

      if (key === '.' && isArray(ctx[ctx.length - 2])) {
        return ctx[ctx.length - 1];
      }

      for (var i = 1; i < names.length; i++) {
        if (val && typeof val == 'object' && names[i] in val) {
          cx = val;
          val = val[names[i]];
        } else {
          val = '';
        }
      }

      if (returnFound && !val) {
        return false;
      }

      if (!returnFound && typeof val == 'function') {
        ctx.push(cx);
        val = this.lv(val, ctx, partials);
        ctx.pop();
      }

      return val;
    },

    // find values with normal names
    f: function(key, ctx, partials, returnFound) {
      var val = false,
          v = null,
          found = false;

      for (var i = ctx.length - 1; i >= 0; i--) {
        v = ctx[i];
        if (v && typeof v == 'object' && key in v) {
          val = v[key];
          found = true;
          break;
        }
      }

      if (!found) {
        return (returnFound) ? false : "";
      }

      if (!returnFound && typeof val == 'function') {
        val = this.lv(val, ctx, partials);
      }

      return val;
    },

    // higher order templates
    ho: function(val, cx, partials, text, tags) {
      var compiler = this.c;
      var options = this.options;
      options.delimiters = tags;
      var t = val.call(cx, text, function(t) {
        return compiler.compile(t, options).render(cx, partials);
      });
      this.b(compiler.compile(t.toString(), options).render(cx, partials));
      return false;
    },

    // template result buffering
    b: (useArrayBuffer) ? function(s) { this.buf.push(s); } :
                          function(s) { this.buf += s; },
    fl: (useArrayBuffer) ? function() { var r = this.buf.join(''); this.buf = []; return r; } :
                           function() { var r = this.buf; this.buf = ''; return r; },

    // lambda replace section
    ls: function(val, ctx, partials, inverted, start, end, tags) {
      var cx = ctx[ctx.length - 1],
          t = null;

      if (!inverted && this.c && val.length > 0) {
        return this.ho(val, cx, partials, this.text.substring(start, end), tags);
      }

      t = val.call(cx);

      if (typeof t == 'function') {
        if (inverted) {
          return true;
        } else if (this.c) {
          return this.ho(t, cx, partials, this.text.substring(start, end), tags);
        }
      }

      return t;
    },

    // lambda replace variable
    lv: function(val, ctx, partials) {
      var cx = ctx[ctx.length - 1];
      var result = val.call(cx);
      if (typeof result == 'function') {
        result = result.call(cx);
      }
      result = coerceToString(result);

      if (this.c && ~result.indexOf("{\u007B")) {
        return this.c.compile(result, this.options).render(cx, partials);
      }

      return result;
    }

  };

  var rAmp = /&/g,
      rLt = /</g,
      rGt = />/g,
      rApos =/\'/g,
      rQuot = /\"/g,
      hChars =/[&<>\"\']/;


  function coerceToString(val) {
    return String((val === null || val === undefined) ? '' : val);
  }

  function hoganEscape(str) {
    str = coerceToString(str);
    return hChars.test(str) ?
      str
        .replace(rAmp,'&amp;')
        .replace(rLt,'&lt;')
        .replace(rGt,'&gt;')
        .replace(rApos,'&#39;')
        .replace(rQuot, '&quot;') :
      str;
  }

  var isArray = Array.isArray || function(a) {
    return Object.prototype.toString.call(a) === '[object Array]';
  };

})(typeof exports !== 'undefined' ? exports : Hogan);




(function (Hogan) {
  // Setup regex  assignments
  // remove whitespace according to Mustache spec
  var rIsWhitespace = /\S/,
      rQuot = /\"/g,
      rNewline =  /\n/g,
      rCr = /\r/g,
      rSlash = /\\/g,
      tagTypes = {
        '#': 1, '^': 2, '/': 3,  '!': 4, '>': 5,
        '<': 6, '=': 7, '_v': 8, '{': 9, '&': 10
      };

  Hogan.scan = function scan(text, delimiters) {
    var len = text.length,
        IN_TEXT = 0,
        IN_TAG_TYPE = 1,
        IN_TAG = 2,
        state = IN_TEXT,
        tagType = null,
        tag = null,
        buf = '',
        tokens = [],
        seenTag = false,
        i = 0,
        lineStart = 0,
        otag = '{{',
        ctag = '}}';

    function addBuf() {
      if (buf.length > 0) {
        tokens.push(new String(buf));
        buf = '';
      }
    }

    function lineIsWhitespace() {
      var isAllWhitespace = true;
      for (var j = lineStart; j < tokens.length; j++) {
        isAllWhitespace =
          (tokens[j].tag && tagTypes[tokens[j].tag] < tagTypes['_v']) ||
          (!tokens[j].tag && tokens[j].match(rIsWhitespace) === null);
        if (!isAllWhitespace) {
          return false;
        }
      }

      return isAllWhitespace;
    }

    function filterLine(haveSeenTag, noNewLine) {
      addBuf();

      if (haveSeenTag && lineIsWhitespace()) {
        for (var j = lineStart, next; j < tokens.length; j++) {
          if (!tokens[j].tag) {
            if ((next = tokens[j+1]) && next.tag == '>') {
              // set indent to token value
              next.indent = tokens[j].toString()
            }
            tokens.splice(j, 1);
          }
        }
      } else if (!noNewLine) {
        tokens.push({tag:'\n'});
      }

      seenTag = false;
      lineStart = tokens.length;
    }

    function changeDelimiters(text, index) {
      var close = '=' + ctag,
          closeIndex = text.indexOf(close, index),
          delimiters = trim(
            text.substring(text.indexOf('=', index) + 1, closeIndex)
          ).split(' ');

      otag = delimiters[0];
      ctag = delimiters[1];

      return closeIndex + close.length - 1;
    }

    if (delimiters) {
      delimiters = delimiters.split(' ');
      otag = delimiters[0];
      ctag = delimiters[1];
    }

    for (i = 0; i < len; i++) {
      if (state == IN_TEXT) {
        if (tagChange(otag, text, i)) {
          --i;
          addBuf();
          state = IN_TAG_TYPE;
        } else {
          if (text.charAt(i) == '\n') {
            filterLine(seenTag);
          } else {
            buf += text.charAt(i);
          }
        }
      } else if (state == IN_TAG_TYPE) {
        i += otag.length - 1;
        tag = tagTypes[text.charAt(i + 1)];
        tagType = tag ? text.charAt(i + 1) : '_v';
        if (tagType == '=') {
          i = changeDelimiters(text, i);
          state = IN_TEXT;
        } else {
          if (tag) {
            i++;
          }
          state = IN_TAG;
        }
        seenTag = i;
      } else {
        if (tagChange(ctag, text, i)) {
          tokens.push({tag: tagType, n: trim(buf), otag: otag, ctag: ctag,
                       i: (tagType == '/') ? seenTag - ctag.length : i + otag.length});
          buf = '';
          i += ctag.length - 1;
          state = IN_TEXT;
          if (tagType == '{') {
            if (ctag == '}}') {
              i++;
            } else {
              cleanTripleStache(tokens[tokens.length - 1]);
            }
          }
        } else {
          buf += text.charAt(i);
        }
      }
    }

    filterLine(seenTag, true);

    return tokens;
  }

  function cleanTripleStache(token) {
    if (token.n.substr(token.n.length - 1) === '}') {
      token.n = token.n.substring(0, token.n.length - 1);
    }
  }

  function trim(s) {
    if (s.trim) {
      return s.trim();
    }

    return s.replace(/^\s*|\s*$/g, '');
  }

  function tagChange(tag, text, index) {
    if (text.charAt(index) != tag.charAt(0)) {
      return false;
    }

    for (var i = 1, l = tag.length; i < l; i++) {
      if (text.charAt(index + i) != tag.charAt(i)) {
        return false;
      }
    }

    return true;
  }

  function buildTree(tokens, kind, stack, customTags) {
    var instructions = [],
        opener = null,
        token = null;

    while (tokens.length > 0) {
      token = tokens.shift();
      if (token.tag == '#' || token.tag == '^' || isOpener(token, customTags)) {
        stack.push(token);
        token.nodes = buildTree(tokens, token.tag, stack, customTags);
        instructions.push(token);
      } else if (token.tag == '/') {
        if (stack.length === 0) {
          throw new Error('Closing tag without opener: /' + token.n);
        }
        opener = stack.pop();
        if (token.n != opener.n && !isCloser(token.n, opener.n, customTags)) {
          throw new Error('Nesting error: ' + opener.n + ' vs. ' + token.n);
        }
        opener.end = token.i;
        return instructions;
      } else {
        instructions.push(token);
      }
    }

    if (stack.length > 0) {
      throw new Error('missing closing tag: ' + stack.pop().n);
    }

    return instructions;
  }

  function isOpener(token, tags) {
    for (var i = 0, l = tags.length; i < l; i++) {
      if (tags[i].o == token.n) {
        token.tag = '#';
        return true;
      }
    }
  }

  function isCloser(close, open, tags) {
    for (var i = 0, l = tags.length; i < l; i++) {
      if (tags[i].c == close && tags[i].o == open) {
        return true;
      }
    }
  }

  function writeCode(tree) {
    return 'var _=this;_.b(i=i||"");' + walk(tree) + 'return _.fl();';
  }

  Hogan.generate = function (code, text, options) {
    if (options.asString) {
      return 'function(c,p,i){' + code + ';}';
    }

    return new Hogan.Template(new Function('c', 'p', 'i', code), text, Hogan, options);
  }

  function esc(s) {
    return s.replace(rSlash, '\\\\')
            .replace(rQuot, '\\\"')
            .replace(rNewline, '\\n')
            .replace(rCr, '\\r');
  }

  function chooseMethod(s) {
    return (~s.indexOf('.')) ? 'd' : 'f';
  }

  function walk(tree) {
    var code = '';
    for (var i = 0, l = tree.length; i < l; i++) {
      var tag = tree[i].tag;
      if (tag == '#') {
        code += section(tree[i].nodes, tree[i].n, chooseMethod(tree[i].n),
                        tree[i].i, tree[i].end, tree[i].otag + " " + tree[i].ctag);
      } else if (tag == '^') {
        code += invertedSection(tree[i].nodes, tree[i].n,
                                chooseMethod(tree[i].n));
      } else if (tag == '<' || tag == '>') {
        code += partial(tree[i]);
      } else if (tag == '{' || tag == '&') {
        code += tripleStache(tree[i].n, chooseMethod(tree[i].n));
      } else if (tag == '\n') {
        code += text('"\\n"' + (tree.length-1 == i ? '' : ' + i'));
      } else if (tag == '_v') {
        code += variable(tree[i].n, chooseMethod(tree[i].n));
      } else if (tag === undefined) {
        code += text('"' + esc(tree[i]) + '"');
      }
    }
    return code;
  }

  function section(nodes, id, method, start, end, tags) {
    return 'if(_.s(_.' + method + '("' + esc(id) + '",c,p,1),' +
           'c,p,0,' + start + ',' + end + ',"' + tags + '")){' +
           '_.rs(c,p,' +
           'function(c,p,_){' +
           walk(nodes) +
           '});c.pop();}';
  }

  function invertedSection(nodes, id, method) {
    return 'if(!_.s(_.' + method + '("' + esc(id) + '",c,p,1),c,p,1,0,0,"")){' +
           walk(nodes) +
           '};';
  }

  function partial(tok) {
    return '_.b(_.rp("' +  esc(tok.n) + '",c,p,"' + (tok.indent || '') + '"));';
  }

  function tripleStache(id, method) {
    return '_.b(_.t(_.' + method + '("' + esc(id) + '",c,p,0)));';
  }

  function variable(id, method) {
    return '_.b(_.v(_.' + method + '("' + esc(id) + '",c,p,0)));';
  }

  function text(id) {
    return '_.b(' + id + ');';
  }

  Hogan.parse = function(tokens, text, options) {
    options = options || {};
    return buildTree(tokens, '', [], options.sectionTags || []);
  },

  Hogan.cache = {};

  Hogan.compile = function(text, options) {
    // options
    //
    // asString: false (default)
    //
    // sectionTags: [{o: '_foo', c: 'foo'}]
    // An array of object with o and c fields that indicate names for custom
    // section tags. The example above allows parsing of {{_foo}}{{/foo}}.
    //
    // delimiters: A string that overrides the default delimiters.
    // Example: "<% %>"
    //
    options = options || {};

    var key = text + '||' + !!options.asString;

    var t = this.cache[key];

    if (t) {
      return t;
    }

    t = this.generate(writeCode(this.parse(this.scan(text, options.delimiters), text, options)), text, options);
    return this.cache[key] = t;
  };
})(typeof exports !== 'undefined' ? exports : Hogan);

define("hogan",Hogan);

/* -- end module hogan -- */
/* -- start module lib/crypto/core/md5 -- */
(function(a){function b(a,b){var c=(a&65535)+(b&65535),d=(a>>16)+(b>>16)+(c>>16);return d<<16|c&65535}function c(a,b){return a<<b|a>>>32-b}function d(a,d,e,f,g,h){return b(c(b(b(d,a),b(f,h)),g),e)}function e(a,b,c,e,f,g,h){return d(b&c|~b&e,a,b,f,g,h)}function f(a,b,c,e,f,g,h){return d(b&e|c&~e,a,b,f,g,h)}function g(a,b,c,e,f,g,h){return d(b^c^e,a,b,f,g,h)}function h(a,b,c,e,f,g,h){return d(c^(b|~e),a,b,f,g,h)}function i(a,c){a[c>>5]|=128<<c%32,a[(c+64>>>9<<4)+14]=c;var d,i,j,k,l,m=1732584193,n=-271733879,o=-1732584194,p=271733878;for(d=0;d<a.length;d+=16)i=m,j=n,k=o,l=p,m=e(m,n,o,p,a[d],7,-680876936),p=e(p,m,n,o,a[d+1],12,-389564586),o=e(o,p,m,n,a[d+2],17,606105819),n=e(n,o,p,m,a[d+3],22,-1044525330),m=e(m,n,o,p,a[d+4],7,-176418897),p=e(p,m,n,o,a[d+5],12,1200080426),o=e(o,p,m,n,a[d+6],17,-1473231341),n=e(n,o,p,m,a[d+7],22,-45705983),m=e(m,n,o,p,a[d+8],7,1770035416),p=e(p,m,n,o,a[d+9],12,-1958414417),o=e(o,p,m,n,a[d+10],17,-42063),n=e(n,o,p,m,a[d+11],22,-1990404162),m=e(m,n,o,p,a[d+12],7,1804603682),p=e(p,m,n,o,a[d+13],12,-40341101),o=e(o,p,m,n,a[d+14],17,-1502002290),n=e(n,o,p,m,a[d+15],22,1236535329),m=f(m,n,o,p,a[d+1],5,-165796510),p=f(p,m,n,o,a[d+6],9,-1069501632),o=f(o,p,m,n,a[d+11],14,643717713),n=f(n,o,p,m,a[d],20,-373897302),m=f(m,n,o,p,a[d+5],5,-701558691),p=f(p,m,n,o,a[d+10],9,38016083),o=f(o,p,m,n,a[d+15],14,-660478335),n=f(n,o,p,m,a[d+4],20,-405537848),m=f(m,n,o,p,a[d+9],5,568446438),p=f(p,m,n,o,a[d+14],9,-1019803690),o=f(o,p,m,n,a[d+3],14,-187363961),n=f(n,o,p,m,a[d+8],20,1163531501),m=f(m,n,o,p,a[d+13],5,-1444681467),p=f(p,m,n,o,a[d+2],9,-51403784),o=f(o,p,m,n,a[d+7],14,1735328473),n=f(n,o,p,m,a[d+12],20,-1926607734),m=g(m,n,o,p,a[d+5],4,-378558),p=g(p,m,n,o,a[d+8],11,-2022574463),o=g(o,p,m,n,a[d+11],16,1839030562),n=g(n,o,p,m,a[d+14],23,-35309556),m=g(m,n,o,p,a[d+1],4,-1530992060),p=g(p,m,n,o,a[d+4],11,1272893353),o=g(o,p,m,n,a[d+7],16,-155497632),n=g(n,o,p,m,a[d+10],23,-1094730640),m=g(m,n,o,p,a[d+13],4,681279174),p=g(p,m,n,o,a[d],11,-358537222),o=g(o,p,m,n,a[d+3],16,-722521979),n=g(n,o,p,m,a[d+6],23,76029189),m=g(m,n,o,p,a[d+9],4,-640364487),p=g(p,m,n,o,a[d+12],11,-421815835),o=g(o,p,m,n,a[d+15],16,530742520),n=g(n,o,p,m,a[d+2],23,-995338651),m=h(m,n,o,p,a[d],6,-198630844),p=h(p,m,n,o,a[d+7],10,1126891415),o=h(o,p,m,n,a[d+14],15,-1416354905),n=h(n,o,p,m,a[d+5],21,-57434055),m=h(m,n,o,p,a[d+12],6,1700485571),p=h(p,m,n,o,a[d+3],10,-1894986606),o=h(o,p,m,n,a[d+10],15,-1051523),n=h(n,o,p,m,a[d+1],21,-2054922799),m=h(m,n,o,p,a[d+8],6,1873313359),p=h(p,m,n,o,a[d+15],10,-30611744),o=h(o,p,m,n,a[d+6],15,-1560198380),n=h(n,o,p,m,a[d+13],21,1309151649),m=h(m,n,o,p,a[d+4],6,-145523070),p=h(p,m,n,o,a[d+11],10,-1120210379),o=h(o,p,m,n,a[d+2],15,718787259),n=h(n,o,p,m,a[d+9],21,-343485551),m=b(m,i),n=b(n,j),o=b(o,k),p=b(p,l);return[m,n,o,p]}function j(a){var b,c="";for(b=0;b<a.length*32;b+=8)c+=String.fromCharCode(a[b>>5]>>>b%32&255);return c}function k(a){var b,c=[];c[(a.length>>2)-1]=undefined;for(b=0;b<c.length;b+=1)c[b]=0;for(b=0;b<a.length*8;b+=8)c[b>>5]|=(a.charCodeAt(b/8)&255)<<b%32;return c}function l(a){return j(i(k(a),a.length*8))}function m(a,b){var c,d=k(a),e=[],f=[],g;e[15]=f[15]=undefined,d.length>16&&(d=i(d,a.length*8));for(c=0;c<16;c+=1)e[c]=d[c]^909522486,f[c]=d[c]^1549556828;return g=i(e.concat(k(b)),512+b.length*8),j(i(f.concat(g),640))}function n(a){var b="0123456789abcdef",c="",d,e;for(e=0;e<a.length;e+=1)d=a.charCodeAt(e),c+=b.charAt(d>>>4&15)+b.charAt(d&15);return c}function o(a){return unescape(encodeURIComponent(a))}function p(a){return l(o(a))}function q(a){return n(p(a))}function r(a,b){return m(o(a),o(b))}function s(a,b){return n(r(a,b))}function t(a,b,c){return b?c?r(b,a):s(b,a):c?p(a):q(a)}"use strict",typeof define=="function"&&define.amd?define("lib/crypto/core/md5",function(){return t}):a.md5=t})(this);
/* -- end module lib/crypto/core/md5 -- */
/* -- start module lib/object-path -- */
(function (root, factory){
    'use strict';

    /*istanbul ignore next:cant test*/
    if (typeof module === 'object' && typeof module.exports === 'object') {
        module.exports = factory();
    } else if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define("lib/object-path",[], factory);
    } else {
        // Browser globals
        root.objectPath = factory();
    }
})(this, function(){
    'use strict';

    var
        toStr = Object.prototype.toString,
        _hasOwnProperty = Object.prototype.hasOwnProperty;

    function isEmpty(value){
        if (!value) {
            return true;
        }
        if (isArray(value) && value.length === 0) {
            return true;
        } else if (!isString(value)) {
            for (var i in value) {
                if (_hasOwnProperty.call(value, i)) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }

    function toString(type){
        return toStr.call(type);
    }

    function isNumber(value){
        return typeof value === 'number' || toString(value) === "[object Number]";
    }

    function isString(obj){
        return typeof obj === 'string' || toString(obj) === "[object String]";
    }

    function isObject(obj){
        return typeof obj === 'object' && toString(obj) === "[object Object]";
    }

    function isArray(obj){
        return typeof obj === 'object' && typeof obj.length === 'number' && toString(obj) === '[object Array]';
    }

    function isBoolean(obj){
        return typeof obj === 'boolean' || toString(obj) === '[object Boolean]';
    }

    function getKey(key){
        var intKey = parseInt(key);
        if (intKey.toString() === key) {
            return intKey;
        }
        return key;
    }

    function set(obj, path, value, doNotReplace){
        if (isNumber(path)) {
            path = [path];
        }
        if (isEmpty(path)) {
            return obj;
        }
        if (isString(path)) {
            return set(obj, path.split('.').map(getKey), value, doNotReplace);
        }
        var currentPath = path[0];

        if (path.length === 1) {
            var oldVal = obj[currentPath];
            if (oldVal === void 0 || !doNotReplace) {
                obj[currentPath] = value;
            }
            return oldVal;
        }

        if (obj[currentPath] === void 0) {
            //check if we assume an array
            if(isNumber(path[1])) {
                obj[currentPath] = [];
            } else {
                obj[currentPath] = {};
            }
        }

        return set(obj[currentPath], path.slice(1), value, doNotReplace);
    }

    function del(obj, path) {
        if (isNumber(path)) {
            path = [path];
        }

        if (isEmpty(obj)) {
            return void 0;
        }

        if (isEmpty(path)) {
            return obj;
        }
        if(isString(path)) {
            return del(obj, path.split('.'));
        }

        var currentPath = getKey(path[0]);
        var oldVal = obj[currentPath];

        if(path.length === 1) {
            if (oldVal !== void 0) {
                if (isArray(obj)) {
                    obj.splice(currentPath, 1);
                } else {
                    delete obj[currentPath];
                }
            }
        } else {
            if (obj[currentPath] !== void 0) {
                return del(obj[currentPath], path.slice(1));
            }
        }

        return obj;
    }

    var objectPath = function(obj) {
        return Object.keys(objectPath).reduce(function(proxy, prop) {
            if (typeof objectPath[prop] === 'function') {
                proxy[prop] = objectPath[prop].bind(objectPath, obj);
            }

            return proxy;
        }, {});
    };

    objectPath.has = function (obj, path) {
        if (isEmpty(obj)) {
            return false;
        }

        if (isNumber(path)) {
            path = [path];
        } else if (isString(path)) {
            path = path.split('.');
        }

        if (isEmpty(path) || path.length === 0) {
            return false;
        }

        for (var i = 0; i < path.length; i++) {
            var j = path[i];
            if ((isObject(obj) || isArray(obj)) && _hasOwnProperty.call(obj, j)) {
                obj = obj[j];
            } else {
                return false;
            }
        }

        return true;
    };

    objectPath.ensureExists = function (obj, path, value){
        return set(obj, path, value, true);
    };

    objectPath.set = function (obj, path, value, doNotReplace){
        return set(obj, path, value, doNotReplace);
    };

    objectPath.insert = function (obj, path, value, at){
        var arr = objectPath.get(obj, path);
        at = ~~at;
        if (!isArray(arr)) {
            arr = [];
            objectPath.set(obj, path, arr);
        }
        arr.splice(at, 0, value);
    };

    objectPath.empty = function(obj, path) {
        if (isEmpty(path)) {
            return obj;
        }
        if (isEmpty(obj)) {
            return void 0;
        }

        var value, i;
        if (!(value = objectPath.get(obj, path))) {
            return obj;
        }

        if (isString(value)) {
            return objectPath.set(obj, path, '');
        } else if (isBoolean(value)) {
            return objectPath.set(obj, path, false);
        } else if (isNumber(value)) {
            return objectPath.set(obj, path, 0);
        } else if (isArray(value)) {
            value.length = 0;
        } else if (isObject(value)) {
            for (i in value) {
                if (_hasOwnProperty.call(value, i)) {
                    delete value[i];
                }
            }
        } else {
            return objectPath.set(obj, path, null);
        }
    };

    objectPath.push = function (obj, path /*, values */){
        var arr = objectPath.get(obj, path);
        if (!isArray(arr)) {
            arr = [];
            objectPath.set(obj, path, arr);
        }

        arr.push.apply(arr, Array.prototype.slice.call(arguments, 2));
    };

    objectPath.coalesce = function (obj, paths, defaultValue) {
        var value;

        for (var i = 0, len = paths.length; i < len; i++) {
            if ((value = objectPath.get(obj, paths[i])) !== void 0) {
                return value;
            }
        }

        return defaultValue;
    };

    objectPath.get = function (obj, path, defaultValue){
        if (isNumber(path)) {
            path = [path];
        }
        if (isEmpty(path)) {
            return obj;
        }
        if (isEmpty(obj)) {
            return defaultValue;
        }
        if (isString(path)) {
            return objectPath.get(obj, path.split('.'), defaultValue);
        }

        var currentPath = getKey(path[0]);

        if (path.length === 1) {
            if (obj[currentPath] === void 0) {
                return defaultValue;
            }
            return obj[currentPath];
        }

        return objectPath.get(obj[currentPath], path.slice(1), defaultValue);
    };

    objectPath.del = function(obj, path) {
        return del(obj, path);
    };

    return objectPath;
});

/* -- end module lib/object-path -- */
/* -- start module lib/hashes -- */
/*! jshashes - New BSD License - https://github.com/h2non/jshashes */
(function(){var n;function e(n){var e,t,r="",o=-1,f;if(n&&n.length){f=n.length;while((o+=1)<f){e=n.charCodeAt(o);t=o+1<f?n.charCodeAt(o+1):0;if(55296<=e&&e<=56319&&56320<=t&&t<=57343){e=65536+((e&1023)<<10)+(t&1023);o+=1}if(e<=127){r+=String.fromCharCode(e)}else if(e<=2047){r+=String.fromCharCode(192|e>>>6&31,128|e&63)}else if(e<=65535){r+=String.fromCharCode(224|e>>>12&15,128|e>>>6&63,128|e&63)}else if(e<=2097151){r+=String.fromCharCode(240|e>>>18&7,128|e>>>12&63,128|e>>>6&63,128|e&63)}}}return r}function t(n){var e,t,r,o,f,i=[],h;e=t=r=o=f=0;if(n&&n.length){h=n.length;n+="";while(e<h){r=n.charCodeAt(e);t+=1;if(r<128){i[t]=String.fromCharCode(r);e+=1}else if(r>191&&r<224){o=n.charCodeAt(e+1);i[t]=String.fromCharCode((r&31)<<6|o&63);e+=2}else{o=n.charCodeAt(e+1);f=n.charCodeAt(e+2);i[t]=String.fromCharCode((r&15)<<12|(o&63)<<6|f&63);e+=3}}}return i.join("")}function r(n,e){var t=(n&65535)+(e&65535),r=(n>>16)+(e>>16)+(t>>16);return r<<16|t&65535}function o(n,e){return n<<e|n>>>32-e}function f(n,e){var t=e?"0123456789ABCDEF":"0123456789abcdef",r="",o,f=0,i=n.length;for(;f<i;f+=1){o=n.charCodeAt(f);r+=t.charAt(o>>>4&15)+t.charAt(o&15)}return r}function i(n){var e,t=n.length,r="";for(e=0;e<t;e+=1){r+=String.fromCharCode(n.charCodeAt(e)&255,n.charCodeAt(e)>>>8&255)}return r}function h(n){var e,t=n.length,r="";for(e=0;e<t;e+=1){r+=String.fromCharCode(n.charCodeAt(e)>>>8&255,n.charCodeAt(e)&255)}return r}function u(n){var e,t=n.length*32,r="";for(e=0;e<t;e+=8){r+=String.fromCharCode(n[e>>5]>>>24-e%32&255)}return r}function a(n){var e,t=n.length*32,r="";for(e=0;e<t;e+=8){r+=String.fromCharCode(n[e>>5]>>>e%32&255)}return r}function c(n){var e,t=n.length*8,r=Array(n.length>>2),o=r.length;for(e=0;e<o;e+=1){r[e]=0}for(e=0;e<t;e+=8){r[e>>5]|=(n.charCodeAt(e/8)&255)<<e%32}return r}function l(n){var e,t=n.length*8,r=Array(n.length>>2),o=r.length;for(e=0;e<o;e+=1){r[e]=0}for(e=0;e<t;e+=8){r[e>>5]|=(n.charCodeAt(e/8)&255)<<24-e%32}return r}function D(n,e){var t=e.length,r=Array(),o,f,i,h,u,a,c,l;a=Array(Math.ceil(n.length/2));h=a.length;for(o=0;o<h;o+=1){a[o]=n.charCodeAt(o*2)<<8|n.charCodeAt(o*2+1)}while(a.length>0){u=Array();i=0;for(o=0;o<a.length;o+=1){i=(i<<16)+a[o];f=Math.floor(i/t);i-=f*t;if(u.length>0||f>0){u[u.length]=f}}r[r.length]=i;a=u}c="";for(o=r.length-1;o>=0;o--){c+=e.charAt(r[o])}l=Math.ceil(n.length*8/(Math.log(e.length)/Math.log(2)));for(o=c.length;o<l;o+=1){c=e[0]+c}return c}function B(n,e){var t="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",r="",o=n.length,f,i,h;e=e||"=";for(f=0;f<o;f+=3){h=n.charCodeAt(f)<<16|(f+1<o?n.charCodeAt(f+1)<<8:0)|(f+2<o?n.charCodeAt(f+2):0);for(i=0;i<4;i+=1){if(f*8+i*6>n.length*8){r+=e}else{r+=t.charAt(h>>>6*(3-i)&63)}}}return r}n={VERSION:"1.0.5",Base64:function(){var n="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",r="=",o=false,f=true;this.encode=function(t){var o,i,h,u="",a=t.length;r=r||"=";t=f?e(t):t;for(o=0;o<a;o+=3){h=t.charCodeAt(o)<<16|(o+1<a?t.charCodeAt(o+1)<<8:0)|(o+2<a?t.charCodeAt(o+2):0);for(i=0;i<4;i+=1){if(o*8+i*6>a*8){u+=r}else{u+=n.charAt(h>>>6*(3-i)&63)}}}return u};this.decode=function(e){var o,i,h,u,a,c,l,D,B,C,A="",s=[];if(!e){return e}o=C=0;e=e.replace(new RegExp("\\"+r,"gi"),"");do{a=n.indexOf(e.charAt(o+=1));c=n.indexOf(e.charAt(o+=1));l=n.indexOf(e.charAt(o+=1));D=n.indexOf(e.charAt(o+=1));B=a<<18|c<<12|l<<6|D;i=B>>16&255;h=B>>8&255;u=B&255;C+=1;if(l===64){s[C]=String.fromCharCode(i)}else if(D===64){s[C]=String.fromCharCode(i,h)}else{s[C]=String.fromCharCode(i,h,u)}}while(o<e.length);A=s.join("");A=f?t(A):A;return A};this.setPad=function(n){r=n||r;return this};this.setTab=function(e){n=e||n;return this};this.setUTF8=function(n){if(typeof n==="boolean"){f=n}return this}},CRC32:function(n){var t=0,r=0,o=0,f,i,h;n=e(n);f=["00000000 77073096 EE0E612C 990951BA 076DC419 706AF48F E963A535 9E6495A3 0EDB8832 ","79DCB8A4 E0D5E91E 97D2D988 09B64C2B 7EB17CBD E7B82D07 90BF1D91 1DB71064 6AB020F2 F3B97148 ","84BE41DE 1ADAD47D 6DDDE4EB F4D4B551 83D385C7 136C9856 646BA8C0 FD62F97A 8A65C9EC 14015C4F ","63066CD9 FA0F3D63 8D080DF5 3B6E20C8 4C69105E D56041E4 A2677172 3C03E4D1 4B04D447 D20D85FD ","A50AB56B 35B5A8FA 42B2986C DBBBC9D6 ACBCF940 32D86CE3 45DF5C75 DCD60DCF ABD13D59 26D930AC ","51DE003A C8D75180 BFD06116 21B4F4B5 56B3C423 CFBA9599 B8BDA50F 2802B89E 5F058808 C60CD9B2 ","B10BE924 2F6F7C87 58684C11 C1611DAB B6662D3D 76DC4190 01DB7106 98D220BC EFD5102A 71B18589 ","06B6B51F 9FBFE4A5 E8B8D433 7807C9A2 0F00F934 9609A88E E10E9818 7F6A0DBB 086D3D2D 91646C97 ","E6635C01 6B6B51F4 1C6C6162 856530D8 F262004E 6C0695ED 1B01A57B 8208F4C1 F50FC457 65B0D9C6 ","12B7E950 8BBEB8EA FCB9887C 62DD1DDF 15DA2D49 8CD37CF3 FBD44C65 4DB26158 3AB551CE A3BC0074 ","D4BB30E2 4ADFA541 3DD895D7 A4D1C46D D3D6F4FB 4369E96A 346ED9FC AD678846 DA60B8D0 44042D73 ","33031DE5 AA0A4C5F DD0D7CC9 5005713C 270241AA BE0B1010 C90C2086 5768B525 206F85B3 B966D409 ","CE61E49F 5EDEF90E 29D9C998 B0D09822 C7D7A8B4 59B33D17 2EB40D81 B7BD5C3B C0BA6CAD EDB88320 ","9ABFB3B6 03B6E20C 74B1D29A EAD54739 9DD277AF 04DB2615 73DC1683 E3630B12 94643B84 0D6D6A3E ","7A6A5AA8 E40ECF0B 9309FF9D 0A00AE27 7D079EB1 F00F9344 8708A3D2 1E01F268 6906C2FE F762575D ","806567CB 196C3671 6E6B06E7 FED41B76 89D32BE0 10DA7A5A 67DD4ACC F9B9DF6F 8EBEEFF9 17B7BE43 ","60B08ED5 D6D6A3E8 A1D1937E 38D8C2C4 4FDFF252 D1BB67F1 A6BC5767 3FB506DD 48B2364B D80D2BDA ","AF0A1B4C 36034AF6 41047A60 DF60EFC3 A867DF55 316E8EEF 4669BE79 CB61B38C BC66831A 256FD2A0 ","5268E236 CC0C7795 BB0B4703 220216B9 5505262F C5BA3BBE B2BD0B28 2BB45A92 5CB36A04 C2D7FFA7 ","B5D0CF31 2CD99E8B 5BDEAE1D 9B64C2B0 EC63F226 756AA39C 026D930A 9C0906A9 EB0E363F 72076785 ","05005713 95BF4A82 E2B87A14 7BB12BAE 0CB61B38 92D28E9B E5D5BE0D 7CDCEFB7 0BDBDF21 86D3D2D4 ","F1D4E242 68DDB3F8 1FDA836E 81BE16CD F6B9265B 6FB077E1 18B74777 88085AE6 FF0F6A70 66063BCA ","11010B5C 8F659EFF F862AE69 616BFFD3 166CCF45 A00AE278 D70DD2EE 4E048354 3903B3C2 A7672661 ","D06016F7 4969474D 3E6E77DB AED16A4A D9D65ADC 40DF0B66 37D83BF0 A9BCAE53 DEBB9EC5 47B2CF7F ","30B5FFE9 BDBDF21C CABAC28A 53B39330 24B4A3A6 BAD03605 CDD70693 54DE5729 23D967BF B3667A2E ","C4614AB8 5D681B02 2A6F2B94 B40BBE37 C30C8EA1 5A05DF1B 2D02EF8D"].join("");t=t^-1;for(i=0,h=n.length;i<h;i+=1){o=(t^n.charCodeAt(i))&255;r="0x"+f.substr(o*9,8);t=t>>>8^r}return(t^-1)>>>0},MD5:function(n){var t=n&&typeof n.uppercase==="boolean"?n.uppercase:false,i=n&&typeof n.pad==="string"?n.pda:"=",h=n&&typeof n.utf8==="boolean"?n.utf8:true;this.hex=function(n){return f(u(n,h),t)};this.b64=function(n){return B(u(n),i)};this.any=function(n,e){return D(u(n,h),e)};this.raw=function(n){return u(n,h)};this.hex_hmac=function(n,e){return f(l(n,e),t)};this.b64_hmac=function(n,e){return B(l(n,e),i)};this.any_hmac=function(n,e,t){return D(l(n,e),t)};this.vm_test=function(){return hex("abc").toLowerCase()==="900150983cd24fb0d6963f7d28e17f72"};this.setUpperCase=function(n){if(typeof n==="boolean"){t=n}return this};this.setPad=function(n){i=n||i;return this};this.setUTF8=function(n){if(typeof n==="boolean"){h=n}return this};function u(n){n=h?e(n):n;return a(C(c(n),n.length*8))}function l(n,t){var r,o,f,i,u;n=h?e(n):n;t=h?e(t):t;r=c(n);if(r.length>16){r=C(r,n.length*8)}o=Array(16),f=Array(16);for(u=0;u<16;u+=1){o[u]=r[u]^909522486;f[u]=r[u]^1549556828}i=C(o.concat(c(t)),512+t.length*8);return a(C(f.concat(i),512+128))}function C(n,e){var t,o,f,i,h,u=1732584193,a=-271733879,c=-1732584194,l=271733878;n[e>>5]|=128<<e%32;n[(e+64>>>9<<4)+14]=e;for(t=0;t<n.length;t+=16){o=u;f=a;i=c;h=l;u=s(u,a,c,l,n[t+0],7,-680876936);l=s(l,u,a,c,n[t+1],12,-389564586);c=s(c,l,u,a,n[t+2],17,606105819);a=s(a,c,l,u,n[t+3],22,-1044525330);u=s(u,a,c,l,n[t+4],7,-176418897);l=s(l,u,a,c,n[t+5],12,1200080426);c=s(c,l,u,a,n[t+6],17,-1473231341);a=s(a,c,l,u,n[t+7],22,-45705983);u=s(u,a,c,l,n[t+8],7,1770035416);l=s(l,u,a,c,n[t+9],12,-1958414417);c=s(c,l,u,a,n[t+10],17,-42063);a=s(a,c,l,u,n[t+11],22,-1990404162);u=s(u,a,c,l,n[t+12],7,1804603682);l=s(l,u,a,c,n[t+13],12,-40341101);c=s(c,l,u,a,n[t+14],17,-1502002290);a=s(a,c,l,u,n[t+15],22,1236535329);u=w(u,a,c,l,n[t+1],5,-165796510);l=w(l,u,a,c,n[t+6],9,-1069501632);c=w(c,l,u,a,n[t+11],14,643717713);a=w(a,c,l,u,n[t+0],20,-373897302);u=w(u,a,c,l,n[t+5],5,-701558691);l=w(l,u,a,c,n[t+10],9,38016083);c=w(c,l,u,a,n[t+15],14,-660478335);a=w(a,c,l,u,n[t+4],20,-405537848);u=w(u,a,c,l,n[t+9],5,568446438);l=w(l,u,a,c,n[t+14],9,-1019803690);c=w(c,l,u,a,n[t+3],14,-187363961);a=w(a,c,l,u,n[t+8],20,1163531501);u=w(u,a,c,l,n[t+13],5,-1444681467);l=w(l,u,a,c,n[t+2],9,-51403784);c=w(c,l,u,a,n[t+7],14,1735328473);a=w(a,c,l,u,n[t+12],20,-1926607734);u=F(u,a,c,l,n[t+5],4,-378558);l=F(l,u,a,c,n[t+8],11,-2022574463);c=F(c,l,u,a,n[t+11],16,1839030562);a=F(a,c,l,u,n[t+14],23,-35309556);u=F(u,a,c,l,n[t+1],4,-1530992060);l=F(l,u,a,c,n[t+4],11,1272893353);c=F(c,l,u,a,n[t+7],16,-155497632);a=F(a,c,l,u,n[t+10],23,-1094730640);u=F(u,a,c,l,n[t+13],4,681279174);l=F(l,u,a,c,n[t+0],11,-358537222);c=F(c,l,u,a,n[t+3],16,-722521979);a=F(a,c,l,u,n[t+6],23,76029189);u=F(u,a,c,l,n[t+9],4,-640364487);l=F(l,u,a,c,n[t+12],11,-421815835);c=F(c,l,u,a,n[t+15],16,530742520);a=F(a,c,l,u,n[t+2],23,-995338651);u=E(u,a,c,l,n[t+0],6,-198630844);l=E(l,u,a,c,n[t+7],10,1126891415);c=E(c,l,u,a,n[t+14],15,-1416354905);a=E(a,c,l,u,n[t+5],21,-57434055);u=E(u,a,c,l,n[t+12],6,1700485571);l=E(l,u,a,c,n[t+3],10,-1894986606);c=E(c,l,u,a,n[t+10],15,-1051523);a=E(a,c,l,u,n[t+1],21,-2054922799);u=E(u,a,c,l,n[t+8],6,1873313359);l=E(l,u,a,c,n[t+15],10,-30611744);c=E(c,l,u,a,n[t+6],15,-1560198380);a=E(a,c,l,u,n[t+13],21,1309151649);u=E(u,a,c,l,n[t+4],6,-145523070);l=E(l,u,a,c,n[t+11],10,-1120210379);c=E(c,l,u,a,n[t+2],15,718787259);a=E(a,c,l,u,n[t+9],21,-343485551);u=r(u,o);a=r(a,f);c=r(c,i);l=r(l,h)}return Array(u,a,c,l)}function A(n,e,t,f,i,h){return r(o(r(r(e,n),r(f,h)),i),t)}function s(n,e,t,r,o,f,i){return A(e&t|~e&r,n,e,o,f,i)}function w(n,e,t,r,o,f,i){return A(e&r|t&~r,n,e,o,f,i)}function F(n,e,t,r,o,f,i){return A(e^t^r,n,e,o,f,i)}function E(n,e,t,r,o,f,i){return A(t^(e|~r),n,e,o,f,i)}},SHA1:function(n){var t=n&&typeof n.uppercase==="boolean"?n.uppercase:false,i=n&&typeof n.pad==="string"?n.pda:"=",h=n&&typeof n.utf8==="boolean"?n.utf8:true;this.hex=function(n){return f(a(n,h),t)};this.b64=function(n){return B(a(n,h),i)};this.any=function(n,e){return D(a(n,h),e)};this.raw=function(n){return a(n,h)};this.hex_hmac=function(n,e){return f(c(n,e))};this.b64_hmac=function(n,e){return B(c(n,e),i)};this.any_hmac=function(n,e,t){return D(c(n,e),t)};this.vm_test=function(){return hex("abc").toLowerCase()==="900150983cd24fb0d6963f7d28e17f72"};this.setUpperCase=function(n){if(typeof n==="boolean"){t=n}return this};this.setPad=function(n){i=n||i;return this};this.setUTF8=function(n){if(typeof n==="boolean"){h=n}return this};function a(n){n=h?e(n):n;return u(C(l(n),n.length*8))}function c(n,t){var r,o,f,i,a;n=h?e(n):n;t=h?e(t):t;r=l(n);if(r.length>16){r=C(r,n.length*8)}o=Array(16),f=Array(16);for(i=0;i<16;i+=1){o[i]=r[i]^909522486;f[i]=r[i]^1549556828}a=C(o.concat(l(t)),512+t.length*8);return u(C(f.concat(a),512+160))}function C(n,e){var t,f,i,h,u,a,c,l,D=Array(80),B=1732584193,C=-271733879,w=-1732584194,F=271733878,E=-1009589776;n[e>>5]|=128<<24-e%32;n[(e+64>>9<<4)+15]=e;for(t=0;t<n.length;t+=16){h=B,u=C;a=w;c=F;l=E;for(f=0;f<80;f+=1){if(f<16){D[f]=n[t+f]}else{D[f]=o(D[f-3]^D[f-8]^D[f-14]^D[f-16],1)}i=r(r(o(B,5),A(f,C,w,F)),r(r(E,D[f]),s(f)));E=F;F=w;w=o(C,30);C=B;B=i}B=r(B,h);C=r(C,u);w=r(w,a);F=r(F,c);E=r(E,l)}return Array(B,C,w,F,E)}function A(n,e,t,r){if(n<20){return e&t|~e&r}if(n<40){return e^t^r}if(n<60){return e&t|e&r|t&r}return e^t^r}function s(n){return n<20?1518500249:n<40?1859775393:n<60?-1894007588:-899497514}},SHA256:function(n){var t=n&&typeof n.uppercase==="boolean"?n.uppercase:false,o=n&&typeof n.pad==="string"?n.pda:"=",i=n&&typeof n.utf8==="boolean"?n.utf8:true,h;this.hex=function(n){return f(a(n,i))};this.b64=function(n){return B(a(n,i),o)};this.any=function(n,e){return D(a(n,i),e)};this.raw=function(n){return a(n,i)};this.hex_hmac=function(n,e){return f(c(n,e))};this.b64_hmac=function(n,e){return B(c(n,e),o)};this.any_hmac=function(n,e,t){return D(c(n,e),t)};this.vm_test=function(){return hex("abc").toLowerCase()==="900150983cd24fb0d6963f7d28e17f72"};this.setUpperCase=function(n){if(typeof n==="boolean"){t=n}return this};this.setPad=function(n){o=n||o;return this};this.setUTF8=function(n){if(typeof n==="boolean"){i=n}return this};function a(n,t){n=t?e(n):n;return u(m(l(n),n.length*8))}function c(n,t){n=i?e(n):n;t=i?e(t):t;var r,o=0,f=l(n),h=Array(16),a=Array(16);if(f.length>16){f=m(f,n.length*8)}for(;o<16;o+=1){h[o]=f[o]^909522486;a[o]=f[o]^1549556828}r=m(h.concat(l(t)),512+t.length*8);return u(m(a.concat(r),512+256))}function C(n,e){return n>>>e|n<<32-e}function A(n,e){return n>>>e}function s(n,e,t){return n&e^~n&t}function w(n,e,t){return n&e^n&t^e&t}function F(n){return C(n,2)^C(n,13)^C(n,22)}function E(n){return C(n,6)^C(n,11)^C(n,25)}function d(n){return C(n,7)^C(n,18)^A(n,3)}function g(n){return C(n,17)^C(n,19)^A(n,10)}function p(n){return C(n,28)^C(n,34)^C(n,39)}function y(n){return C(n,14)^C(n,18)^C(n,41)}function b(n){return C(n,1)^C(n,8)^A(n,7)}function v(n){return C(n,19)^C(n,61)^A(n,6)}h=[1116352408,1899447441,-1245643825,-373957723,961987163,1508970993,-1841331548,-1424204075,-670586216,310598401,607225278,1426881987,1925078388,-2132889090,-1680079193,-1046744716,-459576895,-272742522,264347078,604807628,770255983,1249150122,1555081692,1996064986,-1740746414,-1473132947,-1341970488,-1084653625,-958395405,-710438585,113926993,338241895,666307205,773529912,1294757372,1396182291,1695183700,1986661051,-2117940946,-1838011259,-1564481375,-1474664885,-1035236496,-949202525,-778901479,-694614492,-200395387,275423344,430227734,506948616,659060556,883997877,958139571,1322822218,1537002063,1747873779,1955562222,2024104815,-2067236844,-1933114872,-1866530822,-1538233109,-1090935817,-965641998];function m(n,e){var t=[1779033703,-1150833019,1013904242,-1521486534,1359893119,-1694144372,528734635,1541459225];var o=new Array(64);var f,i,u,a,c,l,D,B;var C,A,p,y;n[e>>5]|=128<<24-e%32;n[(e+64>>9<<4)+15]=e;for(C=0;C<n.length;C+=16){f=t[0];i=t[1];u=t[2];a=t[3];c=t[4];l=t[5];D=t[6];B=t[7];for(A=0;A<64;A+=1){if(A<16){o[A]=n[A+C]}else{o[A]=r(r(r(g(o[A-2]),o[A-7]),d(o[A-15])),o[A-16])}p=r(r(r(r(B,E(c)),s(c,l,D)),h[A]),o[A]);y=r(F(f),w(f,i,u));B=D;D=l;l=c;c=r(a,p);a=u;u=i;i=f;f=r(p,y)}t[0]=r(f,t[0]);t[1]=r(i,t[1]);t[2]=r(u,t[2]);t[3]=r(a,t[3]);t[4]=r(c,t[4]);t[5]=r(l,t[5]);t[6]=r(D,t[6]);t[7]=r(B,t[7])}return t}},SHA512:function(n){var t=n&&typeof n.uppercase==="boolean"?n.uppercase:false,r=n&&typeof n.pad==="string"?n.pda:"=",o=n&&typeof n.utf8==="boolean"?n.utf8:true,i;this.hex=function(n){return f(h(n))};this.b64=function(n){return B(h(n),r)};this.any=function(n,e){return D(h(n),e)};this.raw=function(n){return h(n,o)};this.hex_hmac=function(n,e){return f(a(n,e))};this.b64_hmac=function(n,e){return B(a(n,e),r)};this.any_hmac=function(n,e,t){return D(a(n,e),t)};this.vm_test=function(){return hex("abc").toLowerCase()==="900150983cd24fb0d6963f7d28e17f72"};this.setUpperCase=function(n){if(typeof n==="boolean"){t=n}return this};this.setPad=function(n){r=n||r;return this};this.setUTF8=function(n){if(typeof n==="boolean"){o=n}return this};function h(n){n=o?e(n):n;return u(c(l(n),n.length*8))}function a(n,t){n=o?e(n):n;t=o?e(t):t;var r,f=0,i=l(n),h=Array(32),a=Array(32);if(i.length>32){i=c(i,n.length*8)}for(;f<32;f+=1){h[f]=i[f]^909522486;a[f]=i[f]^1549556828}r=c(h.concat(l(t)),1024+t.length*8);return u(c(a.concat(r),1024+512))}function c(n,e){var t,r,o,f=new Array(80),h=new Array(16),u=[new C(1779033703,-205731576),new C(-1150833019,-2067093701),new C(1013904242,-23791573),new C(-1521486534,1595750129),new C(1359893119,-1377402159),new C(-1694144372,725511199),new C(528734635,-79577749),new C(1541459225,327033209)],a=new C(0,0),c=new C(0,0),l=new C(0,0),D=new C(0,0),B=new C(0,0),p=new C(0,0),y=new C(0,0),b=new C(0,0),v=new C(0,0),m=new C(0,0),x=new C(0,0),_=new C(0,0),S=new C(0,0),U=new C(0,0),j=new C(0,0),M=new C(0,0),T=new C(0,0);if(i===undefined){i=[new C(1116352408,-685199838),new C(1899447441,602891725),new C(-1245643825,-330482897),new C(-373957723,-2121671748),new C(961987163,-213338824),new C(1508970993,-1241133031),new C(-1841331548,-1357295717),new C(-1424204075,-630357736),new C(-670586216,-1560083902),new C(310598401,1164996542),new C(607225278,1323610764),new C(1426881987,-704662302),new C(1925078388,-226784913),new C(-2132889090,991336113),new C(-1680079193,633803317),new C(-1046744716,-815192428),new C(-459576895,-1628353838),new C(-272742522,944711139),new C(264347078,-1953704523),new C(604807628,2007800933),new C(770255983,1495990901),new C(1249150122,1856431235),new C(1555081692,-1119749164),new C(1996064986,-2096016459),new C(-1740746414,-295247957),new C(-1473132947,766784016),new C(-1341970488,-1728372417),new C(-1084653625,-1091629340),new C(-958395405,1034457026),new C(-710438585,-1828018395),new C(113926993,-536640913),new C(338241895,168717936),new C(666307205,1188179964),new C(773529912,1546045734),new C(1294757372,1522805485),new C(1396182291,-1651133473),new C(1695183700,-1951439906),new C(1986661051,1014477480),new C(-2117940946,1206759142),new C(-1838011259,344077627),new C(-1564481375,1290863460),new C(-1474664885,-1136513023),new C(-1035236496,-789014639),new C(-949202525,106217008),new C(-778901479,-688958952),new C(-694614492,1432725776),new C(-200395387,1467031594),new C(275423344,851169720),new C(430227734,-1194143544),new C(506948616,1363258195),new C(659060556,-544281703),new C(883997877,-509917016),new C(958139571,-976659869),new C(1322822218,-482243893),new C(1537002063,2003034995),new C(1747873779,-692930397),new C(1955562222,1575990012),new C(2024104815,1125592928),new C(-2067236844,-1578062990),new C(-1933114872,442776044),new C(-1866530822,593698344),new C(-1538233109,-561857047),new C(-1090935817,-1295615723),new C(-965641998,-479046869),new C(-903397682,-366583396),new C(-779700025,566280711),new C(-354779690,-840897762),new C(-176337025,-294727304),new C(116418474,1914138554),new C(174292421,-1563912026),new C(289380356,-1090974290),new C(460393269,320620315),new C(685471733,587496836),new C(852142971,1086792851),new C(1017036298,365543100),new C(1126000580,-1676669620),new C(1288033470,-885112138),new C(1501505948,-60457430),new C(1607167915,987167468),new C(1816402316,1246189591)]}for(r=0;r<80;r+=1){f[r]=new C(0,0)}n[e>>5]|=128<<24-(e&31);n[(e+128>>10<<5)+31]=e;o=n.length;for(r=0;r<o;r+=32){A(l,u[0]);A(D,u[1]);A(B,u[2]);A(p,u[3]);A(y,u[4]);A(b,u[5]);A(v,u[6]);A(m,u[7]);for(t=0;t<16;t+=1){f[t].h=n[r+2*t];f[t].l=n[r+2*t+1]}for(t=16;t<80;t+=1){s(j,f[t-2],19);w(M,f[t-2],29);F(T,f[t-2],6);_.l=j.l^M.l^T.l;_.h=j.h^M.h^T.h;s(j,f[t-15],1);s(M,f[t-15],8);F(T,f[t-15],7);x.l=j.l^M.l^T.l;x.h=j.h^M.h^T.h;d(f[t],_,f[t-7],x,f[t-16])}for(t=0;t<80;t+=1){S.l=y.l&b.l^~y.l&v.l;S.h=y.h&b.h^~y.h&v.h;s(j,y,14);s(M,y,18);w(T,y,9);_.l=j.l^M.l^T.l;_.h=j.h^M.h^T.h;s(j,l,28);w(M,l,2);w(T,l,7);x.l=j.l^M.l^T.l;x.h=j.h^M.h^T.h;U.l=l.l&D.l^l.l&B.l^D.l&B.l;U.h=l.h&D.h^l.h&B.h^D.h&B.h;g(a,m,_,S,i[t],f[t]);E(c,x,U);A(m,v);A(v,b);A(b,y);E(y,p,a);A(p,B);A(B,D);A(D,l);E(l,a,c)}E(u[0],u[0],l);E(u[1],u[1],D);E(u[2],u[2],B);E(u[3],u[3],p);E(u[4],u[4],y);E(u[5],u[5],b);E(u[6],u[6],v);E(u[7],u[7],m)}for(r=0;r<8;r+=1){h[2*r]=u[r].h;h[2*r+1]=u[r].l}return h}function C(n,e){this.h=n;this.l=e}function A(n,e){n.h=e.h;n.l=e.l}function s(n,e,t){n.l=e.l>>>t|e.h<<32-t;n.h=e.h>>>t|e.l<<32-t}function w(n,e,t){n.l=e.h>>>t|e.l<<32-t;n.h=e.l>>>t|e.h<<32-t}function F(n,e,t){n.l=e.l>>>t|e.h<<32-t;n.h=e.h>>>t}function E(n,e,t){var r=(e.l&65535)+(t.l&65535);var o=(e.l>>>16)+(t.l>>>16)+(r>>>16);var f=(e.h&65535)+(t.h&65535)+(o>>>16);var i=(e.h>>>16)+(t.h>>>16)+(f>>>16);n.l=r&65535|o<<16;n.h=f&65535|i<<16}function d(n,e,t,r,o){var f=(e.l&65535)+(t.l&65535)+(r.l&65535)+(o.l&65535);var i=(e.l>>>16)+(t.l>>>16)+(r.l>>>16)+(o.l>>>16)+(f>>>16);var h=(e.h&65535)+(t.h&65535)+(r.h&65535)+(o.h&65535)+(i>>>16);var u=(e.h>>>16)+(t.h>>>16)+(r.h>>>16)+(o.h>>>16)+(h>>>16);n.l=f&65535|i<<16;n.h=h&65535|u<<16}function g(n,e,t,r,o,f){var i=(e.l&65535)+(t.l&65535)+(r.l&65535)+(o.l&65535)+(f.l&65535),h=(e.l>>>16)+(t.l>>>16)+(r.l>>>16)+(o.l>>>16)+(f.l>>>16)+(i>>>16),u=(e.h&65535)+(t.h&65535)+(r.h&65535)+(o.h&65535)+(f.h&65535)+(h>>>16),a=(e.h>>>16)+(t.h>>>16)+(r.h>>>16)+(o.h>>>16)+(f.h>>>16)+(u>>>16);n.l=i&65535|h<<16;n.h=u&65535|a<<16}},RMD160:function(n){var t=n&&typeof n.uppercase==="boolean"?n.uppercase:false,i=n&&typeof n.pad==="string"?n.pda:"=",h=n&&typeof n.utf8==="boolean"?n.utf8:true,u=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,7,4,13,1,10,6,15,3,12,0,9,5,2,14,11,8,3,10,14,4,9,15,8,1,2,7,0,6,13,11,5,12,1,9,11,10,0,8,12,4,13,3,7,15,14,5,6,2,4,0,5,9,7,12,2,10,14,1,3,8,11,6,15,13],a=[5,14,7,0,9,2,11,4,13,6,15,8,1,10,3,12,6,11,3,7,0,13,5,10,14,15,8,12,4,9,1,2,15,5,1,3,7,14,6,9,11,8,12,2,10,0,4,13,8,6,4,1,3,11,15,0,5,12,2,13,9,7,10,14,12,15,10,4,1,5,8,7,6,2,13,14,0,3,9,11],l=[11,14,15,12,5,8,7,9,11,13,14,15,6,7,9,8,7,6,8,13,11,9,7,15,7,12,15,9,11,7,13,12,11,13,6,7,14,9,13,15,14,8,13,6,5,12,7,5,11,12,14,15,14,15,9,8,9,14,5,6,8,6,5,12,9,15,5,11,6,8,13,12,5,12,13,14,11,8,5,6],C=[8,9,9,11,13,15,15,5,7,7,8,11,14,14,12,6,9,13,15,7,12,8,9,11,7,7,12,7,6,15,13,11,9,7,15,11,8,6,6,14,12,13,5,14,13,13,7,5,15,5,8,11,14,14,6,14,6,9,12,9,12,5,15,8,8,5,12,9,12,5,14,6,8,13,6,5,15,13,11,11];this.hex=function(n){return f(A(n,h))};this.b64=function(n){return B(A(n,h),i)};this.any=function(n,e){return D(A(n,h),e)};this.raw=function(n){return A(n,h)};this.hex_hmac=function(n,e){return f(s(n,e))};this.b64_hmac=function(n,e){return B(s(n,e),i)};this.any_hmac=function(n,e,t){return D(s(n,e),t)};this.vm_test=function(){return hex("abc").toLowerCase()==="900150983cd24fb0d6963f7d28e17f72"};this.setUpperCase=function(n){if(typeof n==="boolean"){t=n}return this};this.setPad=function(n){if(typeof n!=="undefined"){i=n}return this};this.setUTF8=function(n){if(typeof n==="boolean"){h=n}return this};function A(n){n=h?e(n):n;return w(F(c(n),n.length*8))}function s(n,t){n=h?e(n):n;t=h?e(t):t;var r,o,f=c(n),i=Array(16),u=Array(16);if(f.length>16){f=F(f,n.length*8)}for(r=0;r<16;r+=1){i[r]=f[r]^909522486;u[r]=f[r]^1549556828}o=F(i.concat(c(t)),512+t.length*8);return w(F(u.concat(o),512+160))}function w(n){var e,t="",r=n.length*32;for(e=0;e<r;e+=8){t+=String.fromCharCode(n[e>>5]>>>e%32&255)}return t}function F(n,e){var t,f,i,h,c=1732584193,D=4023233417,B=2562383102,A=271733878,s=3285377520,w,F,p,y,b,v,m,x,_,S;n[e>>5]|=128<<e%32;n[(e+64>>>9<<4)+14]=e;h=n.length;for(i=0;i<h;i+=16){w=v=c;F=m=D;p=x=B;y=_=A;b=S=s;for(f=0;f<=79;f+=1){t=r(w,E(f,F,p,y));t=r(t,n[i+u[f]]);t=r(t,d(f));t=r(o(t,l[f]),b);w=b;b=y;y=o(p,10);p=F;F=t;t=r(v,E(79-f,m,x,_));t=r(t,n[i+a[f]]);t=r(t,g(f));t=r(o(t,C[f]),S);v=S;S=_;_=o(x,10);x=m;m=t}t=r(D,r(p,_));D=r(B,r(y,S));B=r(A,r(b,v));A=r(s,r(w,m));s=r(c,r(F,x));c=t}return[c,D,B,A,s]}function E(n,e,t,r){return 0<=n&&n<=15?e^t^r:16<=n&&n<=31?e&t|~e&r:32<=n&&n<=47?(e|~t)^r:48<=n&&n<=63?e&r|t&~r:64<=n&&n<=79?e^(t|~r):"rmd160_f: j out of range"}function d(n){return 0<=n&&n<=15?0:16<=n&&n<=31?1518500249:32<=n&&n<=47?1859775393:48<=n&&n<=63?2400959708:64<=n&&n<=79?2840853838:"rmd160_K1: j out of range"}function g(n){return 0<=n&&n<=15?1352829926:16<=n&&n<=31?1548603684:32<=n&&n<=47?1836072691:48<=n&&n<=63?2053994217:64<=n&&n<=79?0:"rmd160_K2: j out of range"}}};(function(e,t){var r=false;if(typeof exports==="object"){r=exports;if(exports&&typeof global==="object"&&global&&global===global.global){e=global}}if(typeof define==="function"&&typeof define.amd==="object"&&define.amd){define("lib/hashes",function(){return n})}else if(r){if(typeof module==="object"&&module&&module.exports===r){module.exports=n}else{r.Hashes=n}}else{e.Hashes=n}})(this)})();
/* -- end module lib/hashes -- */