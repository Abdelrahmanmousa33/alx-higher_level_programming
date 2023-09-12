#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbO = 0;
  for (const ele of list) {
    if (ele === searchElement) {
      nbO++;
    }
  }
  return nbO;
};
