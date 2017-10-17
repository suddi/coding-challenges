# -*- coding: utf-8 -*-

def solution(A):                                                    # O(N/2)
    """
    Write a sorting function to put the even numbers first, odd numbers afterwards.

    >>> solution([5, 2, 2, 4, 1, 3, 7, 9])
    [4, 2, 2, 5, 1, 3, 7, 9]
    >>> solution([2, 4, 6, 2, 0, 8])
    [2, 4, 6, 2, 0, 8]
    >>> solution([1, 3, 5, 7, 3, 9, 1, 5])
    [1, 3, 5, 7, 3, 9, 1, 5]
    """
    i = 0                                                           # O(1)
    j = len(A) - 1                                                  # O(1)

    def is_even(value):
        return value % 2 == 0                                       # O(1)

    def is_odd(value):
        return value % 2 == 1                                       # O(1)

    while i < j:                                                    # O(N/2)
        if is_even(A[i]):                                           # O(1)
            i += 1                                                  # O(1)

        if is_odd(A[j]):                                            # O(1)
            j -= 1                                                  # O(1)

        if is_odd(A[i]) and is_even(A[j]):                          # O(1)
            A[i], A[j] = A[j], A[i]                                 # O(1)
            i += 1                                                  # O(1)
            j -= 1                                                  # O(1)

    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
