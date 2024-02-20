#!/usr/bin/node
const request = require('request');
const [, , url] = process.argv;
request(url, (error, responsei, body) => {
  if (error) {
    return;
  }
  const todos = JSON.parse(body);
  const result = {};
  for (const i in todos) {
    if (todos[i].completed) {
      if (result[todos[i].userId]) {
        result[todos[i].userId]++;
      } else {
        result[todos[i].userId] = 1;
      }
    }
  }
  console.log(result);
});
