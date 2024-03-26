#!/usr/bin/node

const req = require('request');
const Base_URL = 'https://swapi-api.hbtn.io/api/films/';
const episodeNumber = process.argv[2];

req(Base_URL + episodeNumber, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const resJSON = JSON.parse(body);
    console.log(resJSON.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
