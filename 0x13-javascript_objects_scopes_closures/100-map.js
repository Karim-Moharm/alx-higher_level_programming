#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map(function (elem, idx, arr) {
  return elem * idx;
});

console.log(list);
console.log(newList);
