#!/usr/bin/node

/**
 * prints the title of a Star Wars movie
 * where the episode number matches a given integer
 * first argument must be movie ID
 */
request = require('request');

const episode_api = "https://swapi-api.alx-tools.com/api/films/" +
    process.argv[2];

console.log(episode_api);




