with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

line = [int(c) for c in data.strip().split()]

def change_stone(digit):
    if digit == 0:
        return 1
    elif len(str(digit)) % 2 == 0:
      d_str = str(digit)
      mid = len(d_str) // 2
      part1, part2 = int(d_str[:mid]), int(d_str[mid:])
      return [part1, part2]
    else:
       return digit * 2024
    
for _ in range(25):
    new_line = []
    for num in line:
        result = change_stone(num)
        if isinstance(result, list):
            new_line.extend(result)
        else:
            new_line.append(result)
    line = new_line
   
print(len(line))