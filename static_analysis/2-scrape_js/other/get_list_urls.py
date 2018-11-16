import json
import os
import pandas as pd
import requests
import ssl
import urllib
from configparser import ConfigParser
from slugify import slugify


# Specify inputs
parser = ConfigParser()
parser.read('config.ini')

# Program state: either looking for existing
USE_EXISTING_LOOKUP = False
if (parser['Downloading'] == "True"):
    USE_EXISTING_LOOKUP = True

# Main working directory
MAIN_DIR = parser['Downloading']['ParentWorkingDirectory']

# Where the files will be downloaded to
DATA_DIR = MAIN_DIR + parser['Downloading']['JSOutputDirectory']

# If generating or looking up a table
LOOKUP_DIR = MAIN_DIR + parser['Downloading']['LookupDirectory']
LOOKUP_FILE = parser['Downloading']['LookupFile']

# If generating a new dataset
if (bool(parser['Downloading']['ParquetDataset'])):
    PARQUET_FILE = MAIN_DIR + parser['Downloading']['ParquetDataset']      # running over sample data


# In[4]:


def shorten_name(url_name):
    shortened_url = url_name.replace('https://', '').replace('http://', '').replace('/', '_')
    shortened_url = slugify(shortened_url)[:250]
    suffix = '.txt'
    file_name = shortened_url + suffix

    return file_name


# In[5]:


if (USE_EXISTING_LOOKUP & os.path.isfile(LOOKUP_DIR + LOOKUP_FILE)):
    print("Existing Lookup table found...")
    url_data = pd.read_csv(LOOKUP_DIR + LOOKUP_FILE)

else:
    print("Generating Lookup table...")
    raw_data = pd.read_parquet(PARQUET_FILE, engine='pyarrow')
    url_data = pd.DataFrame()
    url_data['url'] = raw_data['script_url'].unique()
    url_data['filename'] = url_data['url'].apply(shorten_name)
    url_data = url_data.sort_values('filename')
    url_data['status'] = -1



# In[6]:


url_data


# In[7]:


#for url_name in df['script_url'].unique():
#    file_name = shorten_name(DATA_DIR, url_name)
#
#    #with open(file_name, 'w') as source_file:

#    try:
#        r = requests.get(url_name, verify=False)
#        print("{}\n\t\t{}".format(url_name, r.status_code))
#    except (requests.exceptions.RequestException) as e:
#        print("{}\n\t\t{}".format(url_name, e))



# In[26]:


ssl._create_default_https_context = ssl._create_unverified_context
failed = []

for url_name in url_data['script_url']:


    with open(file_name, 'w') as source_file:
        try:
            source_file.write(urllib.request.urlopen(url_name).read().decode(
                'utf-8', 'backslashreplace'))
            print(url_name)
            print("")

        except (urllib.error.URLError, ValueError) as e:
            failed.append(url_name)
            print('Attempted:', url_name)
            print(str(e), '\n')

