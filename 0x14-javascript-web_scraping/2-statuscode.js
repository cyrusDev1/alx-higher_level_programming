#!/usr/bin/node
const request = require('request');
const argv = process.argv;
request(argv[2], (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
