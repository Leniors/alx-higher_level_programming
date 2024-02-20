#!/usr/bin/node
/* Write to a file */
const fs = require('fs');
const [, , filename, content] = process.argv;

fs.writeFile(filename, content, 'utf-8', (err) => {
  if (err != null) {
    console.log(err);
  }
});
