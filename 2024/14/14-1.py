import re

t0_data = """p=2,4 v=2,-3"""

with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

def parse_input(input):
    return [tuple(int(value) for value in match) for match in re.findall(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", input)]

def move_robots(rows, cols, input, n):
    posvel = parse_input(input)

    result = []

    for pv in posvel:
        x, y, vx, vy = pv
        result.append(((x+vx * n) % cols, (y+vy * n) % rows))
    
    return result

def calc_safety_factor(rows, cols, input, n):

    positions = move_robots(rows, cols, input, n)

    q1, q2, q3, q4 = 0, 0, 0, 0

    midr = rows // 2
    midc = cols // 2

    for pos in positions:
        c, r = pos

        if c < midc and r < midr:
            q1 += 1
        elif c > midc and r < midr:
            q2 += 1
        elif c < midc and r > midr:
            q3 += 1
        elif c > midc and r > midr:
            q4 += 1
        
    print(q1, q2, q3, q4)
    return q1*q2*q3*q4
            
print(calc_safety_factor(103, 101, data, 100))



# def print_positions(input, n):
#     rows, cols, _ = parse_input(input)
#     pos = move_robots(input, n)

#     for i in range(rows):
#         row = ""
#         for j in range(cols):
#             if (j, i) in pos:
#                 row += " X"
#             else:
#                 row += " ."
#         print(row)

# print_positions(t_data, 100)