#!/usr/bin/node

'use strict';

// prints the number of arguments already printed
let narg = 0;

exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
