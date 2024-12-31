with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
matrix = [list(line) for line in data.strip().split("\n")]

rows, cols = len(matrix), len(matrix[0])

antenna_pos_dict = {}
antinode_positions = set()

for row in range(rows):
    for col in range(cols):
        char = matrix[row][col]
        if char.isalnum():
            if char not in antenna_pos_dict:
                antenna_pos_dict[char] = []
            antenna_pos_dict[char].append((row, col))


def subtrack_tuple(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1])

def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

for char, positions in antenna_pos_dict.items():
    
    if len(positions) > 1:
        for i in range(len(positions)):
            antinode_positions.add(positions[i])

    for i in range(len(positions)):
        for j in range(len(positions)):
            

            if i != j:
                dist = subtrack_tuple(positions[j], positions[i])

                prev_node =  subtrack_tuple(positions[i], dist)
                while prev_node[0] >= 0 and prev_node[0] < rows and prev_node[1] >= 0 and prev_node[1] < cols:
                    antinode_positions.add(prev_node)
                    prev_node = subtrack_tuple(prev_node, dist)

                after_node = add_tuple(positions[j], dist)
                while after_node[0] >= 0 and after_node[0] < rows and after_node[1] >= 0 and after_node[1] < cols:
                    antinode_positions.add(after_node)
                    after_node = add_tuple(after_node, dist)


print(len(antinode_positions))