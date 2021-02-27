#!/usr/bin/env python
import sys, json
import networkx as nx
from networkx.readwrite import json_graph

#g = nx.barabasi_albert_graph(1000, 3)
#g= nx.watts_strogatz_graph(500,20,0.2)
g= nx.connected_caveman_graph(15, 5)

nodes = g.nodes()


data = json_graph.node_link_data(g)

data['nodes'] = [ {"name": i} for i in range(len(data['nodes'])) ]

f = open(sys.argv[1], 'w')

f.write( json.dumps(data) )

f.close()


