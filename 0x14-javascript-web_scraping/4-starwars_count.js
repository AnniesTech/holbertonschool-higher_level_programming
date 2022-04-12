#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, reponse, body) => {
  if (err) {
    console.log(err);
  } else {
    let cont = 0;
    const respo = JSON.parse(body);
    const result = respo.results;
    for (const i in result) {
      const characters = result[i].characters;
      for (const chars in characters) {
        if (characters[j].includes('18')) {
          cont++;
        }
      }
    }
  }
  console.log(cont);
});
