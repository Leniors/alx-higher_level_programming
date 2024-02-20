#!/usr/bin/node
const request = require('request');
const [, , url] = process.argv;
request(url, (error, response, body) => {
  if (error) {
    return;
  }
  const results = JSON.parse(body);
  let present = 0;
  const films = results.results;
  for (const i in films) {
    const characters = films[i].characters;
    for (const j in characters) {
      if (characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        present += 1;
      }
    }
  }
  console.log(present);
});
