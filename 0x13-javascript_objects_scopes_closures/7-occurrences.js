#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numofOccurence = 0;

  for (const idx in list) {
    if (list[idx] === searchElement) {
      numofOccurence++;
    }
  }
  return numofOccurence;
};
