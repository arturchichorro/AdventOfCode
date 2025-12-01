"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var data = fs.readFileSync("input.txt", "utf8");
var lines = data.split(/\r?\n/);
for (var _i = 0, lines_1 = lines; _i < lines_1.length; _i++) {
    var line = lines_1[_i];
    console.log(line);
}
