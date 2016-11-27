'use strict';

function solution(value) {
    let array = [];
    let subarray = [];

    for (let v of value) {
        const len = subarray.length;
        if (!len || subarray[len - 1] <= v) {
            subarray.push(v);
        } else {
            array.push(subarray);
            subarray = [v];
        }
    }

    array.push(subarray);
    return array;
}

const answer = solution([1, 2, 10, 10, 8, 12, 5, 23, 1]);
console.log(answer);
