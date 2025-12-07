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
const inBounds = (row: number, col: number) => row >= 0 && row < rows && col >= 0 && col < cols;
const [sr, sc] = findS(lines)!;
const splits = new Set<string>();

function dfs(grid: string[][], row: number, col: number) {
    if (grid[row][col] === "^") {
        if (splits.has(`${row}-${col}`)) return;
        if (inBounds(row, col - 1)) dfs(grid, row, col - 1);
        if (inBounds(row, col + 1)) dfs(grid, row, col + 1);
        splits.add(`${row}-${col}`)
        return;
    } else {
        grid[row][col] = "|";
        if (inBounds(row + 1, col)) dfs(grid, row + 1, col);
    }
}

dfs(lines, sr + 1, sc);

console.log(splits.size);