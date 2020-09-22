#!/usr/bin/node
let requestMod = require('request');
let requestUri = 'http://swapi.co/api/films/';
let id = process.argv[2];

requestMod(requestUri + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
