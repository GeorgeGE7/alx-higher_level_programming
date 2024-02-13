#!/usr/bin/node
exports.esrever = function (list) {
  let tool = list?.length - 1;
  let n = 0;
  while ((tool - n) > 0) {
    const temp = list[tool];
    list[tool] = list[n];
    list[n] = temp;
    n++;
    tool--;
  }
  return list;
};
