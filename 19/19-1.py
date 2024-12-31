with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

def parse_input(input):
    towels, goals = input.strip().split("\n\n")

    towels = [towel.strip() for towel in towels.split(",")]
    goals = goals.strip().split("\n")
    
    return towels, goals

def dfs(towels, target, curr):
    
    if len(target) == len(curr):
        return target == curr
    
    for towel in towels:
        new_curr = curr + towel
        if len(new_curr) <= len(target) and target.startswith(new_curr):
            if dfs(towels, target, new_curr):
                return True
    return False

towels, goals = parse_input(data)
print(towels)
print(goals)

count = 0
for goal in goals:
    if dfs(towels, goal, ""):
        count += 1
print(count)