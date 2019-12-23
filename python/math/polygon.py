# -*- coding: utf-8 -*-

def solution(A):                                                    # O(N)
    """
    Identify whether four sides (given by four integers) can form a square,
    a rectangle, or neither.

    Input: You will receive an array of strings, each containing four
    space-separated integers, which represent the length of the sides
    of a polygon. The input lines will follow the 'A B C D' order as in the
    following representation:

    |-----A-----|
    |           |
    |           |
    D           B
    |           |
    |           |
    |-----C-----|
    Output: Whether the sides will form a "square", a "rectange" or some "other polygon"

    Constraints: The four integers representing the sides will be
    such that: -2000 <=X <= 2000 (Where X represents the integer)

    >>> solution('36 30 36 30')
    'rectangle'
    >>> solution('15 15 15 15')
    'square'
    >>> solution('46 96 90 100')
    'other polygon'
    >>> solution('86 86 86 86')
    'square'
    >>> solution('100 200 100 200')
    'rectangle'
    >>> solution('100 100 200 200')
    'other polygon'
    >>> solution('-100 200 -100 200')
    'other polygon'
    """
    array = [int(value) for value in A.split(' ')]                  # O(N)
    side_A = array[0]                                               # O(1)
    side_B = array[1]                                               # O(1)
    unique_values = set(array)                                      # O(N)
    num_unique_sides = len(unique_values)                           # O(1)

    if side_A < 0 or side_B < 0:                                    # O(1)
        return 'other polygon'                                      # O(1)
    if num_unique_sides == 1:                                       # O(1)
        return 'square'                                             # O(1)
    if num_unique_sides == 2:                                       # O(1)
        if side_A == side_B:                                        # O(1)
            return 'other polygon'                                  # O(1)
        return 'rectangle'                                          # O(1)
    return 'other polygon'                                          # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
