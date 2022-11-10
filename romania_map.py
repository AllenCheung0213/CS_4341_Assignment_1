from graph import *

romania_map = Graph(20, False)

file = open("romania_map")
for i in file.readlines():
    node_val = i.split()
    romania_map.add_edge(node_val[0], node_val[1], node_val[2])
