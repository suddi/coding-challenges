# -*- coding: utf-8 -*-

def solution(number):                                               # O(N)
    """
    Write a function to compute the fibonacci sequence value to the requested iteration.

    >>> solution(3)
    2
    >>> solution(10)
    55
    >>> solution(20)
    6765
    """
    m = {
        0: 0,
        1: 1
    }                                                               # O(1)

    def run_sequence(n):                                            # O(N)
        if not isinstance(m.get(n), int):                           # O(1)
            m[n] = run_sequence(n - 1) + run_sequence(n - 2)        # O(N)
        return m[n]                                                 # O(1)

    return run_sequence(number)                                     # O(N)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
