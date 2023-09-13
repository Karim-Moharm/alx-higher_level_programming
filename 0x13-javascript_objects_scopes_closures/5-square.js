#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
<<<<<<< HEAD
=======
    this.size = size;
>>>>>>> f382840bf4659d16fa2b00507178a1a5294c3ac9
  }
};
