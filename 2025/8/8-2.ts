import * as fs from "fs";

type Coord = [number, number, number];
type DistAndIdxs = {
    dist: number,
    idx1: number,
    idx2: number
}

class DSU {
    private parent: number[];
    private size: number[];
    private numConnected: number;

    constructor(n: number) {
        this.parent = Array.from({ length: n }, (_, i) => i);
        this.size = Array.from({ length: n }, () => 1);
        this.numConnected = n;
    }

    public findRoot(i: number): number {
        if (this.parent[i] === i) return i;
        this.parent[i] = this.findRoot(this.parent[i]);
        return this.parent[i];
    }

    public unionSets(i: number, j: number): boolean {
        let rootI = this.findRoot(i);
        let rootJ = this.findRoot(j);

        if (rootI !== rootJ) {
            if (this.size[rootI] < this.size[rootJ]) {
                [rootI, rootJ] = [rootJ, rootI];
            }

            this.parent[rootJ] = rootI;
            this.size[rootI] += this.size[rootJ];
            this.numConnected--;
            return true;
        }
        return false;
    }

    public getSizeCopy(): number[] {
        return [...this.size]
    };

    public areAllConnected = (): boolean => this.numConnected === 1;
}

const data = fs.readFileSync("input.txt", "utf8");
const lines = data
    .split(/\r?\n/)
    .filter(line => line.trim() !== '')
    .map((line) => line.split(',')
        .map(Number)) as Coord[];

const calcDist = (l1: Coord, l2: Coord): number => {
    return Math.pow(l1[0] - l2[0],2) +
        Math.pow(l1[1] - l2[1], 2) +
        Math.pow(l1[2] - l2[2], 2)
}

const dists: DistAndIdxs[] = [];
for (let i=0; i<lines.length; i++) {
    for (let j=i+1; j<lines.length; j++) {
        dists.push({
            dist: calcDist(lines[i], lines[j]),
            idx1: i,
            idx2: j
        });
    }
}
dists.sort((a, b) => b.dist - a.dist);
const dsu = new DSU(lines.length);

let res: number;
while (true) {
    const curr = dists.pop();
    if (curr) {
        dsu.unionSets(curr.idx1, curr.idx2);
        if (dsu.areAllConnected()) {
            res = lines[curr.idx1][0] * lines[curr.idx2][0];
            break;
        }
    }
}
console.log(res);