# Huge Values Analysis
## Goal
Identify what's in the really large values. Proposed in issue [#22](https://github.com/mozilla/overscripted/issues/22).

## Overview
The dataset was grouped by the first keyword of value column (value_domain).
Some statistical data was taken from the value_len for each row of each group. The result was filtered in search of the hugest values with most occurrencies. 
Initial analysis were performed on "cloudflare" group since it holds the biggest min and max value_len. This demonstrated that the biggest values are structured scraped data in JSON format. 

The top results, sorted by count, are listed bellow. 

## Compiled Results: Top 10
| value_domain                      | mean      | std       | min  | max     | count |
|-----------------------------------|-----------|-----------|------|---------|-------|
| {"ScribeTransport".               | 4128.59   | 1406.46   | 2001 | 7211    | 93409 |
| {"ins-today-sId".                 | 5037.69   | 14446.52  | 2002 | 87748   | 60426 |
| {"criteo_pt_cdb_metrics_expires". | 9529.66   | 53326.72  | 2003 | 692032  | 47543 |
| font-face{font-family.            | 162363.28 | 172503.75 | 2634 | 648067  | 45059 |
| {"CLOUDFLARE.                     | 514484.07 | 634151.12 | 4356 | 3253324 | 42660 |
| {"__qubitUACategorisation".       | 64927.71  | 105887.48 | 2018 | 368966  | 40003 |
| Na9BL8mAQgqyMAy1zxOlJg$0.         | 2236.68   | 178.84    | 2001 | 3312    | 37945 |
| 935971.                           | 3726.06   | 396.41    | 3248 | 4695    | 33010 |
| {"insdrSV".                       | 4026.30   | 12823.05  | 2002 | 191041  | 32981 |
| 834540.                           | 2218.71   | 216.20    | 2001 | 2864    | 32117 |
