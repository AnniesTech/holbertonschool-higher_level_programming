#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let cont = 0;
request(url, (err, reponse, body) => {
  if (err) {
    console.log(err);
  } else {
    const respo = JSON.parse(body);
    const results = respo.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          cont++;
        }
      }
    }
  }
  console.log(cont);
});
