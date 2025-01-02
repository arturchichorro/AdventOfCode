import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

def parse_input(input):
    adjacency_list = defaultdict(set)

    print(len(input.splitlines()))

    for line in input.splitlines():
        a, b = line.split("-")
        adjacency_list[a].add(b)
        adjacency_list[b].add(a)
    
    return adjacency_list

adj_list = parse_input(data)

graph = nx.Graph(adj_list)

plt.figure(figsize=(10, 8), facecolor="#0c1810")

nx.draw(graph, with_labels=True, node_color='#4db36f', node_size=50, font_size=5)

plt.show()
