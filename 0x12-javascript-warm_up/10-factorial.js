#!/usr/bin/node
const argv = process.argv;
const parse = parseInt(argv[2], 10);

function factorial (n) {
  if (n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

if (isNaN(parse)) {
  console.log('1');
} else {
  const fact = factorial(parse);
  console.log(fact);
}
