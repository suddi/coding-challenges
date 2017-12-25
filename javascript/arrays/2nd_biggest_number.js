'use strict';

/**
 * Write a function to find the 2nd biggest number in a list.
 *
 * @example
 * solution([4, 4, -5, 3, 2, 3, 7, 7, 8, 8]) // => 7
 * solution([-1, -2, -15, -1, -2, -1, -2]) // => -2
 * solution([1, 1, 1, 1]) // =>
 */
function solution(a) {                                              // O(N)
    let max1;                                                       // O(1)
    let max2;                                                       // O(1)

    for (let value of a) {                                          // O(N)
        if (!max1) {                                                // O(1)
            max1 = value;                                           // O(1)
        } else if (value > max1) {                                  // O(1)
            max2 = max1;                                            // O(1)
            max1 = value;                                           // O(1)
        } else if (value < max1) {                                  // O(1)
            if (!max2) {                                            // O(1)
                max2 = value;                                       // O(1)
            } else if (value > max2) {                              // O(1)
                max2 = value;                                       // O(1)
            }
        }
    }

    return max2;                                                    // O(1)
}
