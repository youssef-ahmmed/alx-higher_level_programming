#!/usr/bin/node

const dict = require('./101-data').dict;

const userIDsByOccurrence = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!userIDsByOccurrence[occurrence]) {
    userIDsByOccurrence[occurrence] = [];
  }

  userIDsByOccurrence[occurrence].push(userId);
}

console.log(userIDsByOccurrence);
