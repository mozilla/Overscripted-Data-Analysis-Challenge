#!/usr/bin/env python3
#
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
# Parameters and input

out = []
CONNECTIONS = 20
TIMEOUT = 2

#MAIN_DIR    = '/media/ddobre/UCOSP_DATA/'
MAIN_DIR    = '/mnt/Data/UCOSP_DATA/'

OUTPUT_DIR  = MAIN_DIR + 'js_source_files/'

#### Small sample
#URL_LIST = MAIN_DIR + 'resources/url_master_list.csv'
#input_data = pd.read_csv(URL_LIST);
#input_data['script_url'] = input_data['url'] # just for laziness

#### Larger dataset
URL_LIST = MAIN_DIR + 'resources/sample_full_url_list_test/'

from pathlib import Path
PARQUET_DIR = Path(URL_LIST)
input_data = pd.concat(
    pd.read_parquet(parquet_file) for parquet_file in PARQUET_DIR.glob('*.parquet')
)

################################################################################
# Handle a URL
def load_url(url, filename, timeout):
    response = requests.get(url, timeout=timeout)
#    print("{}\t{}".format(response.status_code, url))

    if response.status_code == 200:
        content = response.text
#        print("\t\t\t{}".format(len(content)))
#        sys.stdout.write("[%s-%d]]\n" % (url, len(content)))
#        sys.stdout.flush()
        return response.status_code, content, filename

    # Don't forget to cast status code to int. Computers are the suck.
    return int(response.status_code), "", filename

#def load_url(url, filename, timeout):
#
#    ans = requests.head(url, timeout=timeout)
#
#    if (ans.status_code == 200):
#        content = requests.get(url).text
#    else:
#        content = ""
#
#    return ans.status_code, content, filename


################################################################################
# Launch workers
with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (
        executor.submit(
            load_url, row["script_url"], OUTPUT_DIR + row["filename"], TIMEOUT
        )
        for index, row in input_data.iterrows()
    )

    time1 = time.time()

    for future in concurrent.futures.as_completed(future_to_url):
        http_status, content, filename = future.result()
        if http_status == 200 and content:
            print(filename)
            with open(filename, "w") as source_file:
                source_file.write(content)

#    for future in concurrent.futures.as_completed(future_to_url):
#        try:
#            data, content, filename = future.result()
#
#
#            if (data == 200 and content):
#                with open(filename, 'w') as source_file:
#                    source_file.write(content)
#
#        except Exception as exc:
#            data = str(type(exc))
#
#        finally:
#            out.append(data)
#
#            # Print out current count
#            print(str(len(out)),end="\r")

    time2 = time.time()


################################################################################
# Summary
print("-" * 80)
print('Summary:\nIterated over:\t' + URL_LIST)
print(f'Took:\t\t{time2-time1:.2f} s')
print("-" * 80)
print(pd.Series(out).value_counts())
