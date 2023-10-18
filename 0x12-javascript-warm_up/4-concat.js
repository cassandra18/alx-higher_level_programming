#!/usr/bin/node

const { argv } = require('node:process');

const arg1 = argv[2] || 'undefined';
const arg2 = argv[3] || 'undefined';

console.log(arg1 + ' is ' + arg2);
