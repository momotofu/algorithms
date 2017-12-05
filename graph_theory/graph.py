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
        self.__graph_dict = graph_dict

    def vertices(self):
        """
        returns the vertices of a graph
        """
        return list(self.__graph_dict.keys())

    def edges(self):
        """
        returns a list of edges in the graph
        """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        If the vertex is not in the self.__graph_dict, a key
        "vertex" with an empty list as a value is added to
        the dictionary, otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        assumes that the edge is of type set, tuple, or list;
        between two vertices can be multiple edges.
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def find_path(self, start_vertex, end_vertex, path=None):
        """
        find a path from start_vertex to end_vertex in graph
        """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + start_vertex
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def __generate_edges(self):
        """
        A static method generating the edges of the graph "graph".
        Edges are reprsented as sets with one (a loop back to the
        vertex) or two vertices.
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        res = "vertices: "
        for key in self.__graph_dict:
            res += str(key) + " "
        res += "\nedges:"
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
