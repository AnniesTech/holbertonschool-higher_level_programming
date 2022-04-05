#!/usr/bin/node
function sorting (a, b) {
  return a - b;
}
const argslen = process.argv.length;
if (argslen === 2 || argslen === 3) {
  console.log('0');
} else {
  const array = [];
  for (let i = 2; i < argslen; i++) {
    array.push(process.argv[i]);
  }
  array.sort(sorting);
  console.log(array[array.length - 2]);
}
