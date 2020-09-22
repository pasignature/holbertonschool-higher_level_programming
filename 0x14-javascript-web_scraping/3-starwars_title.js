#!/usr/bin/node
const requestMod = require('request');
const requestUri = 'http://swapi.co/api/films/';
const id = process.argv[2];

requestMod(requestUri + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
