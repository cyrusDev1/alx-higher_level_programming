#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
fs.writeFile(argv[2], argv[3], 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
