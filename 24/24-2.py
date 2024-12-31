with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
from collections import defaultdict

input = data

values = dict()
ops = []

for line in input.split("\n\n")[0].split("\n"):
    name, value = line.split(": ")
    values[name] = int(value)

for line in input.split("\n\n")[1].split("\n"):
    inp1, gate, inp2 = line.split(" ->")[0].split(" ")
    out = line.split("-> ")[1]
    ops.append((inp1, inp2, gate, out))

def work() -> int:
    global values
    missing = 0

    for (inp1, inp2, gate, out) in ops:
        if out in values: continue
        if inp1 not in values or inp2 not in values:
            missing += 1
            continue
            
        assert gate in ["AND", "OR", "XOR"], f"undefined gate {gate}"
        match gate:
            case "OR": values[out] = values[inp1] | values[inp2]
            case "AND": values[out] = values[inp1] & values[inp2]
            case "XOR": values[out] = values[inp1] ^ values[inp2]

    return missing

while work(): pass
output = 0
for k, v in values.items():
    if k[0] == "z": output |= v << int(k[1:])

print(output)

def get_path(wire: str) -> list:
    path = []
    for (inp1, inp2, gate, out) in ops:
        if out == wire:
            path.append((inp1, inp2, gate, out))
            path += get_path(inp1)
            path += get_path(inp2)

    return path

def highest_bit(n: int) -> int | None:
    if not n: return None
    bit = 0
    while n:
        n >>= 1
        bit += 1
    return bit-1

last_output = f"z{highest_bit(output)}"
print(f"highest bit is {last_output}")

usage = defaultdict(set)
errors = []

for (inp1, inp2, gate, _) in ops:
    usage[inp1].add(gate)
    usage[inp2].add(gate)

for (inp1, inp2, gate, out) in ops:
    if out == last_output:
        if inp1[0] == "x" or inp1[0] == "y" or inp2[0] == "x" or inp2[0] == "y" or gate != "OR":
            errors.append(out)
        continue

    if out == "z00":
        if sorted([inp1, inp2]) != ["x00", "y00"]: errors.append(out)
        if gate != "XOR": errors.append(out)
        continue

    if inp1 == "x00" or inp1 == "y00" or inp2 == "x00" or inp2 == "y00":
        if (inp1[0] == "x" and inp2[0] == "y") or (inp1[0] == "y" and inp2[0] == "x"):
            if gate != "XOR" and gate != "AND": errors.append(out)
        continue

    if gate == "XOR":
        if inp1[0] == "x" or inp1[0] == "y":
            if inp2[0] != "x" and inp2[0] != "y": errors.append(out)
            if out[0] == "z": errors.append(out)
            if "AND" not in usage[out] or "XOR" not in usage[out]:
                errors.append(out)
        elif out[0] != "z": errors.append(out)
    
    elif gate == "OR":
        if inp1[0] == "x" or inp1[0] == "y" or inp2[0] == "x" or inp2[0] == "y" or out[0] == "z":
            errors.append(out)
        if "AND" not in usage[out] or "XOR" not in usage[out]:
            errors.append(out)
    
    elif gate == "AND":
        if inp1[0] == "x" or inp1[0] == "y":
            if inp2[0] != "x" and inp2[0] != "y": errors.append(out)
        if "OR" not in usage[out]:
            errors.append(out)

errors = sorted(list(set(errors)))
assert len(errors) == 8, f"expected 8 values but got {len(errors)}"

for i in range(len(errors)):
    if i == len(errors)-1: print(errors[i])
    else: print(errors[i], end=",")