'use strict';

function solution(input) {
    let occurences = {};
    let lengths = {};

    function getSpacing(v, lengthNeeded) {
        const additional = lengthNeeded - v.length;
        return v + ' '.repeat(additional);
    }

    for (let v of input) {
        if (!occurences[v[0]]) {
            occurences[v[0]] = v[1];
        } else {
            occurences[v[0]] += v[1];
        }
    }

    for (let v in occurences) {
        lengths[v] = Math.max(v.length, occurences[v].toString(10).length) + 1;
        process.stdout.write(getSpacing(v, lengths[v]));
    }
    process.stdout.write('\n');

    let spacing = '';
    const keys = Object.keys(occurences);
    const length = keys.length;
    for (let i = 0; i < length; i++) {
        const value = occurences[keys[i]];
        console.log(spacing + value);
        spacing += ' '.repeat(lengths[keys[i]]);
    }
}

const answer = solution([['hello', 3], ['world', 2], ['this', 5], ['is', 2], ['fun', 9], ['hello', 1]]);
