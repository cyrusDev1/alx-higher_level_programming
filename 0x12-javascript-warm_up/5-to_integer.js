#!/usr/bin/node
const argv = process.argv;
const parse = parseInt(argv[2], 10);
if (isNaN(parse)) {
  console.log('Not a number');
} else {
  console.log(parse);
}
