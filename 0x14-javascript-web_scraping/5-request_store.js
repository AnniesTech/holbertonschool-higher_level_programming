#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const fs = require('fs');
const file = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(file, body, 'utf-8');
  }
});
