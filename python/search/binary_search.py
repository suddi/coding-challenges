# -*- coding: utf-8 -*-

def solution(A, target):                                            # O(N/2)
    """
    Apply binary search on sorted array of integers.

    >>> solution([1, 2, 3, 7, 11, 15], 11)
    4
    >>> solution([2, 4, 5, 10, 11, 12, 24, 44], 2)
    0
    >>> solution([4, 5, 12, 42, 61], 7)
    -1
    """
    lower = 0                                                       # O(1)
    upper = len(A)                                                  # O(1)

    while lower < upper:                                            # O(N/2)
        mid = lower + (upper - lower) // 2                          # O(1)
        value = A[mid]                                              # O(1)

        if value == target:                                         # O(1)
            return mid                                              # O(1)
        if value < target:                                          # O(1)
            if mid == lower:                                        # O(1)
                break                                               # O(1)
            lower = mid + 1                                         # O(1)
        else:                                                       # O(1)
            upper = mid                                             # O(1)

    return -1                                                       # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
