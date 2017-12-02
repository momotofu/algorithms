""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""

class Graph(object):
    def __init__(self, graph_dict=None):
        """
        Initializes the graph object.
        If no dictionary or None is given,
        an empty dictionary will be used.
        """
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict


