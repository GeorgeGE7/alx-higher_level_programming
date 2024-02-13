#!/usr/bin/node
const rList = require("./100-data.js");
const list = rList.list;
console.log(list);
console.log(list.map((n, indx) => n * indx));
