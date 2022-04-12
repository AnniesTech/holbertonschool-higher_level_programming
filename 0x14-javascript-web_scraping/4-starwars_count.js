#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let cont = 0;
    const result = JSON.parse(body).results;
    for (const i in result) {
      const character = result[i].characters;
      for (const j in character) {
        if (character[j].includes('18')) {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
