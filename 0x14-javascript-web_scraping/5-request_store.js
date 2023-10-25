#!/usr/bin/node

/**
 * gets the contents of a webpage and stores it in a file
 */

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];
request(url, (error, response, body) => {
  if (error) throw error;
  // console.log(body);
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
