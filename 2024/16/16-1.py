import heapq

with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

def parse_input(input):
    maze = [list(line) for line in input.strip().split("\n")]
    start, end = None, None

    width, height = len(maze[0]), len(maze)

    for y in range(height):
        for x in range(width):
            if maze[y][x] == "S":
                start = (x, y)
            if maze[y][x] == "E":
                end = (x, y)
    
    return maze, start, end

def dijkstra(maze, start, end):

    width, height = len(maze[0]), len(maze)
    
    # East, South, West, North
    directions = [(1,0), (0,1), (-1, 0), (0, -1)]

    # Start facing East
    pq = [(0, start[0], start[1], 0)] 
    visited = set()

    while pq:
        score, x, y, facing = heapq.heappop(pq)

        if (x, y) == end:
            return score
        
        if (x, y, facing) in visited:
            continue
        visited.add((x, y, facing))

        dx, dy = directions[facing]
        nx, ny = x + dx, y + dy

        if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] != "#":
            heapq.heappush(pq, (score + 1, nx, ny, facing))
        
        left_facing = (facing - 1) % 4
        heapq.heappush(pq, (score + 1000, x, y, left_facing))
        right_facing = (facing + 1) % 4
        heapq.heappush(pq, (score + 1000, x, y, right_facing))
    
    return float('inf')

maze, start, end = parse_input(data)
print(dijkstra(maze, start, end))
