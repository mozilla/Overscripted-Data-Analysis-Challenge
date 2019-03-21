## Browser Attribute Fingerprinting

### Notes

Fingerprinting is a tracking method which is harder to escape than the usual cookies since it leaves no persisten evidence of taggin on the user's computer.

Types of information that browsers make available to websites:

Table from [How unique is your web browser](https://panopticlick.eff.org/static/browser-uniqueness.pdf)

| Variable                                        | Source                                                    | Remarks                                                                                             |
|-------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| User Agent                                      | Transmitted by HTTP, logged by server                     | Contains   Browser   micro-version,   OS version,  language,  toolbars  and  some- times other info |
| HTTP ACCEPT headers                             | Transmitted by HTTP, logged by server                     |                                                                                                     |
| Cookies enabled?                                | nferred in HTTP, logged by server                         |                                                                                                     |
| Screen resolution                               | JavaScript AJAX post                                      |                                                                                                     |
| Timezone                                        | JavaScript AJAX post                                      |                                                                                                     |
| Browser plugins, plugin versions and MIME types | JavaScript AJAX post                                      |                                                                                                     |
| System fonts                                    | Flash applet or Java applet, collected by JavaScript/AJAX |                                                                                                     |

- Some browser enumerate a large amount of system information (navigator.plugins) or gave font lists returned by Flash and JAva. this is used to do browser attribute fingerprinting.

- Some browser report fonts in non-sorted order perhaps due to a filesystem inorder walk.