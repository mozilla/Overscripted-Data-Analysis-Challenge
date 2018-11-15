(01.10.18) David:

WIP: returning node information for target symbols (depth, distance from first node of that depth), as well as parent information. Could also add number of children and sibilings in the future.

Current unsure if the postion info is totally correct; it seems okay but there are a few inconsistencies (for some nodes, parent is 2 layers above the current depth, and there is some double counting of nodes (forced out by breaking the loop when one node has been counted). Issue is probably related.)

Run with:

`$ ./tree_explorer.py symbol_list.json`

(23.10.18) David:

Produced 1st iteration of code to obtain a symbol list from specified APIs, using the [Mozilla Browser Compatability API](https://github.com/mdn/browser-compat-data/tree/master/api) JSON data. Produces a JSON file with keys corresponding to the original API, and the corresponding values containing a list of all symbols. Recursively goes through these symbols if they are also APIs and then also iterates through them.


(18.10.18) David:

We are looking for all symbols at this point; I grabbed the whole list from the [Mozilla web API reference page](https://developer.mozilla.org/en-US/docs/Web/API) and threw it on a file.

(1st commit) Victor:

The tree_visitor.py class implements two classes which can be used in a visitor pattern to inspect the Esprima AST tree for a given
Javascript source file.

Roughly, there is an Element class which accepts Visitor instances.

The code is very rough at this point, but minimally works to walk the tree.

I've also added a visitor.py module which I found that may be helpful in evolving our tree walker to do richer inspection and transformation of the source tree.

