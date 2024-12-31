with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

rules, updates = data.strip().split("\n\n")

rules_dict = {}

for line in rules.strip().split("\n"):
    key, value = map(int, line.split("|"))
    if key in rules_dict:
        rules_dict[key].append(value)
    else:
        rules_dict[key] = [value]

updates_arr = [list(map(int, line.split(","))) for line in updates.strip().split("\n")]

sum_middles = 0

for j in range(len(updates_arr)):
    
    update = updates_arr[j]
    visited = []
    valid = True

    for i in range(len(update)):
   
        if any(e in visited for e in rules_dict.get(update[i], [])):
            valid = False
            break

        visited.append(update[i])
 
    if valid: 
        sum_middles += update[len(update) // 2]

print(sum_middles)