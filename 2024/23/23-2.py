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

def bron_kerbosch(R, P, X, adj_list):
    if not P and not X:
        return [R]
    
    cliques = []
    for v in P.copy():
        P_v = P & adj_list[v]
        X_v = X & adj_list[v]

        cliques.extend(bron_kerbosch(R | {v}, P_v, X_v, adj_list))
        P.remove(v)
        X.add(v)
    return cliques

def find_largest_clique(adj_list):
    R, P, X = set(), set(list(adj_list.keys())), set()
    return max(bron_kerbosch(R, P, X, adj_list), key = len)

def solve_part2(input):
    return ",".join(sorted(find_largest_clique(parse_input(input))))

print(solve_part2(data))