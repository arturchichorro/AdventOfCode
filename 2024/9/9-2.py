with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

arr = [int(c) for c in data]

def move_files(l):
    files, spaces = dict(), []
    pos = 0
    for i, n in enumerate(l):
        if i % 2:
            spaces.append((pos, n))
        else:
            files[i // 2] = (pos, n)
        pos += n
    
    for id, (file_pos, file_size) in reversed(files.items()):
        for i, (space_pos, space_size) in enumerate(spaces):
            if space_pos >= file_pos: break
            if file_size > space_size: continue

            files[id] = (space_pos, file_size)
            new_space_size = space_size - file_size

            if new_space_size == 0:
                spaces.pop(i)
            else:
                spaces[i] = (space_pos + file_size, new_space_size)
            break
    
    return sum(sum(id * n for n in range(l, l + s)) for id, (l, s) in files.items())

print(move_files(arr))