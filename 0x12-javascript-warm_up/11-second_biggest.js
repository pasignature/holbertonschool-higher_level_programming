#!/usr/bin/node
//finds the second largest number
'use strict';
const arr = process.argv.slice(2);
if (arr.length > 1) {
  arr.sort();
  
// assign secondMax with the second biggest number in the sorted array
let secondMax = arr[arr.length - 2];
}
console.log(secondMax);
