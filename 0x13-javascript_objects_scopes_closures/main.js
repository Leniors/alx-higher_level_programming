#!/usr/bin/node
function Person(name) {
	this.name = name;
	this.introduceSelf = function () {
		console.log(`Hi! I'm ${this.name}.`);
	};
}
lee = new Person("Leeroy");
lee.introduceSelf();
console.log(lee);
