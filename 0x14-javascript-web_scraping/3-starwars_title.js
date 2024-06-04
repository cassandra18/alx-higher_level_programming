#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;

if (!episodeId) {
  console.error('Usage: node 3-starwars_title.js <episode_id>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
