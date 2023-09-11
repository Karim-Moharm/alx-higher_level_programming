#!/usr/bin/node

const count = process.argv[2];
let i = 0;

if (typeof count === 'undefined') {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
