with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

import re

def parse_input(input):
    machines = input.strip().split("\n\n")

    pattern = r"[+=](\d+)"
    result = []

    for machine in machines:
        nums = tuple(map(int, re.findall(pattern, machine)))
        result.append(nums)
    
    return result

def det_2x2(a, b, c, d):
    return a * d - b * c

def solve_part2(input):
    problems = parse_input(input)

    tokens = 0
    for prob in problems:
        x1, y1, x2, y2, x_goal, y_goal = prob
        x_goal += 10000000000000
        y_goal += 10000000000000

        det_A, det_A1, det_A2 = det_2x2(x1, x2, y1, y2), det_2x2(x_goal, x2, y_goal, y2), det_2x2(x1, x_goal, y1, y_goal)

        if det_A != 0 and det_A1 % det_A == 0 and det_A2 % det_A == 0:
            a = det_A1 // det_A
            b = det_A2 // det_A

            tokens += a*3 + b

    return tokens

print(solve_part2(data))
