#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];
request(url, (err, response, body) => {
  if (!err) {
    fs.writeFile(argv[3], body, 'utf8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
