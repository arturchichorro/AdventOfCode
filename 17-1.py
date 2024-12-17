t_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

def parse_input(input):
    lines = input.splitlines()
    ra = int(lines[0].split(":")[1].strip())
    rb = int(lines[1].split(":")[1].strip())
    rc = int(lines[2].split(":")[1].strip())

    program = [int(x) for x in lines[4].split(":")[1].split(",")]

    return ra, rb, rc, program

print(parse_input(t_data))