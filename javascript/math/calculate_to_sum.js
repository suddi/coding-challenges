'use strict';

/**
 * Convert integer into a split array
 */
function retrieveArray(value) {
    return value
        .toString(10)
        .split('')
        .map(Number);
}

function concatPrefix(prefix, paths) {
    return paths
        .filter(function (p) {
            return p.length > 0;
        })
        .map(function (p) {
            return prefix.concat(p);
        });
}

function findPaths(sum, inputNums, previousNumber, index) {
    const previousDigit = Math.abs(previousNumber % 10);
    if (index >= inputNums.length) {
        return sum === previousNumber ? [[previousDigit]] : [];
    }

    const currentDigit = inputNums[index];
    const addValue = (10 * previousNumber) + currentDigit;
    const subtractValue = (10 * previousNumber) - currentDigit;
    const concatenatedNumber = previousNumber >= 0 ? addValue : subtractValue;

    const plusPaths = findPaths(sum - previousNumber, inputNums, currentDigit, index + 1);
    const minusPaths = findPaths(sum - previousNumber, inputNums, -currentDigit, index + 1);
    const concatPaths = findPaths(sum, inputNums, concatenatedNumber, index + 1);

    let paths = [];
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '+'], plusPaths));
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '-'], minusPaths));
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '&'], concatPaths));

    return paths;
}

/**
 * Compute to 100: Given the digits 123456789,
 * build an expression by inserting "+" or "-" anywhere
 * BETWEEN the digits so that it results to 100.
*/
function solution(digits) {
    const inputNums = retrieveArray(digits);
    const foundPaths = findPaths(100, inputNums, inputNums[0], 1);

    let newDigits = '';
    for (let foundPath of foundPaths) {
        newDigits += `${foundPath.join('').replace(/&/g, '')}\n`;
    }

    return newDigits.trim();
}

module.exports = {
    solution
};
