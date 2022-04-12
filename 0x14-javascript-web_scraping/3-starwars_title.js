#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/:id' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
