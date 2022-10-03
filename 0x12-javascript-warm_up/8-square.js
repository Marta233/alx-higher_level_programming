#!/usr/bin/node
const args = process.argv[2];
for (let r = 0; r < args; r++) {
  let row = "";
  for (let c = 0; c < args; c++) row += "X";
  console.log(row);
}
