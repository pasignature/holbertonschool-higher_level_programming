#!/usr/bin/node
// loop through an array of string and print
'use strict';
const languages = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (const language in languages) {
  console.log(languages[language]);
}
