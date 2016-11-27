# -*- coding: utf-8 -*-

def solution(a):
    """
    Write a function to reverse a list without using the built-in function.

    >>> solution([1, 2, 3, 4, 5, 6, 7])
    [7, 6, 5, 4, 3, 2, 1]
    """
    i = 0                                                           # O(1)
    j = len(a) - 1                                                  # O(1)

    while i < j:                                                    # O(N/2)
        a[i], a[j] = [a[j], a[i]]                                   # O(1)
        i += 1                                                      # O(1)
        j -= 1                                                      # O(1)
    return a                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
