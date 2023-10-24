#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
if (process.argv.length === 3) {
  request(url, function (error, response) {
    if (error) throw error;
    console.log(`code: ${response.statusCode}`);
  });
}
