#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const [, , url, filename] = process.argv;
request(url, (error, response, body) => {
  if (error) {
    return;
  }
  fs.writeFile(filename, body, 'utf-8', (err) => {
    if (err != null) {
      return;
    }
  });
});
