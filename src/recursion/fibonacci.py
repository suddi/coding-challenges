# -*- coding: utf-8 -*-

def solution(number):                                               # O(M+N)
    """
    Write a function to compute the fibonacci sequence value to the requested iteration.

    >>> solution(3)
    2
    >>> solution(10)
    55
    >>> solution(20)
    6765
    """
    if number == 0:                                                 # O(1)
        return 0                                                    # O(1)
    elif number == 1:                                               # O(1)
        return 1                                                    # O(1)
    else:                                                           # O(1)
        return solution(number - 1) + solution(number - 2)          # O(M+N)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
