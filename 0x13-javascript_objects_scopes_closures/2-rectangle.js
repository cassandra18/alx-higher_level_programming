#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h) || !Number.isInteger(w) || !Number.isInteger(h)) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
