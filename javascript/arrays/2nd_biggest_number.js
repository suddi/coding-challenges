'use strict';

/**
 * Write a function to find the 2nd biggest number in a list.
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

module.exports = {
    solution
};
