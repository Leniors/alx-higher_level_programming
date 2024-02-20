#!/usr/bin/node
const request = require('request');
const [, , id] = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films';
request(url, (error, response, body) => {
  if (error) {
    return;
  }
  const results = JSON.parse(body);
  const films = results.results;
  const film = films[id - 1];
  const characters = film.characters;
  for (const j in characters) {
    request(characters[j], (error, response, body) => {
      if (error) {
        return;
      }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
