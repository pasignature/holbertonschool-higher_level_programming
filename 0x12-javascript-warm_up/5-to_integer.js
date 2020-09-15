#!/usr/bin/node
// checks if arguments cam be converted into integer
'use strict';
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', process.argv[2]);
}
