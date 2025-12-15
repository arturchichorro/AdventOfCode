import * as fs from "fs";

type Coord = [number, number];
const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/).map(line => line.split(',').map(Number) as Coord);

const calcArea = (a1: Coord, a2: Coord) => 
    Math.abs(a1[0] - a2[0] + 1) * Math.abs(a1[1] - a2[1] + 1);  

let maxArea = 0;
for (const l1 of lines) {
    for (const l2 of lines) {
        if (l1 !== l2) maxArea = Math.max(maxArea, calcArea(l1, l2));
    }
}

console.log(maxArea);

