with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

def parse_input(input):
    lines = input.splitlines()
    
    register = {
        'A': int(lines[0].split(":")[1].strip()),
        'B': int(lines[1].split(":")[1].strip()), 
        'C': int(lines[2].split(":")[1].strip())
    }

    program = [int(x) for x in lines[4].split(":")[1].split(",")]

    return register, program

def combo(operand, register):
    if operand == 4:
        return register['A']
    if operand == 5:
        return register['B']
    if operand == 6:
        return register['C']
    return operand

def solve_part1(input):
    register, program = parse_input(input)
    
    i = 0
    out = []
    while i < len(program):
        opcode, operand = program[i:i+2]
        match opcode:
            case 0:
                register['A'] >>= combo(operand, register)
            case 1:
                register['B'] ^= operand
            case 2:
                register['B'] = combo(operand, register) % 8
            case 3:
                if register['A']:
                    i = operand - 2
            case 4:
                register['B'] ^= register['C']
            case 5:
                out.append(combo(operand, register) % 8)
            case 6:
                register['B'] = register['A'] >> combo(operand, register)
            case 7:
                register['C'] = register['A'] >> combo(operand, register)
        i += 2
    
    return ",".join(str(i) for i in out)
                

print(solve_part1(data))