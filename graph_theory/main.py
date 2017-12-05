import graph

g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
     }

graph = graph.Graph(g)

