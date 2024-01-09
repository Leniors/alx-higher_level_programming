#!/usr/bin/node
const { dict } = require('./101-data.js');

function computeUserIdsByOccurrence(inputDict) {
	const resultDict = {};

	for (const userId in inputDict) {
		const occurrence = inputDict[userId];

		if (resultDict[occurrence]) {
			resultDict[occurrence].push(userId);
		} else {
			resultDict[occurrence] = [userId];
		}
	}
	return resultDict;
}
const userIdsByOccurrence = computeUserIdsByOccurrence(dict);

console.log(userIdsByOccurrence);
