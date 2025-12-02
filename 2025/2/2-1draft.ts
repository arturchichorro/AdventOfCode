import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
// const lines = data.split(/\r?\n/);
// const input: number[] = [];



// const ex = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

const exArr = data.split(',');
const ranges = exArr.map((ele) => ele.split('-').map((e) => Number(e)));

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
