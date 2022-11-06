#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    console.log(data.films.length);
  }
});
