from graph import Graph

g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
     }

graph = Graph(g)

print("Vertices of graph: ", graph.vertices())
print("Edges of graph: ", graph.edges())

print("Add vertix: ")
graph.add_vertex("z")

print("Vertices of graph: ", graph.vertices())

print("Add an edge: ")
graph.add_edge({"a", "z"})

print("Edges of graph: ", graph.edges())

print("adding an edge {'y', 'x'} with new vertices: ")
graph.add_edge({"x","y"})
print("vertices of graph: ", graph.vertices())
print("Edges of graph: ", graph.edges())

