#!/usr/bin/node

/**
 * prints the number of movies where
 * the character “Wedge Antilles” is present
 */

const request = require('request');

const url = process.argv[2];
if (process.argv.length === 3) {
  request(url, (error, response, body) => {
    if (error) throw error;
    const bodyData = JSON.parse(body).results;
    const filmsNum = bodyData.length;
    let count = 0;

    for (let i = 0; i < filmsNum; i++) {
      for (let j = 0; j < bodyData[i].characters.length; j++) {
        if (bodyData[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  });
}
