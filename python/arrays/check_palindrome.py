# -*- coding: utf-8 -*-

def solution(A):                                                    # O(N/2)
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
    j = len(A) - 1                                                  # O(1)

    while i < j:                                                    # O(N/2)
        if A[i] != A[j]:                                            # O(1)
            return False                                            # O(1)
        i += 1                                                      # O(1)
        j -= 1                                                      # O(1)
    return True                                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
