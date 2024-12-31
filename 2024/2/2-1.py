def is_monotonic_with_step_constraint(arr):
    inc = dec = True
    prev = arr[0]

    for num in arr[1:]:
        diff = num - prev
        if diff > 3 or diff < -3 or diff == 0:
            return False
        if diff > 0:
            dec = False
        elif diff < 0:
            inc = False
        prev = num
    
    return inc or dec

with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

lines = data.strip().split("\n")
n_safe = 0

for line in lines:
    vals = [int(num) for num in line.split()]
    if is_monotonic_with_step_constraint(vals): n_safe += 1

print(n_safe)