import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/);
const input: number[] = [];

for (const line of lines) {
    const s1 = line.slice(0, 1);
    const s2 = line.slice(1);
    if (s1 === "R") input.push(Number(s2));
    else input.push(-Number(s2))
}

let curr = 50;
let result = 0;
for (const i of input) {
    curr = (curr += i) % 100;
    if (curr === 0) result += 1;
}

console.log(result);