## Browser Attribute Fingerprinting

### Notes

Fingerprinting is a tracking method which is harder to escape than the usual cookies since it leaves no persisten evidence of taggin on the user's computer.

Types of information that browsers make available to websites:

Table from [How unique is your web browser](https://panopticlick.eff.org/static/browser-uniqueness.pdf)

| Variable                                        | Source                                                    | Remarks                                                                                             |
|-------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| User Agent                                      | Transmitted by HTTP, logged by server                     | Contains   Browser   micro-version,   OS version,  language,  toolbars  and  some- times other info |
| HTTP ACCEPT headers                             | Transmitted by HTTP, logged by server                     |                                                                                                     |
| Cookies enabled?                                | Inferred in HTTP, logged by server                         |                                                                                                     |
| Screen resolution                               | JavaScript AJAX post                                      |                                                                                                     |
| Timezone                                        | JavaScript AJAX post                                      |                                                                                                     |
| Browser plugins, plugin versions and MIME types | JavaScript AJAX post                                      |                                                                                                     |
| System fonts                                    | Flash applet or Java applet, collected by JavaScript/AJAX |                                                                                                     |

- Some browser enumerate a large amount of system information (navigator.plugins) or gave font lists returned by Flash and JAva. this is used to do browser attribute fingerprinting.

- Some browser report fonts in non-sorted order perhaps due to a filesystem inorder walk.

- [This](https://multilogin.com/browser-fingerprinting-the-surveillance-you-can-t-stop/) talks about different kind of ways in browser can send attribute data over internet.

- [Very interesting paper](https://www.datenzone.de/blog/wp-content/uploads/2016/10/Disguised-Chromium-Browser-Robust-Browser-Flash-and-Canvas-Fingerprinting-Protection.pdf). This one talks about an anti-fingerprinting strategy also gives out few well-known finger printing scripts. Fingerprint.JS Coinbase Payment Button, BlueCanva etc.

- Reddit thread on [how to really avoid finger printing](https://www.reddit.com/r/privacy/comments/31zt8r/how_to_really_really_avoid_fingerprinting/)

### Questions to explore/answer

- How does hs-analytics track me?
This can help me identify the value/arguments passed whenver hs-analytics is called and can identify other scripts with same/similar arguments.
- Can we build a hueristic for website attribute fingerprinting?
I feel we can start with something like where a lot of browser information is being passed. That is a red flag. With enough broser information my hash would quickly become unique and can be tracked always.



### Loose ends (Hastily gathered links and readings to follow-up)
- navigator.plugins ---> this is used to validate if a given plugin is enabled or not on the browser. Therefore it can generate some ID for a browser based on what all plugins are enabled etc. This led me to a cool [link](http://www.howtocreate.co.uk/wrongWithIE/?chapter=navigator.plugins) which introduced me to navigator.mimeTypes a similar kind of function. Idea: If navigator.plugin and navigator.mimeTypes are called together multiple times with different arguments they can be used for fingerprinting.

- Check what is happening in this script -- "https://mc.yandex.ru/metrika/watch.js" It asks a lot about flash players. But seems like this is linked to websites which display videos? Think. think. think.