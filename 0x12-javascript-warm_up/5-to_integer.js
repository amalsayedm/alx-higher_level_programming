#!/usr/bin/node

let isnumber = parseInt(process.argv[2]);

if (isnumber) {
  isnumber = 'My number: ' + isnumber;
  console.log(isnumber);
} else {
  console.log('Not a number');
}
