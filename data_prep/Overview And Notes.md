# Overview of the project and some notes on dataset

### What is this about?
Web-content ecosystem is very advertisement centric right now. Ad-tech continues to evolve methods to collect data to generate more and more engagement. It also leads to models to drive human clicks.

The project is a research effort to search for patterns that describe interactions between users and web-pages. (More on this later)

### Data collection for the research
Gathered information about the JS execution on various websites. JS execution data will tell us about the client-page interaction and different APIs employed on modern Web. Think of it like surveying what are the most used ways to interact with clients on modern, most visited web pages. 

### Details about the dataset
- Master list of pages
This was created using a shallow-crawl on 4 different machines seeded by Alexa's top 10,000 site list. What this essentially means is that each of the 10,000 websites served as seeds and the list of pages linked by these seeds (depth=1) were collected. Taking an intersection of these lists resulted in total 981K unique URLs. This formed the main seed list for OpenWPM crawl.
- Javascript calls data 
Modified version of OpenWPM was used to record JS calls in all 981K URLs. Essentially for each of the 981K pages, 10 second window was chosen to record any javascript activity. 


### Research overview
Once we have the data described above we can look into various patterns and derive insights. This section talks about already explored threads and potential directions of research

#### Examining session replay activity
Session replay is a service that lets website track users' interaction with the page. Think of it as a video reply of user's entire session on Web page. To identify which websites used session replay APIs, a list of websites which embed scripts from analytics providers that offer session recording services was obtained from this [project.](https://webtransparency.cs.princeton.edu/no_boundaries/session_replay_sites.html). Of all the different JS script calls around 96K were to session replay providers. Also, a thing to keep in mind is that even if scripts belonging to session replay providers are being accessed, this does not necessarily mean that session is being recorder or replayed. 

#### Eval and dynamically created function calls
This refers to functions that are dynamically created. Although there is nothing inherently wrong with dynamically created functions but they can be used for injections attacks like [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting). More can be read about this in this [blog post](https://medium.com/firefox-context-graph/overscripted-digging-into-javascript-execution-at-scale-2ed508f21862)

### Cryptojacking
This measns using client-side browser to run crypto mining functions using JS calls. 


