#!/usr/bin/node

'use strict';

const requestMod = require('request');
const requestUrl = process.argv[2];

requestMod(requestUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);
    const dic = {};
    for (let index = 0; index < result.length; index++) {
      if (result[index].completed === true) {
        if (dic[result[index].userId] === undefined) {
          dic[result[index].userId] = 1;
        } else {
          dic[result[index].userId] += 1;
        }
      }
    }
    console.log(dic);
  }
});
