# Expected 64
t0_data = """AAAA
AAAA
AAAA
AAAA"""

# Expected 80
t1_data = """AAAA
BBCD
BBCC
EEEC"""

# Expected 236
t2_data = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

# Expected 368
t3_data = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

with open("input.txt", "r") as file:
    data = file.read()

def get_corners(matrix, x, y):
        NW, W, SW, N, S, NE, E, SE = [
            is_same(matrix, x+dx, y+dy, matrix[x][y])
            for dx in range(-1, 2) 
            for dy in range(-1, 2) 
            if dx or dy
        ]
        return sum([
            N and W and not NW, 
            N and E and not NE, 
            S and W and not SW, 
            S and E and not SE, 
            not (N or W),
            not (N or E),
            not (S or W),
            not (S or E)
        ])
    
def is_same(matrix, x, y, type):
    return (
        x in range(len(matrix)) and 
        y in range(len(matrix[0])) and 
        matrix[x][y] == type)

def find_area_and_corners(matrix, x, y, visited):
    type = matrix[x][y]
    stack = [(x, y)]
    a = 0
    c = 0

    visited.add((x,y))

    while stack:
        x, y = stack.pop()
        a += 1
        c += get_corners(matrix, x, y)

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])):
                continue
            elif matrix[nx][ny] != type:
                continue
            elif (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx,ny))
    
    return a, c

def calc_cost(matrix):
    visited = set()
    result = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if (x, y) not in visited:
                a, s = find_area_and_corners(matrix, x, y, visited)
                result += a * s

    return result

matrix = [list(line) for line in data.strip().split("\n")]
print(calc_cost(matrix))