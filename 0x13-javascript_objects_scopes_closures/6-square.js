#!/usr/bin/node

const MainSquare = require('./5-square');
class Square extends MainSquare {
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.height));
    }
  }
}

module.exports = Square;
