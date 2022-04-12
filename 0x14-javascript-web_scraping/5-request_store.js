#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[3];
const file = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(file, body, 'utf-8');
  }
});
