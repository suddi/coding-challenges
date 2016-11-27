# -*- coding: utf-8 -*-

def solution(A):
    """
    You are given a list A (eg. [1, 2, 3, 7, 1, 5]).
    Write a function to calculate the pivot of the array such that the left hand side = right hand side.

    In the example, pivot (P) = 3, because 1 + 2 + 3 = 1 + 5.

    Expected time complexity = O(N).
    Expected auxillary space complexity = O(N).

    >>> solution([1, 2, 3, 7, 1, 5])
    3
    >>> solution([2, 4, 5, 10, 1, 2, 4, 4])
    3
    >>> solution([4, 5, 2, 2, 1])
    -1
    """
    i = 0
    total = sum(A)

    while i < len(A):
        lastdigit = 0
        if i > 0:
            lastdigit = A[i - 1]
        total -= (A[i] + lastdigit)
        if total == 0:
            return i
        i += 1
    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
