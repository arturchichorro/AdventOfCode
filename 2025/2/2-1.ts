import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const ranges = data.split(',').map((ele) => ele.split('-').map(Number));

let result = 0;
for (const arr of ranges) {
    for (let e = arr[0]; e<= arr[1]; e++) {
        const i = String(e);
        const half = Math.floor(i.length / 2);
        const s1 = i.slice(0, half);
        const s2 = i.slice(half);
        if (s1 === s2) result += e;
    }
}

console.log(result);
