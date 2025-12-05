import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const firstSplit = data.split(/\r?\n\n/);
const ranges = firstSplit[0].split(/\r?\n/).map(r => r.split("-").map(Number)).sort((a,b) => a[0] - b[0]);
const merged: [number, number][] = [];

for (const [start, end] of ranges) {
    if (merged.length === 0) {
        merged.push([start, end]);
        continue;
    }

    const last = merged[merged.length - 1];
    if (start <= last[1]) last[1] = Math.max(last[1], end);
    else merged.push([start,end]);
}

const res = merged.reduce((acc, [a, b]) => acc + b - a + 1, 0);
console.log(res);