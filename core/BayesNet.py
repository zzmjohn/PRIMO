import sys
sys.path.append("../lib/networkx-1.7-py2.7.egg")
import networkx as nx
import Node.Node


class BayesNet(object):
    graph = nx.DiGraph()

    def __init__(self):
        print "lol"

    def add_node(self, node):
        if isinstance(node, Node.Node):
            self.graph.add_node(node)
        else:
            raise Exception("Can only add 'Node' and its subclasses as nodes into the BayesNet")