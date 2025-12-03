import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/);

const stringMax = (str: string, ignoreLast = false) => Math.max(...(ignoreLast ? str.slice(0, -1) : str).split("").map(Number));

let res = 0;
lines.forEach((line) => {
   const d1 = stringMax(line, true);
   const d2 = stringMax(line.slice(line.indexOf(String(d1)) + 1));

   res += 10*d1 + d2;
});
console.log(res)
