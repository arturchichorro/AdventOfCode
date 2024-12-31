import re
import time

with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

def parse_input(input_data):
    return [tuple(int(value) for value in match) 
            for match in re.findall(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", input_data)]

def update_positions(data, rows, cols):
    for i, (x, y, vx, vy) in enumerate(data):
        new_x = (x + vx) % cols
        new_y = (y + vy) % rows
        data[i] = (new_x, new_y, vx, vy)
    return data

def calculate_safety_factor(data, rows, cols):
    midr, midc = rows // 2, cols // 2
    q1 = q2 = q3 = q4 = 0

    for x, y, _, _ in data:
        if x < midc and y < midr:
            q1 += 1
        elif x >= midc and y < midr:
            q2 += 1
        elif x < midc and y >= midr:
            q3 += 1
        elif x >= midc and y >= midr:
            q4 += 1

    return q1 * q2 * q3 * q4

def print_grid(data, rows, cols, step, safety_factor):
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    
    for x, y, vx, vy in data:
        grid[y][x] = "#"
    
    print(f"Step: {step}, Safety Factor: {safety_factor}")
    
    for row in grid:
        print("".join(row))
    print("\n" + "=" * cols + "\n")

def simulate(data, rows, cols, max_steps=None):
    step = 0
    safety_factors = []

    while max_steps is None or step < max_steps:
        safety_factor = calculate_safety_factor(data, rows, cols)
        safety_factors.append((safety_factor, step))
        
        # print_grid(data, rows, cols, step, safety_factor)
        
        data = update_positions(data, rows, cols)
        
        step += 1

    safety_factors.sort(key=lambda x: x[0], reverse=True)
    
    print(safety_factors)

def print_step_n(data, rows, cols, n):
    for _ in range(n):
        data = update_positions(data, rows, cols)
    print_grid(data, rows, cols, n, 0)

objects = parse_input(data)
copy_objects = parse_input(data)

rows, cols = 103, 101

max_steps = 10000


simulate(objects, rows, cols, max_steps)
print_step_n(copy_objects, rows, cols, 7584)


# for _ in range(7500):
#     objects = update_positions(objects, rows, cols)

# for i in range(100):
#     objects = update_positions(objects, rows, cols)
#     print_grid(objects, rows, cols, i, 0)
