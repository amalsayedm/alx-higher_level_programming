#!/usr/bin/node

const size = process.argv.length;

if (size <= 3) {
  console.log('0');
} else {
  const array = [];
  let i = 0;
  for (let x = 2; x < size; x++) {
    array[i] = parseInt(process.argv[x]);
    i++;
  }
  array.sort();
  console.log(array[array.length - 2]);
}
