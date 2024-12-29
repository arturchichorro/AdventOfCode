t_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

data = """Register A: 63687530
Register B: 0
Register C: 0

Program: 2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0"""

import re

def run(program, regs):
    a, b, c = range(4, 7)
    ip = 0
    combo = [0, 1, 2, 3, *regs]
    while ip < len(program):
        opcode, operand = program[ip:ip + 2]
        if opcode == 0:
            combo[a] >>= combo[operand]
        elif opcode == 1:
            combo[b] ^= operand
        elif opcode == 2:
            combo[b] = combo[operand] % 8
        elif opcode == 3:
            if combo[a]:
                ip = operand - 2
        elif opcode == 4:
            combo[b] ^= combo[c]
        elif opcode == 5:
            yield combo[operand] % 8
        elif opcode == 6:
            combo[b] = combo[a] >> combo[operand]
        elif opcode == 7:
            combo[c] = combo[a] >> combo[operand]
        ip += 2

def expect(program, out, prev_a=0):
    if not out:
        return prev_a
    for a in range(1 << 10):
        if a >> 3 == prev_a & 127 and next(run(program, (a, 0, 0))) == out[-1]:
            ret = expect(program, out[:-1], (prev_a << 3) | (a % 8))
            if ret is not None:
                return ret

nums = list(map(int, re.findall(r'\d+', data)))
regs = nums[:3]
program = nums[3:]
print(','.join(map(str, run(program, regs))))
print(expect(program, program))