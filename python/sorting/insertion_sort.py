# -*- coding: utf-8 -*-

def solution(A):                                                    # O(N^2)
    """
    Sort numbers in list A using insertion sort.

    >>> solution([5, 2, 2, 4, 1, 3, 7, 9])
    [1, 2, 2, 3, 4, 5, 7, 9]
    >>> solution([2, 4, 6, 2, 0, 8])
    [0, 2, 2, 4, 6, 8]
    >>> solution([1, 3, 5, 7, 3, 9, 1, 5])
    [1, 1, 3, 3, 5, 5, 7, 9]
    """
    length = len(A)                                                 # O(1)

    for i in xrange(0, length):                                     # O(N)
        current = A[i]                                              # O(1)
        j = i - 1                                                   # O(1)

        while j >= 0 and current < A[j]:                            # O(N)
            A[j + 1] = A[j]                                         # O(1)
            j -= 1                                                  # O(1)

        A[j + 1] = current                                          # O(1)

    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
