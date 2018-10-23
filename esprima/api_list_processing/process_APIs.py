from csv import DictWriter
import json
from os import listdir
from os.path import isfile, join
import sys


################################################################################
# sanity check (ensure correct syntax)
def checkNumberOfInputs():

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
    return


################################################################################
# check input type (txt: list of json files OR single path/to/file.json)
def inputIsFilelist():
    state = False

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
# want to return a dict (lowercase : FileName.json) to recursively get nested
#   methods and properties.
def getAllFileDict():
    master_API_dict = {}

    for entry in listdir(sys.argv[2]):
        key = str.lower(entry.split(".")[0])
        master_API_dict[key] = entry

    return master_API_dict


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

    return str.lower(interface_name), property_list


################################################################################
def recursivelyGetProperties(current_interface, res_dict, master_API_dict):

    # import data from file
    data = importData(current_interface)

    # extract interface name and its associated property list
    interface_name, property_list = extractProperties(data)

    # add entries into the output
    res_dict[interface_name] = property_list

    # iterate over all properties, search if they exist in the master API list
    for entry in property_list:

        # (all keys within res_dict and master_API_dict are lowercase)
        entry = str.lower(entry)
        if (entry in master_API_dict):

            # if they exist, make sure they aren't already in the results dict
            if (entry not in res_dict.keys()):

                # take result, create new seed and recursively fill res_dict
                new_seed = sys.argv[2] + master_API_dict[entry]
                res_dict = recursivelyGetProperties(new_seed, res_dict, \
                        master_API_dict)

    return res_dict


################################################################################
def main():

    # sanity check
    checkNumberOfInputs()

    # init empty dict to store all results
    res_dict = {}

    # read in all available files to recurse over
    master_API_dict = getAllFileDict()

    # check input type
    if (inputIsFilelist()):
        file_list = open(sys.argv[1]).read().splitlines()

        # iterate over the list of specified files
        for entry in file_list:

            # generate a nice filename
            file_location = sys.argv[2] + entry
            res_dict = recursivelyGetProperties(file_location, res_dict, \
                    master_API_dict)

    else:
        # with only one specified file, only need to call getProperties once
        res_dict = recursivelyGetProperties(sys.argv[1], res_dict, \
                master_API_dict)

    # dump all results to a file
    with open('symbol_list.json', 'w') as fp:
        json.dump(res_dict, fp)

    # test output:
#    for key in res_dict:
#        print(key)
#        print("")
#
#        for entry in res_dict[key]:
#            print(entry)
#
#        print("---------------------------------\n\n")

################################################################################
if __name__ == '__main__':
    main();
