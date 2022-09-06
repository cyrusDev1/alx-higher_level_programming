#!/usr/bin/node
const Squarep = require('./5-square');
class Square extends Squarep {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let h = 0; h < this.height; h++) {
      if (c) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
