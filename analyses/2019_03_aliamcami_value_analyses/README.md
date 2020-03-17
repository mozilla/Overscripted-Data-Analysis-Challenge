# Overview

## JSON
All the greatest values are JSON, but they represent very little percentual of the whole data. 

### Most of the data have small value_len 
    (mean = 1356 for the 10% sample)
- 95,58% of the data have value_len smaller than the mean 
- 4,42% are bigger than the mean
- 9.35% are valid JSON

### Values above the mean: 
- 61,54% are NOT valid JSON
- 38,46% are valid JSON

### Values that are 1 standard deviation (std) above the mean 
    (std = 26310 for 10% sample):
- 0,11% are NOT valid JSON
- 99,88% are valid JSON
- The bigger the value the greater the chance of being a valid JSON

### Values 4 std above the mean 
- 100% are valid JSON
- The biggest non-JSON value have the length of 104653

##
The top 46745 gratest value_len are valid JSONs, that is 9.35% of the filtered sample (value_len > mean) and 0,41% of the original 10% sample.

---
## Correlation of location_domain and value

- One domain can produces a single type of output (31%).
- 99% of the domains with single type of output do not produces JSON. 


- 31% of all domains can produce JSON. 
- Only 0,016% of all the domains will aways have JSON as output, and less than half of it will always have the same JSON. 


- One JSON is usually (83.09%) produced by a single script domain.


---

# Future questions

## About JSONs:
- **The JSON values are always from the same location or related domains?***
- **Are there a set of location domains that always produces a JSON?***
- Does the JSON values follow a structure pattern? What pattern?
- What data does the JSON hold? Is there any pattern on content?
- Do they have nested JSON? Css? Html? Javascript? Recursive study on JSON properties.

- Is a JSON's structure for a single script_url domain always the same?
- Is every JSON with the same structure produced by the same script_url domain?

<sub> *See notebook 'isJson_Quantitative_Comparasion.ipynb' for more information<sub> 

## General
I'm think some things here maybe a crawler investigation or just wiki reading, since someone may have already described and explained. I just need to find, read and understand it. 

- Are there other valid data types like html, css... in the values column or just JSON?
- Where does the value comes from? What is it used for? 

## Smal: value_len < mean 
- What are the small values?
- Does the smaller values have any pattern?
- What the majority data type?

## Medium: mean < value_len < (mean + std)
- How many rows are there in the intersection of *“no JSON”* and *“everything is JSON”* ?
- What are they? Are they from a specific script_url domain? Or realated domains? 

## Big: value_len > (mean + std)
- What are the big non-JSON values?

## Security and data sharing:
- Do the value columns have any javascript? nested javascript?
- Do the javascripts in the dataset contain known malicious behaviors?
- Can they collect data that threatens user's privacy?

## Statistical knowledge / coincidence: 
The **mean** of the original 10% sample is pretty similar to the **std** of the sample taken after filtering for values above the mean
- why? 
- Is it a coincidence? 
- Is it always like this? 
- Is it a statistical pattern? 