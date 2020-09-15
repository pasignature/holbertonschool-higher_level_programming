#!/usr/bin/node
//passes arguments and prints first argument
'use strict';
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
