import time
start_time = time.time()

with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
equations = [[int(x) for x in line.replace(":", "").split()] for line in data.strip().split("\n")]

def dfs(eq, curr, idx, operation):
    if curr > eq[0]:
        return False
    if idx == len(eq):
         return curr == eq[0]
    
    if operation == "+":
        curr += eq[idx]
    elif operation == "*":
        curr *= eq[idx]
    else:
        curr = int(str(curr) + str(eq[idx]))
    
    return dfs(eq, curr, idx + 1, "+") or dfs(eq, curr, idx + 1, "*") or dfs(eq, curr, idx + 1, "|")

t_sum = 0
for equation in equations:
    if dfs(equation, equation[1], 2, "+") or dfs(equation, equation[1], 2, "*") or dfs(equation, equation[1], 2, "|"):
        t_sum += equation[0]

print(t_sum)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")