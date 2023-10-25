#!/usr/bin/node

/**
 * prints the title of a Star Wars movie
 * where the episode number matches a given integer
 * first argument must be movie ID
 */
const request = require('request');

const episodeApi = 'https://swapi-api.alx-tools.com/api/films/' +
    process.argv[2];

if (process.argv.length === 3) {
  request(episodeApi, (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).title);
  });
}
