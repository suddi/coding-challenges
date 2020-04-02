'use strict';

/* eslint no-param-reassign: off */

/**
 * Swap numbers within an array
 */
function swap(array, i, j) {
    const temp = array[i];                                          // O(1)
    array[i] = array[j];                                            // O(1)
    array[j] = temp;                                                // O(1)
}

/**
 * Returns true if value is even
 */
function isEven(value) {
    return Math.abs(value) % 2 === 0;                               // O(1)
}

/**
 * Returns true if value is odd
 */
function isOdd(value) {
    return Math.abs(value) % 2 === 1;                               // O(1)
}

/**
 * Given a variable length array of integers, partition them such that the even
 * integers precede the odd integers in the array. Your must operate on the array
 * in-place, with a constant amount of extra space.
 *
 * The answer should scale linearly in time with respect to the size of the array.
 */
function solution(numbers) {
    const length = numbers.length;                                  // O(1)
    let i = 0;                                                      // O(1)
    let j = length - 1;                                             // O(1)

    while (i < j) {                                                 // < O(N)
        if (isEven(numbers[i])) {                                   // O(1)
            i++;                                                    // O(1)
        }
        if (isOdd(numbers[j])) {                                    // O(1)
            j--;                                                    // O(1)
        }

        if (isOdd(numbers[i]) && isEven(numbers[j])) {              // O(1)
            swap(numbers, i, j);                                    // O(1)
            i++;                                                    // O(1)
            j--;                                                    // O(1)
        }
    }

    return numbers;
}

module.exports = {
    isEven,
    isOdd,
    solution
};
