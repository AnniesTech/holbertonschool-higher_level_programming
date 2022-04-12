#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
request('http://swapi.co/api/films/' + episode + '/', function (err, response, body) {
  if (err == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
