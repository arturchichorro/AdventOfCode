with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
from collections import defaultdict

def parse_input(input):
    adjacency_list = defaultdict(set)
    for line in input.splitlines():
        a, b = line.split("-")
        adjacency_list[a].add(b)
        adjacency_list[b].add(a)
    
    return adjacency_list

def find_triple_connections(adj_list):
    triples = set()

    for node in adj_list:
        neighbors = adj_list[node]

        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 < neighbor2 and neighbor2 in adj_list[neighbor1]:
                    triple = tuple(sorted([node, neighbor1, neighbor2]))
                    triples.add(triple)

    return triples
        
def triple_contains_starting_t(triple):
    for e in triple:
        if e.startswith("t"):
            return True
        
    return False

def solve_part1(input):
    adj_list = parse_input(input)
    triples = find_triple_connections(adj_list)
    
    count = 0
    for triple in triples:
        if triple_contains_starting_t(triple): count += 1
    
    return count

print(solve_part1(data))