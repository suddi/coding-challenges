# -*- coding: utf-8 -*-

def solution(arrays, k):                                            # O(N^2)
    """
    Given an array of arrays, find the intersecting values in k number of arrays

    >>> solution([ \
        [2, 5, 3, 2, 8, 1, 1, 2, 2], \
        [7, 9, 5, 2, 4, 10, 10], \
        [6, 7, 5, 5, 3, 7] \
    ], 2)
    [2, 3, 5, 7]
    >>> solution([ \
        [2, 5, 3, 2, 8, 1, 1, 2, 2], \
        [7, 9, 5, 2, 4, 10, 10], \
        [6, 7, 5, 5, 3, 7] \
    ], 3)
    [5]
    """
    count = {}                                                      # O(1)
    result = set()                                                  # O(1)
    for array in arrays:                                            # O(N)
        for i in set(array):                                        # O(N)
            if i not in count:                                      # O(1)
                count[i] = 1                                        # O(1)
            else:                                                   # O(1)
                count[i] += 1                                       # O(1)

            if count[i] >= k:                                       # O(1)
                result.add(i)                                       # O(1)
    return list(result)                                             # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
