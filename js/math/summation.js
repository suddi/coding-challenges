// Compute to 100: Given the digits 123456789, build an expression by inserting "+" or "-" anywhere BETWEEN the digits so that it results to 100.
// Your answer should return all possible combinations.
// Example: 1 + 23 - 4 + 5 + 6 + 78 - 9 = 100

function retrieveArray(v) {
    return v.toString(10).split('').map(Number);
}

function concatPrefix(prefix, paths) {
    return paths
        .filter(function(p) { return p.length > 0; })
        .map(function(p) { return prefix.concat(p); });
}

function findPaths(sum, previousNumber, index) {
    var previousDigit = Math.abs(previousNumber%10);
    if (index >= digits.length) {
        return sum == previousNumber ? [[previousDigit]] : [];
    }

    var currentDigit = digits[index];
    var concatenatedNumber = previousNumber >= 0 ? 10*previousNumber + currentDigit : 10*previousNumber - currentDigit;

    var plusPaths = findPaths(sum-previousNumber, currentDigit, index+1);
    var minusPaths = findPaths(sum-previousNumber, -currentDigit, index+1);
    var concatPaths = findPaths(sum, concatenatedNumber, index+1);

    var paths = [];
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '+'], plusPaths));
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '-'], minusPaths));
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '&'], concatPaths));
    return paths;
}

var foundPaths = findPaths(searchSum, digits[0], 1);

if (foundPaths.length == 0) {
    console.log("no paths were found");
} else {
    for (var i = 0; i < foundPaths.length; i++) {
        console.log(foundPaths[i].join("").replace(/&/g, ""));
    }
}

function solution(input, searchSum) {

    const foundPaths = findPaths(inputNums, searchSum, input[0], 1, []);
}

const input = 123456789;
const searchSum = 100;
console.log(solution(input, searchSum));
