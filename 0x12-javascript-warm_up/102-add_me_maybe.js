#!/usr/bin/node
// function that increments and calls a function.
'use strict';
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number++);
};
