# -*- coding: utf-8 -*-

def solution(A, target):                                            # O(N)
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

    for count, value in enumerate(A):                               # O(N)
        if value in remaining:                                      # O(1)
            a = remaining[value]                                    # O(1)
            b = value                                               # O(1)
            combinations.append([remaining[value], count])          # O(1)
        else:                                                       # O(1)
            remaining[target - value] = value                       # O(1)

    return len(combinations)                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
