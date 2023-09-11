#!/usr/bin/node
console.log(isNaN(parseInt(process.argv[2])) ? 'Not a number' : `My number: ${process.argv[2]}`);
