#!/usr/bin/node
const base64 = require('base-64');
const request = require('request');
const utf8 = require('utf8');

let new_promise = new Promise(function (resolve, reject) {
  const token = utf8.decode(base64.encode(`${process.argv[2]}:${process.argv[3]}`));
  const options = {
    url: 'https://api.twitter.com/oauth2/token',
    headers: {
      Authorization: `Basic ${token}`,
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    },
    form: {
      grant_type: 'client_credentials'
    }
  };
  request.post(options, function (err, ress, body) {
    if (!err) {
      resolve(JSON.parse(body).access_token);
    }
  });
});

new_promise.then(
  result => search(result),
  err => console.log(err)
);

function search (token) {
  const options = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: {
      Authorization: `Bearer ${token}`
    },
    qs: {
      q: process.argv[4],
      count: '5'
    }
  };
  request.get(options, function (err, ress, body) {
    if (!err) {
      const tweets = JSON.parse(body).statuses;
      tweets.forEach((t) => console.log(`[${t.id}] ${t.text} by ${t.user.name}`));
    }
  });
}
