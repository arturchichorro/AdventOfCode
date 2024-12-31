t_data = """AAAA
BBCD
BBCC
EEEC"""

t1_data = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

t2_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

with open("input.txt", "r") as file:
    data = file.read()

def find_area_and_perimeter(matrix, x, y, visited):
    type = matrix[x][y]
    stack = [(x, y)]
    a = 0
    p = 0

    visited.add((x,y))

    while stack:
        x, y = stack.pop()
        a += 1

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])):
                p += 1
            elif matrix[nx][ny] != type:
                p += 1
            elif (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx,ny))
    
    return a, p

def calc_cost(matrix):
    visited = set()
    result = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if (x, y) not in visited:
                a, p = find_area_and_perimeter(matrix, x, y, visited)
                result += a * p

    return result

matrix = [list(line) for line in data.strip().split("\n")]
print(calc_cost(matrix))