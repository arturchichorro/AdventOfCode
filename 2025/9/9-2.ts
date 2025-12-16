import * as fs from "fs";

type Coord = [number, number];

type Area = {
    area: number,
    n1: Coord,
    n2: Coord
}

const data = fs.readFileSync("input.txt", "utf8");
const lines = data.split(/\r?\n/).map(line => line.split(',').map(Number) as Coord);
const len = lines.length;

const calcArea = (a1: Coord, a2: Coord) => 
    (Math.abs(a1[0] - a2[0]) + 1) * (Math.abs(a1[1] - a2[1]) + 1);  

const areas: Area[] = [];
for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
        areas.push({
            area: calcArea(lines[i], lines[j]),
            n1: lines[i],
            n2: lines[j]
        })
    }
}

areas.sort((a, b) => b.area - a.area);

const edges: { n1: Coord, n2: Coord }[] = lines.map((val, idx) => {
    const next = lines[(idx + 1) % len];
    return {
        n1: [val[0], val[1]],
        n2: [next[0], next[1]]
    }
})

const intersection = (a1: number, b1: number, a2: number, b2: number): boolean =>
    !(a1 <= a2 && a1 <= b2 && b1 <= a2 && b1 <= b2) &&
    !(a1 >= a2 && a1 >= b2 && b1 >= a2 && b1 >= b2);

const res: number = areas.find((area) =>
    !edges.some(
        (edge) =>
            intersection(edge.n1[1], edge.n2[1], area.n1[1], area.n2[1]) &&
            intersection(edge.n1[0], edge.n2[0], area.n1[0], area.n2[0])
    )
)!.area;

console.log(res);













