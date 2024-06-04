#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Usage: node 2-statusCode.js <url>');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(`code:  ${response.statusCode}`);
});
