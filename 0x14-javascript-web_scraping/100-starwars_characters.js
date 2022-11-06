#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = argv[2];
const endpoint = `${url}${id}`;

request(endpoint, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach(url => {
      request(url, (err, response, body) => {
        if (!err) {
          const data = JSON.parse(body);
          const name = data.name;
          console.log(name);
        }
      });
    });
  }
});
