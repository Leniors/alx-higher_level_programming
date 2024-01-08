#!/usr/bin/node
if ((process.argv).length <= 2) {
	console.log(0);
	return;
} else if ((process.argv).length === 3) {
	console.log(0);
	return;
}
let myArray = [];
for (let i = 2; i < (process.argv).length; i++) {
	myArray.push(process.argv[i]);
}
myArray.sort(function (a, b) {
	return a - b;
})
let len = myArray.length;
console.log(myArray[len - 2]);
