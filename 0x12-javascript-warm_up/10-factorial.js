#!/usr/bin/node
function recursion(n) {
  if (isNaN(Number(n))) {
    return 1;
  } else if (n === 0) {
    return 1;
  }
  return n * recursion(n - 1);
}
console.log(recursion(process.argv[2]));
