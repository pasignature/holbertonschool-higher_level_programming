#!/usr/bin/node
// class Square that defines square and inherits from 5-square.js
const newSquare = require('./5-square');

class Square extends newSquare {
  charPrint (c) {
    for (let count = 0; count < this.height; count++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
