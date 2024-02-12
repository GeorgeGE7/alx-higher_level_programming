#!/usr/bin/node
if (process.argv.length <= 3) {
  const zeroString = "0";
  console.log(zeroString);
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort(function (a, b) {
    return b - a;
  })[1];
  console.log(second);
}
