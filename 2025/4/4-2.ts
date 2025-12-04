import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/).map((l) => l.split(""));

const DIRECTIONS = [
    [0,1], [1,0], [1,1], [0, -1], 
    [-1, 0], [-1, -1], [1, -1], [-1, 1]
];
const rows = lines.length;
const cols = lines[0].length;

const inBounds = (row: number, col: number) => row >= 0 && row < rows && col >= 0 && col < cols;

const check = (r: number, c: number, matrix: String[][]) => {
    if (matrix[r][c] !== "@") return false;
    let count = 0
    for (const [dr, dc] of DIRECTIONS) {
        const nr = r + dr, nc = c + dc;
        if (!inBounds(nr, nc)) continue;
        if (matrix[nr][nc] === '@') count ++;
        if (count > 3) return false;
    }
    return true;
}

let res=0;
while (true) {
    let found = false;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (check(r, c, lines)) {
                lines[r][c] = "."
                res++;
                found = true;
            };
        }   
    }
    if (!found) break;
}

console.log(res);