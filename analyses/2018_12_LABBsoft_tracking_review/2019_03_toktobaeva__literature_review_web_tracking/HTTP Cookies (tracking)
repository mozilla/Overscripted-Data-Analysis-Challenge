# HTTP (tracking) cookies identification
### 1. Summary
Websites store small pieces of data (4KB), cookie files, with a unique 
user identifier on the user's computer. This allows websites to then 
retrieve such identifiers each time the user visits them. While some 
cookies are non-tracking, such as those used for authentication, for the
purposes of the research, we are only interested in the tracking type. 


### 2. Detection

##### *In Literature*

It is important to note that the detection accuracy relies on three 
conditions: user allowing cookies in the first place, the cookie cache 
not being deleted (only 30% of users do so) and the same browser being 
used for accessing the website. With average tracking cookies (more than 
80%) having values longer than 35 characters and some information split
across multiple cookies, the recognition precision is 99.4%. 

Cookies are known for often being set up and read by third party 
websites. Some browsers (including Firefox) and browser add-ons prevent
that from happening. This, however, can be bypassed by a JavaScript
redirecting users to the third party websites. 

Tracking cookies are often leaked from one domain to another, allowing
third parties to exchange information about the user. Some websites pass
information onto tracking services. 

* Tracks in a private browsing?
    * Yes (Safari)
    * No (Chrome, Firefox, IE)

##### *In The Overscripted Dataset*
Cookies were detected a total of 36,148,204 times in the overscripted 
dataset. The only instances of cookies as an explicit name were with 
window.navigator browser version identification, which is a core 
component of fingerprinting.

##### What else would we need to detect it?


##### Do we see it?
Using the symbol_counts.csv from the Overscript Data Prep folder, 
we can check for all named instances of the 'cookies'. 

We don't see the [SetCookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie) 
HTTP response header, which is used to send cookies from the server to 
the user agent.

What we see is the number of times in the dataset that a call to the 
[window.document.cookie](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)
, which gets and sets cookies associated with the document,
and [window.navigator.cookieEnabled](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/cookieEnabled) 
was made, which returns a Bool value that indicates whether or not the 
user has enabled cookies
```
count = 0
for line in f.split('\n'):
    if "cookie" in line:
        count += int(line.split(",")[1])
        print(line[17:])
print("Total:", count)
```

Output:
```
cookie,35455680
cookieEnabled,692524
Total: 36148204
```

### 3. References:

Information derived from the following sources:

[A Survey on Web Tracking: Mechanisms, Implications, and Defenses](https://upcommons.upc.edu/bitstream/handle/2117/108437/web_tracking_survey-postprint.pdf)
