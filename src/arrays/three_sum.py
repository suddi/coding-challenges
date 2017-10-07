# -*- coding: utf-8 -*-

def solution(A, summed_value):                                      # O(N^2)
    """
    Write a function that will return the numbers used to add up to a certain value.

    >>> solution([-2, 0, 1, 3], 2)
    [(-2, 1, 3)]
    >>> solution([5, 1, 3, 4, 7], 12)
    [(1, 4, 7), (3, 4, 5)]
    >>> solution([1, 2], 3)
    []
    """
    length = len(A)                                                 # O(1)
    result = []                                                     # O(1)

    if not A or length < 3:                                         # O(1)
        return result                                               # O(1)

    A.sort()                                                        # O(NlogN)
    for i, _ in enumerate(A):                                       # O(N)
        j = i + 1                                                   # O(1)
        k = length - 1                                              # O(1)

        while j < k:                                                # O(N)
            computed = A[i] + A[j] + A[k]                           # O(1)
            if computed == summed_value:                            # O(1)
                result.append((A[i], A[j], A[k]))                   # O(1)
                j += 1                                              # O(1)
                k -= 1                                              # O(1)
            elif computed < summed_value:                           # O(1)
                j += 1                                              # O(1)
            elif computed > summed_value:                           # O(1)
                k -= 1                                              # O(1)

    return result                                                   # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
