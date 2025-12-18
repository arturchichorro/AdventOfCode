import * as fs from "fs";

type instruction = {
    grid: number,
    amounts: number[]
}

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n\n/);

const instructions: instruction[] = lines.pop()!.split(/\r?\n/)
    .map(i => {
        const [grid, amounts] = i.split(':');

        return {
            grid: grid.split("x").map(Number).reduce((acc, c) => acc * c, 1),
            amounts: amounts.trim().split(" ").map(Number)
        }
    })

const gifts: number[] = lines.map(line => line
    .split(/\r?\n/)
    .slice(1))
    .map((line) => line.join('').split("#").length - 1)
    
const def_too_small = (inst: instruction): boolean => {
    const occupied = inst.amounts
        .map((val, idx) => val * gifts[idx])
        .reduce((acc, curr) => acc + curr, 0);
    return inst.grid < occupied;
}

let res = instructions.length;
for (const inst of instructions)
    if (def_too_small(inst)) res--;
console.log(res);

