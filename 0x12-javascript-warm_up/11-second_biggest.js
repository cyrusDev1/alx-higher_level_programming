#!/usr/bin/node
const argv = process.argv;
const copy = argv.slice(2);
if (copy.length <= 1) {
  console.log(0);
} else {
  copy.sort((a, b) => b - a);
  console.log(copy[1]);
}
