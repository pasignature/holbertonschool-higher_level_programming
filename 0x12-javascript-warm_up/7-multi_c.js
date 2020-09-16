#!/usr/bin/node
// print C is fun by number of passed in argument
'use strict';
const args = process.argv[2];
let count = 0;
if (isNaN(args)) {
  console.log('Missing number of occurrences');
}
while (count < args) {
  console.log('C is fun');
  count++;
}
