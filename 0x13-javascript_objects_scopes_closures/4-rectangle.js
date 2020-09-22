#!/usr/bin/node
// class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let count = 0; count < this.height; count++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const holder = this.width;
    this.width = this.height;
    this.height = holder;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
