#!/usr/bin/node
const fs = require('fs');

const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;
fs.readFile(sourceFilePath1, 'utf8', (err1, data1) => {
	fs.readFile(sourceFilePath2, 'utf8', (err2, data2) => {
		const concatenatedContent = data1 + data2;
		fs.writeFile(destinationFilePath, concatenatedContent, 'utf8', (errWrite) => {
		});
	});
});
