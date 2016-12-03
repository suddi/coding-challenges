# -*- coding: utf-8 -*-

def solution(numbers, target):                                      # O(N)
    """
    Similar to src.arrays.two_sum, find all the combinations that can be added up to reach a given target.
    Given that all values are unique.

    >>> solution([1, 2, 3, 4, 5], 5)
    2
    >>> solution([3, 4, 5, 6], 9)
    2
    """
    remaining = {}                                                  # O(1)
    combinations = []                                               # O(1)

    for count, number in enumerate(numbers):                        # O(N)
        if number in remaining:                                     # O(1)
            a = remaining[number]                                   # O(1)
            b = number                                              # O(1)
            combinations.append([remaining[number], count])         # O(1)
        else:                                                       # O(1)
            remaining[target - number] = number                     # O(1)

    return len(combinations)                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
