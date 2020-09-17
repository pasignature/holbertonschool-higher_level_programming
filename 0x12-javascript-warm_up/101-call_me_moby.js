#!/usr/bin/node
// function that executes x times a function.
'use strict';
exports.callMeMoby = function (x, theFunction) {
  for (let count = 0; count < x; count++) {
    theFunction();
  }
};
