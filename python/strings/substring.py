# -*- coding: utf-8 -*-

def solution(x, y):                                                 # O(N)
    """
    Write  a  program  to  determine  whether  an  input  string  x  is  a  substring  of 
    another  input  string  y.

    >>> solution('bat', 'abate')
    True
    >>> solution('bat', 'beat')
    False
    >>> solution('', 'hello')
    False
    >>> solution('bat', 'cwwbababolbatpo')
    True
    >>> solution('bat', 'cwwbababolbaipo')
    False
    """
    if not x or not y:
        return False

    i = 0                                                           # O(1)
    j = 0                                                           # O(1)

    length_x = len(x)                                               # O(1)
    length_y = len(y)                                               # O(1)

    while i < length_x and j < length_y:                            # O(N)
        if x[i] != y[j]:                                            # O(1)
            i = 0                                                   # O(1)
            j += 1                                                  # O(1)
        else:                                                       # O(1)
            i += 1                                                  # O(1)
            j += 1                                                  # O(1)

    if i == length_x:                                               # O(1)
        return True                                                 # O(1)
    return False                                                    # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
