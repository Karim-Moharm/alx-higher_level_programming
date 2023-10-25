#!/usr/bin/node

/**
 * computes the number of tasks completed by user id
 */

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) throw error;
  const objectBody = JSON.parse(body);
  const itemsNum = objectBody.length;
  for (let i = 0; i < itemsNum; i++);
});
