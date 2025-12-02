import * as fs from "fs";

const data = fs.readFileSync("input.txt", "utf8");

const exArr = data.split(',');
const ranges = exArr.map((ele) => ele.split('-').map(Number));

const checkRepetition = (s: string) => (s+s).slice(1, -1).includes(s);

let result = 0;
for (const arr of ranges) for (let i = arr[0]; i <= arr[1]; i++) if (checkRepetition(String(i))) result += i

console.log(fs.readFileSync('input.txt','utf8').split(',').flatMap(r=>{const [a,b]=r.split('-').map(Number);return Array.from({length:b-a+1},(_,i)=>a+i)}).reduce((sum,i)=>{const s=String(i);return sum + ((s+s).slice(1,-1).includes(s) ? i : 0)},0));

