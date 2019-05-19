# -*- coding: utf-8 -*-

def solution(value):                                                # O(N)
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    eg.
    - 2 is written as II in Roman numeral, just two one's added together.
    - 12 is written as, XII, which is simply X + II.
    - 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, the number four is written as IV.
    Because the one is before the five we subtract it making four.
    The same principle applies to the number nine, which is written as IX.
    There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.
    Input is guaranteed to be within the range from 1 to 3999.

    >>> solution(3)
    'III'
    >>> solution(4)
    'IV'
    >>> solution(9)
    'IX'
    >>> solution(58)
    'LVIII'
    >>> solution(1994)
    'MCMXCIV'
    >>> solution(2)
    'II'
    >>> solution(12)
    'XII'
    >>> solution(27)
    'XXVII'
    """
    roman_numerals = [                                              # O(1)
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    output = ''                                                     # O(1)

    for mapping in roman_numerals:                                  # O(N)
        multiple = value / mapping[0]                               # O(1)
        output += mapping[1] * multiple                             # O(1)
        value = value % mapping[0]                                  # O(1)

    return output                                                   # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
