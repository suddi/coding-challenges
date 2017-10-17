# -*- coding: utf-8 -*-

def solution(A):                                                    # O(NlogN)
    """
    Given a list of tuples, merge the tuples to show only the non-overlapping intervals.

    >>> solution([(1, 3), (2, 6), (8, 10), (15, 18)])
    [(1, 6), (8, 10), (15, 18)]
    >>> solution([(1, 4), (4, 8), (2, 5), (14, 19)])
    [(1, 8), (14, 19)]
    """
    A.sort(key=lambda value: value[0])                              # O(NlogN)
    merged = []                                                     # O(1)
    target = ()                                                     # O(1)

    for i in A:                                                     # O(N)
        if not target:                                              # O(1)
            target = i                                              # O(1)
        elif target[1] >= i[0]:                                     # O(1)
            target = (target[0], max(target[1], i[1]))              # O(1)
        else:                                                       # O(1)
            merged.append(target)                                   # O(1)
            target = i                                              # O(1)

    if target:                                                      # O(1)
        merged.append(target)                                       # O(1)

    return merged                                                   # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
