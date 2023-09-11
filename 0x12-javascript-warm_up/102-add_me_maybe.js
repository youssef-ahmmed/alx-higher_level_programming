#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  theFunction(parseInt(number) + 1);
};
