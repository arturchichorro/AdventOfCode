data="""965842 9159 3372473 311 0 6 86213 48"""

t_data = """0 1 10 99 999"""

t_data_2 = """125 17"""

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