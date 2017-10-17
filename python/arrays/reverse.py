# -*- coding: utf-8 -*-

def solution(A):                                                    # O(N/2)
    """
    Write a function to reverse a list without using the built-in function.

    >>> solution([1, 2, 3, 4, 5, 6, 7])
    [7, 6, 5, 4, 3, 2, 1]
    """
    i = 0                                                           # O(1)
    j = len(A) - 1                                                  # O(1)

    while i < j:                                                    # O(N/2)
        A[i], A[j] = A[j], A[i]                                     # O(1)
        i += 1                                                      # O(1)
        j -= 1                                                      # O(1)
    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
