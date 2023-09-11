#!/usr/bin/node

if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log(0);
} else {
  const sortedArgs = process.argv.sort();
  console.log(sortedArgs[sortedArgs.length - 2]);
}
