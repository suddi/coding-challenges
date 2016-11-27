'use strict';

function solution(a, b) {
    const len_a = a.length;
    if (len_a !== b.length) {
        return false;
    }

    for (let i = 0; i < len_a; i++) {
        if (a === b) {
            return true;
        }
        a = a.slice(1) + a[0];
    }
    return false;
}

const answer = solution('aabbcc', 'bccaab');
console.log(answer);
