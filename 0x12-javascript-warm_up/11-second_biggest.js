#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = [];
  for (let i = 0; i < process.argv.length - 2; i++) {
    list[i] = process.argv[i + 2];
  }
  list.sort();
  console.log(list[list.length - 2]);
}
