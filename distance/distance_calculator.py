from distance.graph import Graph
from distance.node import Node

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

graph = Graph.create_from_nodes([a, b, c, d, e, f])

graph.connect(a, b, 5)
graph.connect(b, c, 7)
graph.connect(b, d, 3)
graph.connect(c, e, 4)
graph.connect(d, e, 10)
graph.connect(d, f, 8)

print([(weight, [n.data for n in node]) for (weight, node) in graph.dijkstra(a)])
