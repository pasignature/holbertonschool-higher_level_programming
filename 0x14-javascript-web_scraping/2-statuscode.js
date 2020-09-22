#!/usr/bin/node
const request_uri = require('request');
request_uri(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
