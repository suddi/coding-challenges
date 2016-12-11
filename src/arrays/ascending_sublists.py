# -*- coding: utf-8 -*-

def solution(A):                                                    # O(N)
    """
    Write a function to group together all ascending sublists within a list a.

    >>> solution([1, 2, 10, 10, 8, 12, 5, 23, 1])
    [[1, 2, 10, 10], [8, 12], [5, 23], [1]]
    >>> solution([3, 4, 5, 12, 2, 3, 5, 2, 5, -1])
    [[3, 4, 5, 12], [2, 3, 5], [2, 5], [-1]]
    """
    output = []                                                     # O(1)
    inner = []                                                      # O(1)

    for value in A:                                                 # O(N)
        if not inner or value >= inner[-1]:                         # O(1)
            inner.append(value)                                     # O(1)
        elif value < inner[-1]:                                     # O(1)
            output.append(inner)                                    # O(1)
            inner = [value]                                         # O(1)

    if inner:                                                       # O(1)
        output.append(inner)                                        # O(1)

    return output                                                   # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
