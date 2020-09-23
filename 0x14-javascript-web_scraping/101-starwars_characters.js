#!/usr/bin/node

'use strict';

const requestMod = require('request');
const requestUrl = 'http://swapi.co/api/films/';
let id = parseInt(process.argv[2], 10);
let characters = [];

requestMod(requestUrl, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }
    for (let i = 0; i < results.length; i++) {
      if (results[i].episode_id === id) {
        characters = results[i].characters;
        break;
      }
    }
    for (let j = 0; j < characters.length; j++) {
      requestMod(characters[j], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
