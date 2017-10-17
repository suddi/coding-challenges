'use strict';

/**
 * Write a function to group together all ascending sublists within a list a.
 *
 * @example
 * solution([1, 2, 10, 10, 8, 12, 5, 23, 1])
 * // => [[1, 2, 10, 10], [8, 12], [5, 23], [1]]
 * solution([3, 4, 5, 12, 2, 3, 5, 2, 5, -1])
 * // => [[3, 4, 5, 12], [2, 3, 5], [2, 5], [-1]]
 */
function solution(a) {                                              // O(N)
    let result = [];                                                // O(1)
    let group = [];                                                 // O(1)

    for (let value of a) {                                        // O(N)
        let length = group.length;                                // O(1)
        let lastValue = length ? group[length - 1] : -Infinity;   // O(1)
        if (value >= lastValue) {                                   // O(1)
            group.push(value);                                      // O(1)
        } else {                                                    // O(1)
            result.push(group);                                     // O(1)
            group = [value];                                        // O(1)
        }
    }

    if (group.length) {                                             // O(1)
        result.push(group);                                         // O(1)
    }
    return result;                                                  // O(1)
}
