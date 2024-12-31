with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

from collections import deque

def parse_input(input):
    vals, operations = input.strip().split("\n\n")

    val_dict = {}
    for line in vals.split("\n"):
        name, value = line.split(":")
        value = int(value)        
        val_dict[name] = value

    # e1, e2, operand, res
    oper = deque()
    for line in operations.split("\n"):
        op, result = line.split("->")
        result = result.strip()

        operand = ""
        if "AND" in op:
            operand = "AND"
        elif "XOR" in op:
            operand = "XOR"
        elif "OR" in op:
            operand = "OR"

        e1, e2 = op.split(operand)
        e1, e2 = e1.strip(), e2.strip()
        oper.append((e1, e2, operand, result))
    
    return val_dict, oper

def solve_part1(input):
    
    def z_bits_to_decimal(val_dict):
        z_keys = sorted([key for key in val_dict if key.startswith('z')], key = lambda k: int(k[1:]))
        binary_number = ''.join(str(val_dict[key]) for key in reversed(z_keys))
        return int(binary_number, 2)
        
    val_dict, oper = parse_input(input)

    while oper:
        e1, e2, operand, result = oper.popleft()

        if e1 in val_dict and e2 in val_dict:
            if operand == "AND":
                val_dict[result] = val_dict[e1] & val_dict[e2]
            elif operand == "XOR":
                val_dict[result] = val_dict[e1] ^ val_dict[e2]
            elif operand == "OR":
                val_dict[result] = val_dict[e1] | val_dict[e2]
        else:
            oper.append((e1, e2, operand, result))
        
    return z_bits_to_decimal(val_dict)

print(solve_part1(t_data))
print(solve_part1(data))



