#!/usr/bin/node
'use strict';

exports.converter = function (base) {
  function convert (number) {
    return number.toString(base);
  }
  return convert;
};
