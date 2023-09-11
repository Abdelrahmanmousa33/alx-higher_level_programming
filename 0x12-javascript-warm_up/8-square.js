#!/usr/bin/node

let row = '';
if (Number.isInteger(Number(process.argv[2]))) {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      row = row + 'X';
    }
    console.log(row);
    row = '';
  }
}
