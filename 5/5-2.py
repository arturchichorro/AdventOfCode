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

invalid_idxs = []
for i in range(len(updates_arr)):
    
    update = updates_arr[i]
    visited = []

    for j in range(len(update)):
   
        if any(e in visited for e in rules_dict.get(update[j], [])):
            invalid_idxs.append(i)
            break

        visited.append(update[j])

# Rules são o dict
def bubble_sort_rules(arr, rules):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] in rules.get(arr[j+1], []):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

middle_sum = 0
for k in range(len(invalid_idxs)):
    inv_update = updates_arr[invalid_idxs[k]]

    bubble_sort_rules(inv_update, rules_dict)
    middle_sum += inv_update[len(inv_update) // 2]

print(middle_sum)


