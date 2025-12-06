import * as fs from "fs";

const ops: Record<string, (a: number, b: number) => number> = {
    "+": (a, b) => a + b,
    "*": (a, b) => a * b
}

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/);
const opLine = lines.pop()!;

const colWidths: number[] = [];
let count = 1;
for (let i = 1; i < opLine.length; i++) {
    const c = opLine[i];
    count += 1;
    if (c === "*" || c === "+") {
        colWidths.push(count - 2);
        count = 1;
    }
}
colWidths.push(count);

const operations = opLine.match(/\S/g)!;
const linesParsed = lines.map(line => {
    const parts = [];
    let s = 0;
    for (const width of colWidths) {
        parts.push(line.slice(s, s + width));
        s = s + width + 1;
    }
    return parts
});

const transposed = linesParsed[0].map((_, colIdx) => 
    linesParsed.map(row => row[colIdx]
));

let res = 0;
for (let i = 0; i < transposed.length; i++) {
    const line = transposed[i];
    const op = operations[i];
    const nums = [];
    for (let j = 0; j < colWidths[i]; j++) 
        nums.push(line.reduce((acc, l) => acc + l[j], "").trim());
    
    res += nums.map(Number).reduce((acc, n) => ops[op](acc, n)); 
}
console.log(res);
