# -*- coding: utf-8 -*-

def solution(string):                                               # O(N)
    """
    Write  a  function  to  reverse  the  order  of  words  in  a  string  in  place.

    >>> solution('this is going to be an amazing story')
    'story amazing an be to going is this'
    """
    words = string.split(' ')                                       # O(N)

    result = ''                                                     # O(1)
    while words:                                                    # O(N)
        word = words.pop()                                          # O(1)
        result = result + ' ' + word                                # O(1)

    return result.lstrip()                                          # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
