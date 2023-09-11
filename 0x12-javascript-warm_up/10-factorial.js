#!/usr/bin/node

const num = parseInt(process.argv[2]);

const fact = (n) => {
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

console.log(fact(num));
