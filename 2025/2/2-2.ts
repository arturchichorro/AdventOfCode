import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const ranges = data.split(',').map((ele) => ele.split('-').map(Number));

const check = (s: string) => (s+s).slice(1,-1).includes(s);

let res1 = 0;
for (const arr of ranges) for (let i = arr[0]; i <= arr[1]; i++) if (check(String(i))) res1 += i
console.log(res1);

let res2 = 0;
ranges.forEach((range) => {
    for (let i = range[0]; i<= range[1]; i++) {
        if (check(String(i))) res2 += i;
    }
});
console.log(res2);

const res3 = ranges.flatMap(([a, b]) => Array.from({ length: b - a + 1 }, (_, i) => a + i))
    .filter((n) => check(String(n)))
    .reduce((n, acc) => n + acc, 0);

console.log(res3);