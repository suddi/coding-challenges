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
    array = [int(value) for value in A.split(' ')]
    side_A = array[0]
    side_B = array[1]
    unique_values = set(array)
    num_unique_sides = len(unique_values)

    if side_A < 0 or side_B < 0:
        return 'other polygon'
    elif num_unique_sides == 1:
        return 'square'
    elif num_unique_sides == 2:
        if side_A == side_B:
            return 'other polygon'
        return 'rectangle'
    else:
        return 'other polygon'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
