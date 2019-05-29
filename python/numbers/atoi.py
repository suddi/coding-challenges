# -*- coding: utf-8 -*-

def solution(string):                                               # O(N)
    """
    Write  a  function  to  convert  a  string  into  an  integer. 
    Return None if string is an invalid integer.

    >>> solution('123')
    123
    >>> solution('0')
    0
    >>> solution('-1243')
    -1243
    >>> solution('hello')

    >>> solution('31-12')
    """
    number_value = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }                                                               # O(1)

    is_negative = False                                             # O(1)
    result = 0                                                      # O(1)
    for count, char in enumerate(string):                           # O(N)
        value = number_value.get(char)                              # O(1)
        if count == 0 and char == '-':                              # O(1)
            is_negative = True                                      # O(1)
        elif value is None:                                         # O(1)
            return value                                            # O(1)
        else:                                                       # O(1)
            result *= 10                                            # O(1)
            result += value                                         # O(1)

    if is_negative:                                                 # O(1)
        return result * -1                                          # O(1)
    return result                                                   # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
