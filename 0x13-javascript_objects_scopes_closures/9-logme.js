#!/usr/bin/node

'use strict';

// prints the number of arguments already printed
const counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
