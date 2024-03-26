#!/usr/bin/node
const req = require('request');
const fileStore = require('fs');
req(process.argv[2]).pipe(fileStore.createWriteStream(process.argv[3]));
