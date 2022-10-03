#!/usr/bin/node
const count = process.argv[2];
if (count == undefined) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}
