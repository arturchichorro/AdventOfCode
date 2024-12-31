with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

directions = [(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]
total_xmas = 0

word = "XMAS"

matrix = [list(row) for row in data.split("\n")]
rows, cols = len(matrix), len(matrix[0])

for i in range(rows):
    for j in range(cols):

        if matrix[i][j] == "X":
            for dir in directions:

                current = "X"
                valid = True

                for k in range(1, len(word)):
                    new_x = i + k*dir[0]
                    new_y = j + k*dir[1]

                    if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                        valid = False
                        break

                    current += matrix[new_x][new_y]
                    
                    if not word.startswith(current):
                        valid = False
                        break
                
                if valid and current == word:
                    total_xmas += 1

print(total_xmas)




