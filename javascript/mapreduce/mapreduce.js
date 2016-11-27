'use strict';

// MapReduce: You are provided with a dataset which is an ASCII text file. You are
// to create a mapreduce program that processes the dataset.  The mapper should
// process each line and produce key-value pairs. The reducer should process the
// values corresponding to each key. The goal of the program is to find the
// occurrences of a given word in the text with the mapreduce pattern.

const fs = require('fs');

// helper functions
let count = 0;
const keywordToFind = 'TCP';

fs.readFile(__dirname + '/input.txt', 'utf8', function(err,data) {
    if (err) {
        return console.log('file not found');
    }
    //console.log(data);

    // fake map reduce calls
    const lines = data.split('\n');
    for (let i = 0; i < lines.length; i++) {
        map(i, lines[i])
    }
    for (let key in context.map) {
        reduce(key, context.read(key));
    }
    // OUTPUT ALL KEYS AND THEIR FINAL COUNT
    //for (const key in result.map) {
    //  console.log(key, result.read(key))
    //}

    count = result.map[keywordToFind.toLowerCase()];
    printResult();
});

// *** Start your code here *** //

const context = {
    map: {},
    // TODO
    read: function (k) {
        return context.map[k];
    }
}

const result = {
    map: {},
    // TODO
    read: function (k) {
        return result.map[k];
    }
}

function map(key, value) {
    // TODO
    const words = value.split(/ +/);

    context.map[key] = [];
    for (let word of words) {
        word = word.replace(/[-\.\[\]\\'\f"\(\)\<\>]/g, '');
        if (word.length) {
            context.map[key].push([word.toLowerCase(), 1]);
        }
    }
}

function reduce(key, values) {
    // TODO
    for (let value of values) {
        result.map[value[0]] = result.map[value[0]] ? result.map[value[0]] + value[1] : value[1];
    }
}

// *** End your code here *** //

function printResult() {
    console.log(count);
}
