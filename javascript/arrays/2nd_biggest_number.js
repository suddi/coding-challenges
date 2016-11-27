'use strict';

function solution(array) {
    let max_1;
    let max_2;

    for (let v of array) {
        if (!max_1) {
            max_1 = v;
        } else if (!max_2 && v !== max_1) {
            max_2 = Math.min(max_1, v);
        } else {
            if (v > max_1) {
                max_2 = max_1;
                max_1 = v;
            } else if (v > max_2 && v !== max_1) {
                max_2 = v;
            }
        }
    }

    return max_2;
}

const answer = solution([4, 4, -5, 3, 2, 3, 7, 7, 8, 8]);
console.log(answer);
