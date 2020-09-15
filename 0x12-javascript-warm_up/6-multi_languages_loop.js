#!/usr/bin/node
// loop through an array of string and print
'use strict';
let languages = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (let language in languages) {
  console.log(languages[language]);
}
