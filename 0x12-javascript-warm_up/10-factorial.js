#!/usr/bin/node

function factorial (a) {
  if (a === 1 || !Number.isInteger(Number(a))) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(process.argv[2]));
