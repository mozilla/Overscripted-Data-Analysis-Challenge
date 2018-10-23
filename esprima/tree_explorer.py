import json
import esprima
import visitor

import visitor

####
# Port of estree-walk from Node

class Element:

    BLACKLISTEDKEYS = ['parent']

    ##### Constructor
    def __init__(self, esprima_ast):
        self._ast = esprima_ast         # Assign member var AST
        self._visitors = []             # Init empty visitor array

    ##### Accept a new visitor node
    def accept(self, visitor):
        self._visitors.append(visitor)  # Append a visitor (node?) to visitors
                                        #   array

    ##### (private) Step through the node's queue of potential nodes to visit
    def _step(self, node, queue):
        before = len(queue)

        for key in node.keys():         # Enumerate keys for possible children
            if key in self.BLACKLISTEDKEYS:
                continue                # Ignore node if it is a blacklisted
                                        #   key

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

        return len(queue) != before     # Return whether any children were
                                        #   pushed

    ##### Walk through this AST
    def walk(self):
        queue = [self._ast]             # Add the imported AST to the queue

        while len(queue) > 0:           # While stuff in the queue
            node = queue.pop()          # Pop stuff off of it

            for v in self._visitors:    # Run visitors here
                v.visit(node)

            # If the node is an instance of "esprima node",
            #   step through the queue
            if isinstance(node, esprima.nodes.Node):
                self._step(node, queue)


class MatchPropertyVisitor:

    ##### Constructor
    def __init__(self, property_name, node_handler):
        self._property_name = property_name
        self._node_handler = node_handler   # lambda printing
                                            #   node.type : parent.type

    ##### Visit the nodes
    def visit(self, node):
        if 'MemberExpression' == node.type and \
                node.property.type == 'Identifier' and \
                node.property.name == self._property_name:
            self._node_handler(node)    # Do what the node handler is defined
                                        #   to do

def main():
    print ("#" * 100)

    # Get the AST using esprima
    ast = esprima.parseScript(open('js/snowplow.js').read())

    #print (ast)

    el = Element(ast)

    def parent_type(node):
        return getattr(getattr(node, 'parent', None), 'type', None)

    visitor = MatchPropertyVisitor('colorDepth', lambda n: \
            print("{}:{}".format(n.type, parent_type(n))))

    el.accept(visitor)

    el.walk()

main()

# read the file; generate ast through esprima
# create a new element using that ast
