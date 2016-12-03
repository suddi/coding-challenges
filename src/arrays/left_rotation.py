# -*- coding: utf-8 -*-

def solution(a, k):                                                 # O(N^2)
    """
    Write a function to left rotate a list a by k number of times.
    eg. [1, 2, 3]
        if k = 1, then result = [2, 3, 1]
        if k = 2, then result = [3, 1, 2]

    >>> solution([1, 2, 3, 4, 5], 4)
    [5, 1, 2, 3, 4]
    """
    def rotate(value):                                              # O(N)
        v = value.pop(0)                                            # O(N)
        value.append(v)                                             # O(1)
        return value                                                # O(1)

    for i in range(0, k):                                           # O(N)
        a = rotate(a)                                               # O(N)
    return a                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
