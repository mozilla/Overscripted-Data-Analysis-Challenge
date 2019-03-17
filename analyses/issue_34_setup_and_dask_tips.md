
## Accesing Scripts
 
[Notebook](https://github.com/mozilla/overscripted/blob/master/analyses/issue_34_setup_and_dask_tips.ipynb) with basic examples for finding each of the scripts.

#### hs-analytics:

- To get the hs-analytics scripts, something like df[df.script_url.str.contains('hs-analytics')] will return all the call rows with hs-analytics scripts.

#### akam:

- To get the akam scripts it's df[df.script_url.str.contains('/akam/')]

#### fingerprintjs2:

- To get the script you can search for fingerprint in the script url field

- You can [refer](https://github.com/Valve/fingerprintjs2/blob/master/fingerprint2.js#L919)and look for df[df.argument_0.str.contains('Cwm fjordbank glyphs vext quiz')] as this line can be considered something of a signature for fingerprintjs2 
 and then get all the script urls where that argument is being used.
 
 ## Additional Information
 
- There is no need to develop a technique for detecting fingerprinting. This has already been developed and examples
are in the literature. You can refer "Online Tracking: A 1-million-site Measurement and Analysis " and "The Web's Sixth Sense" on the reading [list](https://github.com/mozilla/overscripted/wiki/Reading-List-(WIP))

- In particular, the code for detecting four types of fingerprinting we're interested in (canvas, font, audio, and webrtc) is available [here](https://github.com/sensor-js/OpenWPM-mobile/blob/mobile_sensors/feature_extraction/extract_features.py)
 
 
