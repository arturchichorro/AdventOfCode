with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
def parse_input(input):
    towels, goals = input.strip().split("\n\n")

    towels = [towel.strip() for towel in towels.split(",")]
    goals = goals.strip().split("\n")

    print(len(towels), len(goals), len(goals[0]))
    
    return towels, goals

def dfs(towels, target, index, memo):
    
    if index == len(target):
        return 1
    
    if index in memo:
        return memo[index]

    ways = 0
    for towel in towels:
        if target.startswith(towel, index):
            ways += dfs(towels, target, index + len(towel), memo)
    memo[index] = ways

    return ways

towels, goals = parse_input(data)

count = 0
for goal in goals:
    memo = {}
    count += dfs(towels, goal, 0, memo)

print(count)