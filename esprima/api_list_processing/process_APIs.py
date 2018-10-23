import json
from os import listdir
from os.path import isfile, join
import sys

################################################################################
def inputIsFilelist():
    state = False

    # check correct inputs
    if (len(sys.argv) != 3):
        print('''Warning: invalid input type!
Syntax:
        $ python3.6 this_script.py <list_of_json_files.txt> \
<file_location_dir>
OR
        $ python3.6 this_script.py <path/to/json_file.json> \
<file_location_dir>
''')
        exit()

    # get file extension
    filetype = sys.argv[1].split(".")[-1]

    # check for types
    if (filetype == 'txt'):
        # if txt, must loop over entries
        state = True

    # fail if type is not txt or json
    elif ((filetype != 'json') and (filetype != 'JSON')):
        print("Warning: invalid input type! Need json or txt file")
        exit()

    return state


################################################################################
# import all data from specified filename
def importData(filename):

    # read in JSON data
    with open(filename, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    return data['api']


################################################################################
# once imported data from file, extract the desired properties
def extractProperties(json_data):

    # this only works if guaranteed that json file has one key under 'api'
    interface_name = list(json_data.keys())[0]
    property_list = list(json_data[interface_name].keys())

    return interface_name, property_list

################################################################################
# want to return a dict (lowercase : FileName.json) to recursively get nested
#   methods and properties.
def getAllFileDict():
    ret_dict = {}

    for entry in listdir(sys.argv[2]):
        key = str.lower(entry.split(".")[0])
        ret_dict[key] = entry

    return ret_dict


################################################################################
def main():

    # init empty dict
    res_dict = {}

    # check input type
    if (inputIsFilelist()):
        print("TODO: iterate over list of files")
        data = {}

    else:
        data = importData(sys.argv[1])
        interface_name, property_list = extractProperties(data)

        print(interface_name)
        for entry in property_list:
            print(entry)

        total_API_list = getAllFileDict()
        #print(total_API_list.keys())

        print("\n")
        for entry in property_list:
            if str.lower(entry) in total_API_list:
                print(total_API_list[str.lower(entry)])

################################################################################
if __name__ == '__main__':
    main();
