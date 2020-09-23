#!/usr/bin/node

'use strict';

const requestMod = require('request');
const requestUrl = 'http://swapi.co/api/films/' + process.argv[2];

requestMod(requestUrl, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const characters = resp.characters;
    for (let i = 0; i < characters.length; i++) {
      requestMod(characters[i], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
