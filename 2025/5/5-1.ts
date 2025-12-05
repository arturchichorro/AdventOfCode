import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const firstSplit = data.split(/\r?\n\n/);
const ranges = firstSplit[0].split(/\r?\n/).map(r => r.split("-").map(Number));
const ingredients = firstSplit[1].split(/\r?\n/);

let res = 0;
for (const ing of ingredients) {
    for (const range of ranges) {
        if (Number(ing) >= range[0] && Number(ing) <= range[1]) {
            res += 1;
            break;
        } 
    }
}
console.log(res);