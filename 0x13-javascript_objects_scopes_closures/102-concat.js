#!/usr/bin/node

const fs = require('fs');

const concatFiles = (firstFile, secondFile, thirdFile) => {
  const firstData = fs.readFileSync(firstFile, 'utf-8');

  const secondData = fs.readFileSync(secondFile, 'utf-8');

  const thirdData = firstData + secondData;

  fs.writeFileSync(thirdFile, thirdData);
};

const firstFile = process.argv[2];
const secondFile = process.argv[3];
const thirdFile = process.argv[4];

if (
  fs.existsSync(firstFile) && fs.statSync(firstFile).isFile() &&
  fs.existsSync(secondFile) && fs.statSync(secondFile).isFile() &&
  thirdFile !== undefined
) {
  concatFiles(firstFile, secondFile, thirdFile);
}
