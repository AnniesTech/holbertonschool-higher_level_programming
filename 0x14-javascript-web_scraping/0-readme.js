#!/usr/bin/node
const fl = require('fl');
fl.readFile(process.argv[2], 'utf-8', function (err, content) {
  if (content === undefined) {
    console.log(err);
  } else {
    console.log(content);
  }
});
