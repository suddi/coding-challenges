# -*- coding: utf-8 -*-

def solution1(A):                                                   # O(N)
    """
    You are given a list A (eg. [1, 2, 3, 7, 1, 5]).
    Write a function to calculate the pivot of the array such that the
    left hand side = right hand side.

    In the example, pivot (P) = 3, because 1 + 2 + 3 = 1 + 5.

    Expected time complexity = O(N).
    Expected auxillary space complexity = O(N).

    >>> solution1([1, 2, 3, 7, 1, 5])
    3
    >>> solution1([2, 4, 5, 10, 1, 2, 4, 4])
    3
    >>> solution1([4, 5, 2, 2, 1])
    -1
    >>> solution1([10, 3, 7, 3])
    1
    >>> solution1([2, 8, 1, 10])
    2
    """
    i = 0                                                           # O(1)
    total = sum(A)                                                  # O(N)

    while i < len(A):                                               # < O(N)
        lastdigit = 0                                               # O(1)
        if i > 0:                                                   # O(1)
            lastdigit = A[i - 1]                                    # O(1)
        total -= (A[i] + lastdigit)                                 # O(1)
        if total == 0:                                              # O(1)
            return i                                                # O(1)
        i += 1                                                      # O(1)
    return -1                                                       # O(1)

def solution2(A):                                                   # O(N)
    """
    You are given a list A (eg. [1, 2, 3, 7, 1, 5]).
    Write a function to calculate the pivot of the array such that the
    left hand side = right hand side.

    In the example, pivot (P) = 3, because 1 + 2 + 3 = 1 + 5.

    Expected time complexity = O(N).
    Expected auxillary space complexity = O(N).

    >>> solution2([1, 2, 3, 7, 1, 5])
    3
    >>> solution2([2, 4, 5, 10, 1, 2, 4, 4])
    3
    >>> solution2([4, 5, 2, 2, 1])
    -1
    >>> solution2([10, 3, 7, 3])
    1
    >>> solution2([2, 8, 1, 10])
    2
    """
    i = 0                                                           # O(1)
    total = sum(A)                                                  # O(N)

    while i < len(A):                                               # < O(N)
        pivot = total - A[i]                                        # O(1)
        if pivot == 0:                                              # O(1)
            return i                                                # O(1)
        total -= (2 * A[i])                                         # O(1)
        i += 1                                                      # O(1)

    return -1                                                       # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
