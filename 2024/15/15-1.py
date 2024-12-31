with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

def parse_input(input):
    m, instructions = input.strip().split("\n\n")
    
    maze = [[c for c in line] for line in m.strip().split()]
    
    return maze, instructions

def print_maze(maze):
    for row in maze:
        print("".join(f"{e:3}" for e in row))
        
def move_in_maze(maze, dir, x, y):
    # dir is [1,0], [0,1], [-1, 0] or [0, -1]
    # x, y is current location

    new_x, new_y = x + dir[0], y + dir[1]
    if maze[new_x][new_y] == ".":
        maze[x][y] = "."
        maze[new_x][new_y] = "@"
        return maze, new_x, new_y
    elif maze[new_x][new_y] == "#":
        return maze, x, y
  
    sx, sy = 0, 0
    while maze[new_x][new_y] == "O":
        new_x, new_y = new_x + dir[0], new_y + dir[1]

        if maze[new_x][new_y] == "#":
            return maze, x, y
        elif maze[new_x][new_y] == ".":
            sx, sy = new_x, new_y

    while True:
        prev_x, prev_y = sx - dir[0], sy - dir[1]

        if maze[prev_x][prev_y] == "O":
            maze[sx][sy] = "O"
            maze[prev_x][prev_y] = "."
        elif maze[prev_x][prev_y] == "@":
            maze[sx][sy] = "@"
            maze[prev_x][prev_y] = "."
            break
        
        sx, sy = prev_x, prev_y
    
    return maze, x + dir[0], y + dir[1]

def calc_gps_coordinates(maze):
    res = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "O":
                res += i*100 + j
    return res


def simulate(maze, instructions):
    x, y = 0, 0
    found = False
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "@":
                x, y = i, j
                found = True
                break
        if found: break
    
    for i in instructions:
        if i == "^":
            maze, x, y = move_in_maze(maze, [-1, 0], x, y)
        elif i == ">":
            maze, x, y = move_in_maze(maze, [0, 1], x, y)
        elif i == "<":
            maze, x, y = move_in_maze(maze, [0, -1], x, y)
        elif i == "v":
            maze, x, y = move_in_maze(maze, [1, 0], x , y)

    return calc_gps_coordinates(maze)

maze, instructions = parse_input(data)
print(simulate(maze, instructions))

