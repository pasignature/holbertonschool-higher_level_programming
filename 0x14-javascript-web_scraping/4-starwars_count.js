#!/usr/bin/node

'use strict';

const requestMod = require('request');
const requesturl = process.argv[2];

requestMod(requesturl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let counter = 0;
    for (let index = 0; index < results.length; index++) {
      for (let char = 0; char < results[index].characters.length; char++) {
        if (results[index].characters[char].includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
