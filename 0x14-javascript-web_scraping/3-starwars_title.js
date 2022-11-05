#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = argv[2];
const endpoint = `${url}${id}`;
request(endpoint, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
