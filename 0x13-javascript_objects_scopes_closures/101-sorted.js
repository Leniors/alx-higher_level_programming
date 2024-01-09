#!/usr/bin/node
const { dict } = require('./101-data.js');
console.log(dict);
const keys = []
for (let key in dict) {
	keys.push(dict[key]);
}
const newKeys = new Set(keys);
const dict1 = {};
for (const value of newKeys) {
	let list = [];
	for (let i in dict) {
		if (dict[i] === value) {
			list.push(i);
		}
	}
	dict1[value] = list;
}
console.log(dict1);
