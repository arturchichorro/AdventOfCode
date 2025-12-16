import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");
const lines = new Map<string, string[]>(
    data.split(/\r?\n/)
        .filter(line => line.trim())
        .map(line => {
            const [key, val] = line.split(":").map(el => el.trim());
            return [key, val.split(/\s+/)];
        })
);

const dfs = (curr: string, visited: Set<string>) => {
    if (visited.has(curr)) return 0;
    if (curr === "out") return 1;
    
    const next = lines.get(curr);
    if (!next) return 0;

    visited.add(curr);

    let total = 0;
    for (const n of next) {
        total += dfs(n, visited);
    };

    visited.delete(curr);

    return total;
}

const vis = new Set<string>;
console.log(dfs("you", vis));


