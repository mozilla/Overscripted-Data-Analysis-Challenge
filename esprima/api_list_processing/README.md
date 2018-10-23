API Symbol extraction from JSON database:

Requires Mozilla's API list found on the [browser compatability data github](https://github.com/mdn/browser-compat-data/tree/master/api). For this reference, I've downloaded all of the json files into a directory called `api/`.

To run, need to specify the path to the target .json file, OR a .txt file containing a list of all the .json files you wish to run through, as well as the directory to find all of the files, for example:

`$ python3.6 process_APIs.py api/Window.json api/`

OR 

`$ python3.6 process_APIs.py json_list.txt api/`

Program will run through the specified .json files, extracting methods/symbols, and then checking if these methods/symbols also exist as .json files in the json directory. If they do (and they haven't already been parsed), then program will also check through those files.

Spits out an output `symbol_list.json`, with keys corresponding to the original interface, and values containing the lists of the corresponding symbols and methods.
