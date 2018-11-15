import os
import pandas as pd
import ssl
import urllib

from slugify import slugify

################################################################################
# Specify inputs
DATA_DIR = '/media/ddobre/UCOSP_DATA/'  # SD directory
PARQUET_FILE = DATA_DIR + 'sample'      # running over sample data

################################################################################
df = pd.read_parquet(PARQUET_FILE, engine='pyarrow')
df['script_url']

ssl._create_default_https_context = ssl._create_unverified_context
failed = []

for url_name in df['script_url'].unique():
    folder_name = DATA_DIR + r'js_source_files'
    shortened_url = url_name.replace('https://', '').replace('http://', '').replace('/', '_')
    shortened_url = slugify(shortened_url)[:250]
    suffix = '.txt'
    file_name = folder_name + '/' + shortened_url + suffix

    with open(file_name, 'w') as source_file:
        try:
            source_file.write(urllib.request.urlopen(url_name).read().decode(
                'utf-8', 'backslashreplace'))

        except (urllib.error.URLError, ValueError) as e:
            failed.append(url_name)
            print('Attempted:', url_name)
            print(str(e), '\n')
