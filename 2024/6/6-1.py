with open("input.txt", "r") as file:
    data = file.read()

with open("example1.txt", "r") as file:
    t_data = file.read()

with open("example2.txt", "r") as file:
    t_data_2 = file.read()

matrix = [list(line) for line in data.strip().split("\n")]

directions = [[-1,0], [0,1], [1,0], [0,-1]]

def find_start(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "^": 
                return [i,j]

def within_bounds(pos):
    rows, cols = len(matrix), len(matrix[0])
    return not (pos[0] < 0 or pos[0] >= rows or pos[1] < 0 or pos[1] >= cols)

def sum_arr(arr1, arr2):
    return [arr1[0] + arr2[0], arr1[1] + arr2[1]]

def read_matrix(matrix, pos):
    return matrix[pos[0]][pos[1]]

def assign_matrix(matrix, pos, val):
    matrix[pos[0]][pos[1]] = val

def print_matrix(matrix):
    for line in matrix:
        print(line)

def count_val_matrix(matrix, val):
    rows, cols = len(matrix), len(matrix[0])
    res = 0
    
    for i in range(rows):
        for j in range(cols):
            if read_matrix(matrix, [i,j]) == val: res += 1 
            
    return res

pos = find_start(matrix)

assign_matrix(matrix, pos, "X")
dir_idx = 0
while within_bounds(pos) and within_bounds(sum_arr(pos, directions[dir_idx])):
    
    next_pos = sum_arr(pos, directions[dir_idx])
    if within_bounds(next_pos) and read_matrix(matrix, next_pos) == "#":
        dir_idx = (dir_idx + 1) % 4

        while read_matrix(matrix, sum_arr(pos, directions[dir_idx])) == "#":
            dir_idx = (dir_idx + 1) % 4

        pos = sum_arr(pos, directions[dir_idx])

    else:
        pos = next_pos[:]
    
    assign_matrix(matrix, pos, "X")

print(count_val_matrix(matrix, "X"))


    