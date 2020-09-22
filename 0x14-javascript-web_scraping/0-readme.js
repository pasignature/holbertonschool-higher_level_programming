#!/usr/bin/node
let filesystem = require('fs');
filesystem.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
