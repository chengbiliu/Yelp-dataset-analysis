import networkx as nx
import csv
import matplotlib.pyplot as plt

g=nx.Graph()

r=csv.reader(open('test1.csv', 'rb'))
for row in r:
    g.add_edge(row[0],row[1])
nx.draw(g)
plt.draw
plt.show()