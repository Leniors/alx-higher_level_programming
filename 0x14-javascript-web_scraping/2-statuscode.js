#!/usr/bin/node
const request = require('request');
const [, , url] = process.argv;
request(url, (error, response) => {
  if (error) {
    return;
  }
  console.log('code:', response.statusCode);
});
