#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
fs.readFile(argv[2], 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
