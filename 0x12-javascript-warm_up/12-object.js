#!/usr/bin/node
// changes value of an object
'use strict';
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
