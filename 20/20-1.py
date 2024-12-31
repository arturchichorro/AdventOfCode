with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
from collections import deque

def parse_input(input):
    maze = input.strip().split("\n")

    height, width = len(maze), len(maze[0])
    start, end = (0,0), (0,0)

    for y in range(height):
        for x in range(width):
            if maze[y][x] == "S":
                start = (x, y)
            elif maze[y][x] == "E":
                end = (x, y)

    return maze, start, end

def solve_part1(input):
    maze, start, end = parse_input(input)
    height, width = len(maze), len(maze[0])

    queue = deque([(*start, 0, dict())])
    while queue:
        x, y, time, visited = queue.popleft()
        visited[(x, y)] = time

        if (x, y) == end:
            break

        for i, j in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if (i in range(height) and j in range(width) and (i, j) not in visited and maze[j][i] != "#"):
                queue.append((i, j, time + 1, visited.copy()))

    cheats = 0
    for (x, y), t1 in visited.items():
        for i, j in [(x+2, y), (x-2, y), (x, y-2), (x, y+2)]:
            if visited.get((i, j), 0) - t1 >= 102:
                cheats += 1
        
    return cheats

print(solve_part1(data))