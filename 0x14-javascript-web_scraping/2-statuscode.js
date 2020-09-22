#!/usr/bin/node
const requestUri = require('request');
requestUri(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
