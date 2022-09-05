#!/usr/bin/node
const { argv } = require('node:process');
const arg = argv.length;
switch (arg) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
    break;
}
