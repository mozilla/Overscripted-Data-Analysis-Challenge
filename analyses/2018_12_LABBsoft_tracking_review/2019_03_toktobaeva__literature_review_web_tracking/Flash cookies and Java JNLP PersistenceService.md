# Flash cookies and Java JNLP PersistenceService
### 1. Summary

Adobe Flash stores two types of objects on users' computers: Local 
Shared Objects (LOSes) and Remote Shared Objects (RSOs.) LOSes, while 
generally referred to as Flash cookies, are fundamentally different 
from HTTP cookies: store 100 Kb of data, harder to erase, cab be 
accessed from all the browsers installed in the system from the same 
storage and do not expire by default. RSOs allow for cooperating Flash 
objects to access the contents locally. Unless passed to the third 
party, the information on LOSes and RSOs can only be read by the domain 
where Adobe Flash was used.

Another way to store data is through Java JNLP Persistence system even 
for applications in the untrusted execution environment. Data stored 
with URLs. Applications are limited to only using those URLs. 

### 2. Detection

##### *In Literature*

It is important to note that the detection accuracy relies on two 
conditions: user not disallowing Flash cookies and not blocking Flash
execution/Java applets. 

Adobe supports ClearSiteData API (since v.10.3), which is invoked by all
main browsers. The Flash manager allows for blocking of storage of any
Flash objects.

* Tracks in a private browsing?
    * Yes

##### *In The Overscripted Dataset*
The only reference to the Java Flash possible to find in this dataset is
querying to see if the flash plugin is available.

##### What else would we need to detect it?


##### Do we see it?
Using the symbol_counts.csv from the Overscript Data Prep folder, 
we can check for  the number of times in the dataset that a call to the
window.navigator.plugins[Shockwave Flash].description was made, which
queries whether the Flash plugin is available. 

```
count = 0
for line in f.split('\n'):
    if "plugins[Shockwave Flash].description" in line:
        count += int(line.split(",")[1])
        print(line[17:])
print("Total:", count)
```

Output:
```
plugins[Shockwave Flash].description,1863285
Total: 1863285
```

### 3. References:

_Main information derived from the following sources:_

[A Survey on Web Tracking: Mechanisms, Implications, and Defenses](https://upcommons.upc.edu/bitstream/handle/2117/108437/web_tracking_survey-postprint.pdf)

[Interface PersistenceService](https://docs.oracle.com/javase/7/docs/jre/api/javaws/jnlp/javax/jnlp/PersistenceService.html)

_Supplemental Information:_

[Locally Shared Objects and Flash Cookies – CompTIA Security+ SY0-401: 3.5](https://www.professormesser.com/security-plus/sy0-401/locally-shared-objects-and-flash-cookies/)

[INTRODUCTION TO FLASH LOCAL SHARED-OBJECT](https://www.permadi.com/tutorial/flashSharedObject/index.html)
