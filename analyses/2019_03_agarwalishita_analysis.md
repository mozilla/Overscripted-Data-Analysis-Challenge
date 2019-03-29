The major difference between the dataset required to train/synthesize ad blocker and data blocker is described in this piece of text.

**Ad blocker:**
Its data mainly consists of filter rules which comes from EasyList, EasyPrivacy, etc. which consist of known ads on English Language websites all over the world. You can check the whole list [here](https://easylist.to/easylist/easylist.txt).

  Ad blocker blocks data based on two things:

1.  *Url domains*: Based on the dataset, ad blockers know which domains are not part of ad networks and those domains calls are blocked. You might have gotten idea about this idea after looking at the EasyList.
    
2.  *Tags name contained in your code*: It go through your script and see the tags, certain labelled tags as ads are blocked. In the same way, images under images/ads are blocked.
    
    So, the basic working of ad blocker can be seen as:

-   URLs matched against filters.
    
-   DOM element names matched against element hiding filters.
    
-   Iframe content removed (iframe tag can be recognized by ad blocker).
    
-   Resource requests blocked.

*Now question arises how tracker blocker like Ghost Rank used by ghostery browser is different from ad blocker. Does it uses the same technology? Are the datasets it is trained on is same as ad blocker?* Let’s talk about it in detail.
Tracker Blocker-

These are the ones which are used for tracking the trackers. To explain this, I’ll be taking example of two methods, one used by [ghostery](https://github.com/ghostery/ghostery-extension) browser and another by mozilla in the repository named [overscipted](https://github.com/mozilla/overscripted).

1.  **Ghostery**: It primarily use the data collected by its own extension GhostRank. The data consist of lots of information of web pages and links visited by the real ghostery browser users but this may concern the users about the stealing/tracking of data by ghostery itself. The concerns was solved/answer by the CPO at Ghostery in [this](https://www.extremetech.com/internet/212476-is-it-safe-to-use-the-ghostery-privacy-extension) interview.
2.   **Mozilla:** The overscripted repository’s tracker blocker majorly used the data collected by the web crawler that the mozilla organization ran on … The data primarily consist of attributes such as location, operation, script_url, time_stamp, etc. You can go through the description of various other data attributes from [here](https://github.com/agarwalishita/overscripted/blob/master/schema.md).

Hence, the sample dataset provided in the repository contains absolutely required attributes suitable for a tracker blocker. Thus, the consistency will be best suited to build tracker blocker rather than ad blocker.