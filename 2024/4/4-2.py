with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()


directions = [(-1,1), (1,1)]
total_x_mas = 0

matrix = [list(row) for row in data.strip().split("\n")]
rows, cols = len(matrix), len(matrix[0])

for i in range(rows):
    for j in range(cols):
        
        if matrix[i][j] == "A":

            valid = True

            for dir in directions:
                dir_x = i + dir[0]
                dir_y = j + dir[1]
                m_dir_x = i - dir[0]
                m_dir_y = j - dir[1]

                if dir_x < 0 or dir_x >= rows or dir_y < 0 or dir_y >= cols \
                or m_dir_x < 0 or m_dir_x >= rows or m_dir_y < 0 or m_dir_y >= cols:
                    valid = False
                    break

                p_diag = matrix[dir_x][dir_y]
                n_diag = matrix[m_dir_x][m_dir_y]

                if not ((p_diag == "M" and n_diag == "S") or (p_diag == "S" and n_diag == "M")):
                    valid = False
                    break
            
            if valid: total_x_mas += 1

print(total_x_mas)

