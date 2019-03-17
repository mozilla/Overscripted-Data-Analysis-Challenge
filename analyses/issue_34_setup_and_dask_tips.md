
# Objective

There are some scripts that we can pick out by name that are doing browser attribute fingerprinting:

1. Scripts with hs-analytics in the script_url
2. Scripts with /akam/ in the script_url
3. The fingerprintjs scripts

we aim to build a heuristic for browser attribute fingerprinting that pulls out these scripts


## Accesing Scripts
 
[Notebook](https://github.com/mozilla/overscripted/blob/master/analyses/issue_34_setup_and_dask_tips.ipynb) with basic examples for finding each of the scripts.

#### hs-analytics:

- To get the hs-analytics scripts, something like df[df.script_url.str.contains('hs-analytics')] will return all the call rows with hs-analytics scripts.

- The copy of hs-analytics script which was grabbed and formatted is [here](https://gist.github.com/birdsarah/1d47ed38da7efcc258b388c1951a992e)

- You can find the function "Fingerprint" [here](https://gist.github.com/birdsarah/1d47ed38da7efcc258b388c1951a992e#file-hs-analytics-2-js-L2533)

#### akam:

- To get the akam scripts it's df[df.script_url.str.contains('/akam/')]

- The akam script that was de-obfuscated is [here](https://gist.github.com/birdsarah/3150ec8860ed736aabbedeaff8299153)

#### fingerprintjs2:

- To get the script you can search for fingerprint in the script url field

- You can [refer](https://github.com/Valve/fingerprintjs2/blob/master/fingerprint2.js#L919)and look for df[df.argument_0.str.contains('Cwm fjordbank glyphs vext quiz')] as this line can be considered something of a signature for fingerprintjs2 and then get all the script urls where that argument is being used.

- [This](https://github.com/Valve/fingerprintjs2/blob/master/fingerprint2.js) is the source for fingerprint2.js although there are a number of variants out there.


 ## Additional Information
 
- The notebook supplied does not solve this issue it provides the code to filter some relevant scripts out of the whole dataset. The hard work is then developing a "heuristic" that picks out these scripts and others like it. By "heuristic" it is  meant a rule-set encoded in code that selects for specific scripts and not others.
 
- There is no need to develop a technique for detecting fingerprinting. This has already been developed and examples
are in the literature. You can refer "Online Tracking: A 1-million-site Measurement and Analysis " and "The Web's Sixth Sense" on the reading [list](https://github.com/mozilla/overscripted/wiki/Reading-List-(WIP))

- In particular, the code for detecting four types of fingerprinting we're interested in (canvas, font, audio, and webrtc) is available [here](https://github.com/sensor-js/OpenWPM-mobile/blob/mobile_sensors/feature_extraction/extract_features.py)

- This issue is about developing code like that shown [here](https://github.com/sensor-js/OpenWPM-mobile/blob/mobile_sensors/feature_extraction/extract_features.py) but finding a set of rules that detect browser attribute fingerprinting, that is the type of fingerprinting that compiles together a series of browser attributes. Again, the reading list articles will elaborate this type of fingerprinting in more detail.

- Some work of applying these heuristics to the dataset has been done and the results of the work are [here](https://github.com/mozilla/overscripted/blob/master/analyses/2018_12_willoughr__fingerprinting_prevalence.txt)
