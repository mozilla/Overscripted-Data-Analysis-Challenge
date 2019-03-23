# Overview

All the greatest values are JSON, but they represent very little percentage of the whole data. 

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
