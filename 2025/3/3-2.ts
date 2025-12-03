import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/);

const stringMax = (str: string, ignoreN: number) => Math.max(...(ignoreN ? str.slice(0, -ignoreN) : str).split("").map(Number));

let res = 0;
for (let line of lines) {
    for (let i = 11; i >= 0; i--) {
        const d = stringMax(line, i);
        line = line.slice(line.indexOf(String(d)) + 1);
        res += d*Math.pow(10, i)
    }
};
console.log(res);
