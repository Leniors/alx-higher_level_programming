#!/usr/bin/node
let itemNo = 0;
exports.logMe = function (item) {
  console.log(`${itemNo}:${item}`);
  itemNo += 1;
};
