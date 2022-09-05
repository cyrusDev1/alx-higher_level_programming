#!/usr/bin/node
const argv = process.argv;
const parse = parseInt(argv[2], 10);
if (isNaN(parse)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parse; i++) {
    console.log('X'.repeat(parse));
  }
}
