#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);
let i = 0;
let j = 0;

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  if (squareSize > 0) {
    for (i = 0; i < squareSize; i++) {
      let row = '';
      for (j = 0; j < squareSize; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
