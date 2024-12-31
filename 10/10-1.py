with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

matrix = [[int(c) for c in line] for line in data.strip().split("\n")]

def find_zeros(m):
    result = []
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 0:
                result.append((r,c))
    
    return result

def dfs(m, x, y, target):
    if not (0 <= x < len(m) and 0 <= y < len(m[0])):
        return set()
    if m[x][y] != target:
        return set()
    if m[x][y] == 9:
        return {(x, y)}
    
    reachable = set()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        reachable.update(dfs(m, x + dx, y + dy, target + 1))
    
    return reachable


def score(m):
    zeros = find_zeros(m)
    soma = 0

    for r, c in zeros:
        reachable = dfs(m, r, c, 0)
        soma += len(reachable)
    
    return soma

print(score(matrix))