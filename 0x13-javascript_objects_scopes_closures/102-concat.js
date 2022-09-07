#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const textA = fs.readFileSync(argv[2], 'utf8', function (err) { if (err) { console.log(err); } });
const textB = fs.readFileSync(argv[3], 'utf8', function (err) { if (err) { console.log(err); } });
const textC = textA.concat(textB);
fs.writeFile(argv[4], textC, 'utf8', function (err) { if (err) { console.log(err); } });
console.log(textB);
