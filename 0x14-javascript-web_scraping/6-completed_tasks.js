#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = argv[2];
request(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const tasks = {};
    data.forEach(task => {
      if (task.completed && !(task.userId in tasks)) {
        tasks[task.userId] = 1;
      } else if (task.completed && task.userId in tasks) {
        tasks[task.userId]++;
      }
    });
    console.log(tasks);
  }
});
