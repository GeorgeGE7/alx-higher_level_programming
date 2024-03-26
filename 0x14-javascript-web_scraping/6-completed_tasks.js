#!/usr/bin/node
const u_r_l = process.argv[2];
const req = require('request');

req(u_r_l, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const done = {};
    const all_tasks = JSON.parse(body);
    for (const i in all_tasks) {
      const task = all_tasks[i];
      if (task.completed === true) {
        if (done[task.userId] === undefined) {
          done[task.userId] = 1;
        } else {
          done[task.userId]++;
        }
      }
    }
    console.log(done);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
