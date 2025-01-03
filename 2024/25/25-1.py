with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
# width = 5, height = 7, always
WIDTH = 5
HEIGHT = 7

def parse_input(input):
    blocks = input.strip().split("\n\n")
    
    keys, locks = [], []

    for block in blocks:
        lines = block.split("\n")

        # Is a lock
        if lines[0] == "#####":
            lock = []
            for x in range(WIDTH):
                for y in range(HEIGHT):
                    if lines[y][x] == ".":
                        lock.append(y)
                        break
            locks.append(lock)
        # Is a key
        else:
            key = []
            for x in range(WIDTH):
                for y in range(HEIGHT - 1, -1, -1):
                    if lines[y][x] == ".":
                        key.append(HEIGHT - y - 1)
                        break
            keys.append(key)       
    return locks, keys

def solve(locks, keys):

    result = 0

    for lock in locks:
        for key in keys:
            
            isValid = True

            for i in range(WIDTH):
                if lock[i] + key[i] > HEIGHT:
                    isValid = False
                    break

            if isValid: result += 1

    return result

locks, keys = parse_input(data)
print(solve(locks, keys))
