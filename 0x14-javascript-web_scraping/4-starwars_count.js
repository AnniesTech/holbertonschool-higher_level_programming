#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, reponse, body) => {
  if (err) {
    console.log(err);
  } else {
    let cont = 0;
    const result = JSON.parse(body).results;
    for (const i in result) {
      const character = result[i].characters;
      for (const i in character) {
        if (character[i].includes('18')) {
          cont++;
        }
      }
    }
  }
  console.log(cont);
});
