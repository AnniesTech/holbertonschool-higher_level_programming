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
    for (let i = 0; i < result.length; i++) {
      const characters = result[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          cont++;
        }
      }
    }
  }
  console.log(cont);
});
