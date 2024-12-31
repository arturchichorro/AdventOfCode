with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

more_t_data = "12345"

# copy = more_t_data.strip()
# copy = t_data.strip()
copy = data.strip()


start, end = 0, 0
start_id, end_id = 0, 0
if len(copy) % 2 == 1:
    end = len(copy) - 1
    end_id = len(copy) // 2
else:
    end = len(copy) - 2
    end_id = len(copy) // 2 - 1

end_block = int(copy[end])
sum = 0
mult = 0
space = 0

assigned = False

operations = []

while start < end:
    start_block = int(copy[start])

    space = space + int(copy[start+1])
    
    while start_block > 0:
        operations.append(start_id)
        sum += start_id * mult
        mult += 1
        start_block -= 1
    start_id += 1

    while space > 0 and start < end:
        assigned = False
        if end_block > 0:
            operations.append(end_id)
            sum += end_id * mult
            mult += 1
            end_block -= 1
            space -= 1
        
        if end_block == 0:
            end_id -= 1
            end -= 2
            end_block = int(copy[end])
            assigned = True

    start += 2
    if end <= start and not assigned:
        while end_block > 0:
            operations.append(end_id)
            sum += end_id * mult
            mult += 1
            end_block -= 1

print(sum)


# ex_res = "0099811188827773336446555566"
# print("operations: ", "".join(map(str, operations)))
# print("ex_resssss: ", ex_res)

# print(len(copy))