#!/usr/bin/node
const args = process.argv;
function factorials (x) {
  if (x === 0) {
    return 1;
  } else {
    return x * factorials(x - 1);
  }
}
if (isNaN(parseInt(args[2]))) {
  console.log(1);
} else {
  console.log(factorials(parseInt(args[2])));
}
