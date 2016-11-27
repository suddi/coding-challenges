# -*- coding: utf-8 -*-

def solution(a):
    """
    Write a function to check if the input string is a palindrome.
    A palindrome is defined a string that reads the same backwards and forwards.

    >>> solution('citic')
    True
    >>> solution('thisisapalindromemordnilapasisiht')
    True
    >>> solution('thisisnotapalindrome')
    False
    """
    i = 0                                                           # O(1)
    j = len(a) - 1                                                  # O(1)

    while i < j:                                                    # O(N/2)
        if a[i] != a[j]:                                            # O(1)
            return False                                            # O(1)
        i += 1                                                      # O(1)
        j -= 1                                                      # O(1)
    return True                                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
