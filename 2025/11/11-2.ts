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

const memo = new Map<string, number>();
const dfs = (curr: string, hasDac: boolean, hasFft: boolean): number => {
    const key = `${curr}-${hasDac}-${hasFft}`;
    if (memo.has(key)) return memo.get(key)!;

    if (curr === "out") return (hasDac && hasFft) ? 1 : 0;

    const next = lines.get(curr);
    if (!next) return 0;

    let total = 0;
    for (const n of next) total += dfs(n, hasDac || n === "dac", hasFft || n === "fft");

    memo.set(key, total);
    return total;
};

console.log(dfs("svr", false, false));


