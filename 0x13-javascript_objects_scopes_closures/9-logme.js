#!/usr/bin/node

let occurence = 0;
exports.logMe = function (item) {
  console.log(`${occurence}: ${item}`);
  occurence++;
};
