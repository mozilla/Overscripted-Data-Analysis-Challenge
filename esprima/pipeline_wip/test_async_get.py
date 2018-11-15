# Original code: Glen Thompson Sep 10 '17
#       https://stackoverflow.com/users/3866246/glen-thompson
#
# Script adapted by David Dobre Nov 14 '18

import pandas as pd
import concurrent.futures
import requests
import time

out = []
CONNECTIONS = 100
TIMEOUT = 5

data = pd.read_csv('/mnt/Data/UCOSP_DATA/resources/url_master_list.csv');


urls = list(data['url'].values.flatten())

def load_url(url, timeout):
    ans = requests.head(url, timeout=timeout)
    return ans.status_code

with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(load_url, url, TIMEOUT) for url in urls)
    time1 = time.time()
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
        except Exception as exc:
            data = str(type(exc))
        finally:
            out.append(data)

            print(str(len(out)),end="\r")

    time2 = time.time()

print(f'Took {time2-time1:.2f} s')
print(pd.Series(out).value_counts())

out
