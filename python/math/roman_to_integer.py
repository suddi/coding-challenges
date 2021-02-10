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

    >>> solution('III')
    3
    >>> solution('IV')
    4
    >>> solution('IX')
    9
    >>> solution('LVIII')
    58
    >>> solution('MCMXCIV')
    1994
    >>> solution('II')
    2
    >>> solution('XII')
    12
    >>> solution('XXVII')
    27
    """
    roman_numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }                                                               # O(1)

    i = len(value) - 1                                              # O(1)
    result = 0                                                      # O(1)
    keys = roman_numerals.keys()                                    # O(1)

    while i >= 0:
        current = value[i]                                          # O(1)
        previous = ''                                               # O(1)
        if i > 0:                                                   # O(1)
            previous = value[i - 1]                                 # O(1)

        num_string = previous + current                             # O(1)
        if num_string in keys:                                      # O(1)
            i -= 2                                                  # O(1)
            result += roman_numerals[num_string]                    # O(1)
        else:                                                       # O(1)
            i -= 1                                                  # O(1)
            result += roman_numerals[current]                       # O(1)

    return result                                                   # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
