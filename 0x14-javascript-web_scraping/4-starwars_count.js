#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (eoer, res, body) {
  if (!eoer) {
    const ress = JSON.parse(body).results;
    console.log(ress.reduce((num, film) => {
      return film.characters.find((char) => char.endsWith('/18/'))
        ? num + 1
        : num;
    }, 0));
  }
});
