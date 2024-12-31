import re
from functools import reduce
 
with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

# Solution 1 using re
pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, data)
n_pairs = []

for s in matches:
    n = s[s.find("(") + 1:s.find(")")]
    n_pairs.append([int(x) for x in n.split(",")])

print(sum(reduce(lambda x, y: x*y, pair) for pair in n_pairs))

# Solution 2 not using re
num_pairs = []

start = 0
while (start := data.find("mul(", start)) != -1:
    end = data.find(")", start)
    if end != -1:
        candidate = data[start+4:end]

        if "," in candidate and all(part.strip().isdigit() for part in candidate.split(",")):
            # print(candidate.split(","))
            num_pairs.append([int(x) for x in candidate.split(",")])
        
        start = start + 4
    else:
        break

print(sum(reduce(lambda x, y: x*y, pair) for pair in num_pairs))