#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let temp = 0;
  for (let n = 0; n < list.length; n++) {
    if (searchElement === list[n]) {
      temp++;
    }
  }
  return temp;
};
