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