with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
import heapq

def parse_input(input):
    return [(int(x), int(y)) for line in input.strip().split("\n") for x, y in [line.split(",")]]

def print_obstacles(input, fell, width, height):
    corruptions = parse_input(input)[:fell]

    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) in corruptions:
                line += " # "
            else:
                line += " . "
        print(line)


def n_steps(input, fell, width, height):

    corruptions = parse_input(input)[:fell]
    end = (width-1, height-1)

    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    # score, x, y
    pq = [(0, 0, 0)]
    visited = set()

    while pq:
        score, x, y = heapq.heappop(pq)

        if (x, y) == end:
            return score
        
        if (x, y) in visited:
            continue
        visited.add((x,y))

        for dir in directions:
            dx, dy = dir
            nx, ny = x + dx, y + dy

            if 0 <= ny < height and 0 <= nx < width and (x, y) not in corruptions:
                heapq.heappush(pq, (score + 1, nx, ny))
        
    return -1

def search(input, width, height):
    corruptions = parse_input(input)
    max = len(corruptions)

    start, end = 0, max - 1

    while start < end:
        mid = (start + end) // 2
        if n_steps(input, mid, width, height) == -1:
            end = mid
        else:
            start = mid + 1
    
    if n_steps(input, start, width, height) == -1:
        return start, corruptions[start-1]
    else:
        return -1, None


def brute_search(input, width, height):
    corruptions = parse_input(input)

    for i in range(len(corruptions)):
        if n_steps(input, i, width, height) == -1:
            return i, corruptions[i-1]
    
    return -1, None

print(search(data, 71, 71))
