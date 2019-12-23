# -*- coding: utf-8 -*-

def solution(number):                                               # O(N)
    """
    Write a function to calculate the factorial of a number

    >>> solution(0)
    1
    >>> solution(1)
    1
    >>> solution(6)
    720
    """
    m = {
        0: 1,
        1: 1
    }                                                               # O(1)

    for i in range(2, number + 1):                                 # O(N)
        m[i] = i * m[i - 1]                                         # O(1)

    return m[number]                                                # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
