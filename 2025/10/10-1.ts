import * as fs from "fs";

type dbj = {
    diagram: string,
    buttons: string[],
    joltage: string
}

const data = fs.readFileSync("input.txt", "utf8");
const lines: dbj[] = data.split(/\r?\n/).map(line => {
    const diagram = line.match(/\[(.*?)\]/)![1]; 
    const buttons = [...line.matchAll(/\((.*?)\)/g)].map(match => match[1]);
    const joltage = line.match(/\{(.*?)\}/)![1];

    return {
        diagram,
        buttons,
        joltage
    }
});

const diagramToMask = (diagram: string): number => {
    let mask = 0;
    for (let i = 0; i < diagram.length; i++) {
        if (diagram[i] === '#') mask |= (1 << i);
    }
    return mask;
}

const buttonToMask = (button: string): number =>
    button.split(',')
        .reduce((mask, idx) => mask | (1 << parseInt(idx)), 0);

const bfs = (target: string, buttons: string[]): number => {
    const targetMask = diagramToMask(target);
    const buttonMasks = buttons.map(buttonToMask);
    const len = target.length; 
    
    const start = 0;
    if (start === targetMask) return 0;

    const queue: [number, number][] = [[start, 0]];
    const visited = new Uint8Array(1 << len);
    visited[start] = 1;

    let head = 0;
    while (head < queue.length) {
        const [curr, dist] = queue[head++];

        for (const bMask of buttonMasks) {
            const next = curr ^ bMask;
            if (next === targetMask) return dist + 1;

            if (!visited[next]) {
                visited[next] = 1;
                queue.push([next, dist + 1]);
            }
        }
    }
    return -1;
}

let res = 0;
for (const line of lines) res += bfs(line.diagram, line.buttons);
console.log(res);