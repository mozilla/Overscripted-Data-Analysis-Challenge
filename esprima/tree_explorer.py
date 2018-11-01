#!/usr/bin/env python3

import esprima
import json
import sys
#import visitor # Not yet in use

################################################################################
class Element:

    ## Define keys you want to skip over
    BLACKLISTEDKEYS = ['parent']

    ## Constructor
    def __init__(self, esprima_ast):
        self._ast = esprima_ast         # Assign member var AST
        self._visitors = []             # Init empty visitor array

    ## Add a new visitor to execute (will be executed at each node)
    def accept(self, visitor):
        self._visitors.append(visitor)

    ## (private) Step through the node's queue of potential nodes to visit
    def _step(self, node, queue):
        before = len(queue)

        for key in node.keys():         # Enumerate keys for possible children
            if key in self.BLACKLISTEDKEYS:
                continue                # Ignore node if it is blacklisted

            child = getattr(node, key)  # Assign child = node.key

            # if the child exists && the child has an attribute 'type'
            if child and hasattr(child, 'type') == True:
                child.parent = node     # Assign this node as child's parent
                queue.append(child)     # Append the child in this node's queue

            # if there is a list of children
            if isinstance(child, list):
                for item in child:      # Iterate through them and do the same
                                        #   as above
                    if hasattr(item, 'type') == True:
                        item.parent = node
                        queue.append(item)

        return len(queue) - before     # Return whether any children were
                                        #   pushed

    ## Walk through this AST
    def walk(self):
        queue = [self._ast]             # Add the imported AST to the queue

        # TODO: v1 of depth counting
        depth_counter = 0           #TODO
        this_depth_num_nodes = 1    #TODO
        next_depth_num_nodes = 0    #TODO
        node_counter = 0            #TODO
        this_depth_count = 0

        while len(queue) > 0:           # While stuff in the queue
            node = queue.pop()          # Pop stuff off of it

            this_depth_num_nodes -= 1   #TODO: reduce how many left
            node_counter += 1           #TODO: increment counter


            for v in self._visitors:    # Run visitor instances here
                if v.visit(node):
                    print("\t-> {}; {}".format(node_counter, node_counter - this_depth_count))


            # If node is an instance of "esprima node", step through the queue
            if isinstance(node, esprima.nodes.Node):
#                self._step(node, queue)
                next_depth_num_nodes += self._step(node, queue) #TODO: add how many children


            #TODO
            if this_depth_num_nodes == 0:
                this_depth_num_nodes = next_depth_num_nodes
                next_depth_num_nodes = 0
                this_depth_count = node_counter
                depth_counter += 1
                print("\n-------------------- Depth: {};\t Current: {}\n\n".format(
                    depth_counter, this_depth_count))



################################################################################
"""
Executes specified code given that an input node matches the property name of
    this node.

Attributes:
    _property_name: the name of the property required to execute the handler
    _node_handler:  code to execute if _property_name matches
    visit(node):    checks if input node's property matches this nodes; if yes,
                        executes the code passed into _node_handler, passing the
                        input node as an argument
"""
class MatchPropertyVisitor:

    ## Constructor
    def __init__(self, property_name, node_handler):
        self._property_name = property_name
        self._node_handler = node_handler

    ## Visit the nodes, check if matches, and execute handler if it does
    def visit(self, node):
        if 'MemberExpression' == node.type and \
                node.property.type == 'Identifier' and \
                node.property.name == self._property_name:
            self._node_handler(node)

            return True
        return False


def node_handler(n):

    def parent_type(node):
        return getattr(getattr(node, 'parent', None), 'type', None)

    print("- {}\t\t{}:{}".format(n.property.name, n.type, parent_type(n)))


################################################################################
# Extract JSON and JavaScript AST data from precompiled list
def importData():

    if (len(sys.argv) == 2):
        with open(sys.argv[1], encoding='utf-8') as data_file:
            api_list = json.loads(data_file.read())
        ast = esprima.parseScript(open('js/snowplow.js').read())

        return ast, api_list

    elif (len(sys.argv) == 3):
        with open(sys.argv[1], encoding='utf-8') as data_file:
            api_list = json.loads(data_file.read())
        with open(sys.argv[2]) as js_file:
            ast = esprima.parseScript(js_file.read())

        return ast, api_list

    else:
        print('''Warning: invalid input type!
Syntax:
        $ python3.6 this_script.py <path/to/api_list.json>
OR
        $ python3.6 this_script.py <path/to/api_list.json> \
<path/to/javascript.js>
''')
        exit()

    return


################################################################################
def main():
    print ("#" * 100)

    # Get the AST using esprima
    ast, api_list = importData()

#    # Debugging #########################
#    counter = 0;
#    for key in api_list.keys():         #
#        print(key)                      #
#        print("-------------------")    #
#                                        #
#        for entries in api_list[key]:   #
#            print(entries)              #
#            counter += 1
#                                        #
#        print("")                       #
#    print(counter)
#    #####################################

    # Create an element using that AST
    el = Element(ast)




    # Debugging #########################
    visitors = []
    for key in api_list.keys():         #
        print(key)                      #
        print("-------------------")    #
                                        #
        for entry in api_list[key]:   #
            print(entry)              #
            visitor = MatchPropertyVisitor(entry, node_handler)

            el.accept(visitor)
                                        #
        print("")                       #
    #####################################



#    visitor = MatchPropertyVisitor('userAgent', \
#            lambda n: print("{}:{}".format(n.type, parent_type(n))))

#    el.accept(visitor)

    el.walk()

if __name__ == '__main__':
    main()
