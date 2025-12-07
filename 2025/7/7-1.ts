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

const splits = new Set<string>();

function dfs(r: number, c: number) {
    const cell = lines[r][c];

    if (cell === "^") {
        const key = `${r}-${c}`;
        if (splits.has(key)) return;

        if (inBounds(r, c - 1)) dfs(r, c - 1);
        if (inBounds(r, c + 1)) dfs(r, c + 1);
        
        splits.add(key);
        return;
    } 
    
    if (cell !== "|") lines[r][c] = "|";
    if (inBounds(r + 1, c)) dfs(r + 1, c);
}

dfs(sr + 1, sc);

console.log(splits.size);