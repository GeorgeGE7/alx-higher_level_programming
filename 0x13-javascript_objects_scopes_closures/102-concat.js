#!/usr/bin/node
const fs = require('fs');

const first = fs.readFileSync(process.argv[2]).toString();
const seconde = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], `${first}${seconde}`);
