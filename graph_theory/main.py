from graph import Graph

g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
     }

graph = Graph(g)

print("Vertices of graph: ", graph.vertices());

