#!/usr/bin/node

exports.esrever = function (list) {
  let idx = list.length - 1;
  const revList = [];

  for (idx; idx >= 0; idx--) {
    revList.push(list[idx]);
  }
  return revList;
};
