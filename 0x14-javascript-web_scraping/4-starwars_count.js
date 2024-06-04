#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

if (!apiUrl) {
  console.error('Usage: node 4-starwars_count.js <api_url>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    const filteredMovies = movies.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(filteredMovies.length);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
