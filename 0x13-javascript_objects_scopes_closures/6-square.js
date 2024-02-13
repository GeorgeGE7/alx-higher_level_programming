#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      let s = '';
      for (let sn = 0; sn < this.width; sn++) {
        s = `${s}${c}`;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
