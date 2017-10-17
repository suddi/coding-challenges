# -*- coding: utf-8 -*-

def solution(A):                                                    # O(N)
    """
    Return a given array in Zig Zag fashion.

    >>> solution([4, 3, 7, 8, 6, 2, 1])
    [3, 7, 4, 8, 2, 6, 1]
    >>> solution([1, 4, 3, 2])
    [1, 4, 2, 3]
    >>> solution([3])
    [3]
    >>> solution([3, 2])
    [2, 3]
    """
    length = len(A)                                                 # O(1)
    if length < 2:                                                  # O(1)
        return A                                                    # O(1)

    i = 0                                                           # O(1)
    greater_than = True                                             # O(1)
    while i < length - 1:                                           # O(N)
        if greater_than:                                            # O(1)
            if A[i] > A[i + 1]:                                     # O(1)
                A[i], A[i + 1] = A[i + 1], A[i]                     # O(1)
            greater_than = False                                    # O(1)
        else:                                                       # O(1)
            if A[i] < A[i + 1]:                                     # O(1)
                A[i], A[i + 1] = A[i + 1], A[i]                     # O(1)
            greater_than = True                                     # O(1)
        i += 1                                                      # O(1)

    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
