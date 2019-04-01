The major differences between the dataset required to train/synthesize ad blocker and tracker blocker is described in this piece of text.

**[Ad blocker:](https://en.wikipedia.org/wiki/Ad_blocking)**

An ad blocker is a program that will remove different kinds of advertising from a Web user’s experience online. These programs target certain kinds of ads, such as pop-ups, banner ads and other common forms of online advertisement, allowing a user to surf the Web without annoying distractions or interruptions.

Some of the ad blockers consists of filter rules which comes from mainly these two lists:

- [EasyList](https://easylist.to/), that is the primary list of ad-blocking filters that all ad blockers use. The “EasyList” block list is open source which can be easily altered accordingly, the default one can be reviewed [here](https://easylist.to/easylist/easylist.txt)

- EasyPrivacy, which is an offshoot of EasyList that prevents ads from following you around the web, by blocking the trackers advertisers use to know where you've been. You can check this list [here]([https://easylist.to/easylist/easyprivacy.txt](https://easylist.to/easylist/easyprivacy.txt)).

List-based ad-blockers block ads as per the following two methods :

1. *Url domains*: Based on the dataset such as EasyList, ad blockers know which domains are not part of ad networks and those domains calls are blocked.

2. *Tags name contained in your code*: Ad blockers go through your script and see the tags, certain labelled tags as ads are blocked. In the same way, images under images/ads are blocked. Also tags under ###, are blocked. Some of the examples of these tags are given below, extracted from the easy list.                                                                                                                               

-  ads-ns. ,ads-placement. ,ads-plugin/ ,ads-ns.
- ###AD1line, ###AD2line, ###AD300Right
- /images/ads-, /images/ads. , /images/ads/*


Consider this example:  Assuming that the tag you are using is named “back” and that your website domain name is company.com, the entry into the EasyList blacklist will read as follows: company.com###back

If you find an entry in a blacklist, simply modify the tag name within your web pages and the reinserted content will once again appear when an ad blocker is detected.

So, the basic working of ad blocker can be seen as:

- URLs matched against filters.
- DOM element names matched against element hiding filters.
- Iframe content removed (iframe tag < iframe > can be recognized by ad blocker.)
- Resource requests blocked.

<hr>

*Now question arises how tracker blocker like [Ghost Rank](https://www.ghostery.com/wp-content/themes/ghostery/images/campaigns/tracker-study/Ghostery_Study_-_Tracking_the_Trackers.pdf) used by [Ghostery](https://www.ghostery.com/) browser is different from list based ad blocker. Does it uses the same technology? Are the datasets it is trained on is same as ad blocker?* Let’s talk about it in detail.

**Tracker Blocker**

The two methods to synthesize a Tracker Blocker are :

- Using the data of real users as collected by browsers such as [ghostery](https://github.com/ghostery/ghostery-extension).

- Using the data collected by a web crawler as in this Mozilla’s repository named [overscipted](https://github.com/mozilla/overscripted).


1. **[Ghostery](https://www.ghostery.com/)**: It primarily use the data collected by its own extension GhostRank. The data consist of lots of information of web pages and links visited by the real ghostery browser users but this may concern the users about the stealing/tracking of data by ghostery itself. The concerns was solved/answer by the CPO at Ghostery in [this](https://www.extremetech.com/internet/212476-is-it-safe-to-use-the-ghostery-privacy-extension) interview.

There are also detailed papers from the cliqz team about their privacy approach and data collection practices : [WhoTracks.me](https://arxiv.org/abs/1804.08959) and [Tracking the Trackers- Ghostery](https://www.ghostery.com/lp/study/)

2. **Mozilla:** The overscripted repository majorly used the data collected by the web crawler that the mozilla organization ran on November 2017. The data primarily consist of attributes such as location, operation, script_url, time_stamp, etc. You can go through the description of various other data attributes from [here](https://github.com/overscripted/blob/master/schema.md). <hr>
