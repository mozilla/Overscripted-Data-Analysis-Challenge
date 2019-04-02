## Browser Attribute Fingerprinting

Browser Attribute Fingerprinting referes to uniquely identifing a client based on a set of browser attributes. This kind of fingerprinting is difficult to evade because it doesn't store any cookies on the client-end. Secondly innocuous choices like enabling or disabling a plugin or an add-on adds to a unique identity of a client. Something like adding the system to a no-tracker list in itself adds a unique attribute about the client to the list and in turn increases the chances of a successful fingerprinting. 

Browser Fingerprinting can loosely be defined (but not restricted to) as collecting following information: Browser Plugins, Browser Add-on Enumeration, System Fonts Enumeration, User Agent String, Screen Resolution etc. Details about these can be found [here](https://multilogin.com/browser-fingerprinting-the-surveillance-you-can-t-stop/)

The questions I am trying to answer in this analysis:

- __Detect all the scripts linked in the dataset which can be used for browser finger printing.__ As discussed in [#34](https://github.com/mozilla/overscripted/issues/34) we already know that `hs-analytics`, `fingerprint2.js` and `/akam/` are scripts used for fingerprinting. Can we find features in the dataset using which we can identify other such scripts?

- __Understand which script uses what information to do the fingerprinting.__ This is useful to develop a broad heuristic which we can then employ to understand how prevalent is browser attribute fingerprinting in our dataset. Here I want to identify scripts which use plugin information vs scripts which employ add-ons or screen resolution details to fingerprint browsers. Idea here is that even if a script only takes plugin information it can potentially do fingerprinting without asking client for other attributes. Therefore we can not be too restrictive in our analysis/filtering.

- __Develop a heuristic to identify cases of Browser Attribute Fingerprinting.__ Finally I want to come up with a rule based heuristic which is smart enough to catch all cases of browser attribute fingerprinting. This is linked to both Q1 and Q2. Answering this would require a reasonable progress on both of the earlier questions.


### Analysis 1: What kind of plugin information is queried by JS API executions
`navigator.plugins[SOME PLUGIN]` and `navigator.mimeTypes` symbols are used to query plugin information from the browser. 
In the paper [Device Fingerprinting for Augmentin Web Authentication: Classification and Analysis of Methods](http://people.scs.carleton.ca/~paulv/papers/acsac2016-device-fingerprinting.pdf) authors suggest that plugin information is used as a feature in many fingerprinting scripts to identify uniqueness of browsers.

After analysing the data I found that in the dataset scripts querying for plugin information only query about Shockwave flash player and futuresplash.

### Analysis 2: Which scripts are abusing plugin information to do fingerprinting?
In this analysis I am interested in finding scripts which are taking plugin information with an intention to use it to fingerprint the client. There are 11 unique plugin information attributes available in the dataset. 
I find the scripts which query for all or most of the available plugin attributes (name, description, length etc.). This gave me 1679 unique script urls. Out of these scripts I filtered known cases of fingerprinting scripts (hs-analytics, akam, fingerprint2.js). Finally I am left with 888 potential script_urls which can be fingerprinting.

### Analysis 3: Taking a deep-dive to understand one of the flagged scripts -- metrika/watch.js script which has come up in the analysis?
With a list of potential scripts I choose to take a deeper look into some of the more fishy looking script_urls. `metrika/watch.js` queries for 10 attributes of Shockwave Flash player in each of the location where it is linked. 
After some internet search on `https://mc.yandex.ru/metrika/watch.js` I found this [script](https://github.com/ValdikSS/p0f-mtu-script/blob/master/index.php). 
Looking at the script I can see that it produces a hash and matches it with stored hashes to identify a client. The information used is fetched from `https://mc.yandex.ru/metrika/watch.js`. Therefore this can also potentially be used as fingerprinting script.  

### Analysis 4: Browser fingerprinting using fingerprint.js
fingerprint.j2 or fingerprint2.js are common javascript libraries used for fingerprinting. They query a bunch of features from the client and produces a hashcode using murmur hash functions based on the query results. This assigns a unique (almost) hash to each device and can be used to track client across websites. 

Here I am interested in looking at all calls of fingerprint2.js. I want to understand what all arguments and values are associated with calls to fingerprint2.js. 

I took a look at the timestamps of the queries but realised that timestamps data can't be directly used to understand fingerprinting. There are many variable acting at the same time. During scraping it is possible that two different locations were being scraped around the same time and those calls would be clubbed as well. 
What one should ideally look at is: For the same location how many times fingerprint.js results in JS API execution vs a non-fingerprinting scripts results in JS API executions. In that also it is possible that a non-fingerprinting script has a function which results in multiple JS API executions therefore it will come up multiple times in the dataset. This analysis is not easy to do and maybe not possible to scale.

### Analysis 5: Using symbols used by fingerprint.js
After analysing calls by `fingerprint.js` I realised a bunch of symbols other than plugin information that it was querying for. I wanted to group these symbols and check which all scripts called the same symbols and queried for all attributes.
For this I classified symbols into three categories. This classification was based on the type of query these symbols were associated with. 
- *plugin symbols* -- queried for plugin attributes.
- *canvas symbols* -- queried for HTML Canvas Rendering etc.
- *RTC symbols* -- queried for RTCPeer Connection attributes.
- *other symbols* -- all the symbols queried by fingerprint.js which didn't fall in any of the above category.
I shortlisted for all the scripts which queried for greater than 50% of any of the above symbols list in one location_url. Using this I could shortlist the script_urls which queried *majority* of the plugin information available or *majority* of the RTCPeer connection information available etc. More analysis can be done to change threshold from 50% to a higher/lower number. 

This resulted in a filtered list of script_urls. Now my simple heuristic for identifying cases of browser attribute fingerprinting taking intersection of the script_url lists for any two of the above four classes. 


### Questions for further analysis

- How many of the script_urls identified are actually doing canvas finger printing and not browser attribute finger printing (particularly for the scripts in canvas_potential?
- How is RTCPeerConnection information used?
- Is there an automatic way to download the linked javascript file from script_url and parse it to look for keywords like "murmurhash", "hashset", "fingerprint"?
- An assumption underlying the above analysis is that the script has to make different calls to the same location with different symbols to get information which it can then hash. Is it possible that a script can make just one call to a function which returns all the information in the value_1000? How would that look
- Current set of potential scripts are restricted by canvas_potential and other_potential. Is it the correct set to restrict? Can we ignore these scripts assuming they are doing only canvas fingerprinting? Maybe we can use previous study done [here](https://github.com/mozilla/overscripted/blob/master/analyses/2018_09_biskit1_mordax__canvas_fingerprinting.ipynb) to white-list some scripts and focus only on scripts doing browser attribute fingerprinting.


--------------------------------------------------------------------------------
#### Notes[WIP]

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

- Fingerprinting using information in Javascript implementations [Link](https://cseweb.ucsd.edu/~kmowery/papers/js-fingerprinting.pdf)

Notes from [Device Fingerprinting for Augmenting Web Authentication:Classification and Analysis of Methods](http://people.scs.carleton.ca/~paulv/papers/acsac2016-device-fingerprinting.pdf)


### Questions to explore/answer

- How does hs-analytics track me?
This can help me identify the value/arguments passed whenver hs-analytics is called and can identify other scripts with same/similar arguments.
- Can we build a hueristic for website attribute fingerprinting?
I feel we can start with something like where a lot of browser information is being passed. That is a red flag. With enough broser information my hash would quickly become unique and can be tracked always.



### Loose ends (Hastily gathered links and readings to follow-up)
- navigator.plugins ---> this is used to validate if a given plugin is enabled or not on the browser. Therefore it can generate some ID for a browser based on what all plugins are enabled etc. This led me to a cool [link](http://www.howtocreate.co.uk/wrongWithIE/?chapter=navigator.plugins) which introduced me to navigator.mimeTypes a similar kind of function. Idea: If navigator.plugin and navigator.mimeTypes are called together multiple times with different arguments they can be used for fingerprinting.

- Check what is happening in this script -- "https://mc.yandex.ru/metrika/watch.js" It asks a lot about flash players. But seems like this is linked to websites which display videos? Think. think. think.


- http://pseudo-flaw.net/content/defcon/