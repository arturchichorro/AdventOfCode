import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/).map(line => line.split(""));

function findS(grid: string[][]) {
    for (let row = 0; row < grid.length; row++) {
        const col = grid[row].indexOf("S");
        if (col !== -1) return [ row, col ];
    }
    return null;
}

const rows = lines.length;
const cols = lines[0].length;

const inBounds = (row: number, col: number) => 
    row >= 0 && row < rows && col >= 0 && col < cols;

const start = findS(lines);
if (!start) throw new Error ("No S in grid");
const [sr, sc] = start;

const memo = new Map<string, number>();

function dfs(r: number, c: number): number {
    if (!inBounds(r, c)) {
        return 1;    
    }

    const key = `${r}-${c}`;
    if (memo.has(key)) return memo.get(key)!;

    const cell = lines[r][c];
    let result: number;
    if (cell === "^") {
        const left = dfs(r, c - 1);
        const right = dfs(r, c + 1);
        result = left + right;
    } else {
        result = dfs(r + 1, c);
    }
    memo.set(key, result);
    return result;
}

const timelines = dfs(sr + 1, sc);

console.log(timelines);