import re
from functools import reduce

# Import data 
with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

# Solution 1 using re
do = True
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, t_data)
n_pairs = []

for s in matches:
    if s == "do()":
        do = True
        continue
    elif s == "don't()":
        do = False
        continue
    elif do:
        n = s[s.find("(") + 1:s.find(")")]
        n_pairs.append([int(x) for x in n.split(",")])

print(n_pairs)
print(sum(reduce(lambda x, y: x*y, pair) for pair in n_pairs))

# Solution 2 without using re
do = True
num_pairs = []

start = 0
while start < len(data):
    mul_start = data.find("mul(", start)
    do_start = data.find("do()", start)
    dont_start = data.find("don't()", start)

    if mul_start == -1 and do_start == -1 and dont_start == -1:
        break

    next_match_idx = min([i for i in [mul_start, do_start, dont_start] if i != -1])

    if next_match_idx == do_start:
        do = True
        start = do_start + 4
        continue
    if next_match_idx == dont_start:
        do = False
        start = dont_start + 7
        continue

    if next_match_idx == mul_start and do:
        end = data.find(")", mul_start)
        if end != -1:
            candidate = data[mul_start+4:end]

            if "," in candidate and all(part.strip().isdigit() for part in candidate.split(",")):
                num_pairs.append([int(x) for x in candidate.split(",")])
            start = mul_start + 5
        else:
            break
    elif not do:
        start = mul_start + 4

print(sum(reduce(lambda x, y: x*y, pair) for pair in num_pairs))