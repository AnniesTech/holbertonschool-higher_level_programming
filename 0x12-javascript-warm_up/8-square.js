#!/usr/bin/node
const args = process.argv;
if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < parseInt(args[2]); i++) {
    row = String(row + 'X');
  }
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log(row);
  }
}
