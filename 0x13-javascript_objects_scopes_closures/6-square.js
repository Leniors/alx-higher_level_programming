#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += 'X';
        }
        console.log(line);
      }
    }
  }
};
