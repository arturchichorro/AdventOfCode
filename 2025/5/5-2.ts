import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const firstSplit = data.split(/\r?\n\n/);
const ranges = firstSplit[0].split(/\r?\n/).map(r => r.split("-").map(Number));


