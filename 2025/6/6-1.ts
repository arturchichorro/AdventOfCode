import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/).map(line => line.trim().split(/\s+/));

const transposed = lines[0].map((_, colIdx) => 
    lines.map(row => row[colIdx]
));

const ops: Record<string, (a: number, b: number) => number> = {
    "+": (a, b) => a + b,
    "*": (a, b) => a * b
}

const res = transposed.reduce((sum, line) => {
    const op = line.pop()!;
    return sum + line.map(Number).reduce(ops[op]);
}, 0);

console.log(res);


