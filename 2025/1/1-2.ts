import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/);
const input: number[] = [];

const M = 100
const trueMod = (n: number, m: number): number => ((n % m) + m) % m;

for (const line of lines) {
    const s1 = line.slice(0, 1);
    const s2 = line.slice(1);
    if (s1 === "R") input.push(Number(s2));
    else input.push(-Number(s2))
}

let curr = 50;
let result = 0;
for (const i of input) {
    const temp = curr + i;
    if (temp > 99) result += Math.floor(temp / M);
    else if (temp < 0) {
        result += Math.abs(Math.ceil(temp / M));
        if (curr !== 0) result += 1;
    } 
    else if (temp === 0) result += 1;
    curr = trueMod(temp, M);
}

console.log(result);
