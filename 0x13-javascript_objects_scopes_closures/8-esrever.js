#!/usr/bin/node
exports.esrever = function (list) {
  let last = list.length - 1;
  for (let i = 0; i < list.length && i <= last; i++) {
    const temp = list[i];
    list[i] = list[last];
    list[last] = temp;
    last -= 1;
  }
  return list;
};
