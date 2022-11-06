#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = argv[2];
const endpoint = `${url}${id}`;

const people = url => {
  return new Promise((resolve) => {
    request(url, (err, response) => {
      if (!err) {
        const data = JSON.parse(response.body);
        const name = data.name;
        resolve(name);
      }
    });
  });
};

const printcharacters = async characters => {
  for (let i = 0; i < characters.length; i++) {
    const result = await people(characters[i]);
    console.log(result);
  }
};

request(endpoint, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const characters = data.characters;
    printcharacters(characters);
  }
});
