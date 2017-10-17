# -*- coding: utf-8 -*-

def solution(A, B):                                                 # O(N)
    """
    Find common elements in 2 lists.

    >>> solution([1, 2, 3, 7, 1, 5], [7, 3, 6])
    [7, 3]
    >>> solution([2, 4, 5, 10, 1, 2, 4, 4], [10, -1, 3])
    [10]
    >>> solution([4, 5, 2, 2, 1], [3, 6, -1])
    []
    """
    elements = {}                                                   # O(1)
    for value in A:                                                 # O(N)
        elements[value] = True                                      # O(1)

    common_elements = []                                            # O(1)
    for value in B:                                                 # O(N)
        if value in elements:                                       # O(1)
            common_elements.append(value)                           # O(1)

    return common_elements                                          # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
