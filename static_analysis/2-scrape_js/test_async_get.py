# Original code: Glen Thompson Sep 10 '17
#       https://stackoverflow.com/users/3866246/glen-thompson
#
# Script adapted by David Dobre Nov 14 '18:
#       Added parquet loading, iteration over dataframes, and content saving
################################################################################

import pandas as pd
import concurrent.futures
import requests
import time

################################################################################
out = []
CONNECTIONS = 100
TIMEOUT = 5

MAIN_DIR    = '/media/ddobre/UCOSP_DATA/'
#MAIN_DIR    = '/mnt/Data/UCOSP_DATA/'

OUTPUT_DIR  = MAIN_DIR + 'js_source_files/'

#### Small sample
URL_LIST = MAIN_DIR + 'resources/url_master_list.csv'
input_data = pd.read_csv(URL_LIST);
input_data['script_url'] = input_data['url'] # just for laziness

#### Larger dataset
#URL_LIST = MAIN_DIR + 'resources/sample_full_url_list/'
#
#from pathlib import Path
#PARQUET_DIR = Path(URL_LIST)
#input_data = pd.concat(
#    pd.read_parquet(parquet_file)
#    for parquet_file in PARQUET_DIR.glob('*.parquet')
#)

################################################################################
def load_url(url, filename, timeout):

    ans = requests.head(url, timeout=timeout)

    if (ans.status_code == 200):
        content = requests.get(url).text
    else:
        content = ""

    return ans.status_code, content, filename


################################################################################
with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(load_url, row['script_url'], OUTPUT_DIR + row['filename'], TIMEOUT) for index, row in input_data.iterrows())

    time1 = time.time()

    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data, content, filename = future.result()

            if (data == 200 and content):
                with open(filename, 'w') as source_file:
                    source_file.write(content)

        except Exception as exc:
            data = str(type(exc))

        finally:
            out.append(data)

            # Print out current count
            print(str(len(out)),end="\r")

    time2 = time.time()


################################################################################
# Summary
print("-" * 80)
print('Summary:\nIterated over:\t' + URL_LIST)
print(f'Took:\t\t{time2-time1:.2f} s')
print("-" * 80)
print(pd.Series(out).value_counts())
