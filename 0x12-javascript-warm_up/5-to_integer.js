#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv[2];
const intValue = parseInt(arg);

if (!isNaN(intValue)) {
  console.log(`My number: ${intValue}`);
} else {
  console.log('Not a number');
}
