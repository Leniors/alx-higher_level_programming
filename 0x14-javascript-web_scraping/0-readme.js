#!/usr/bin/node
/* read a file */
const fs = require('fs');
const [, , filename] = process.argv;
fs.readFile(filename, 'utf-8', (err, data) => {
  if (err != null) {
    console.log(err);
  } else {
    console.log(data);
  }
});
