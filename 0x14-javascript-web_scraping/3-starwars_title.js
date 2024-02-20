#!/usr/bin/node
const request = require('request');
const [, , id] = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (error, response) => {
  if (error) {
    return;
  }
  const obj = JSON.parse(response.body);
  console.log(obj.title);
});
