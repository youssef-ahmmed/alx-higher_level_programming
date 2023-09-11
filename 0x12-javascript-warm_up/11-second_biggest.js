#!/usr/bin/node
const args = process.argv.slice(2);

if (!args.length || args.length === 1) {
  console.log(0);
} else {
  args.sort();
  console.log(args[args.length - 2]);
}
