#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

const firstArg = parseInt(argv[2]);
const secondArg = parseInt(argv[3]);

if (!isNaN(firstArg) && !isNaN(secondArg)) {
  const result = add(firstArg, secondArg);
  console.log(result);
} else {
  console.log('NaN');
}
