# -*- coding: utf-8 -*-

def solution(S):
    """
    Given that a valid password requires an upper case character and must not contain a digit.
    Write a function to compute the longest valid password from a given string.
    eg. "a0B0cdAg1", longest valid password is "cdAg".

    >>> solution('aabb2323Afefv424')
    5
    >>> solution('a0B0cdAg1')
    4
    """
    password_length = 0                                             # O(1)
    password_valid = False                                          # O(1)
    password_lengths = []                                           # O(1)

    def validate_password():
        if password_valid:                                          # O(1)
            password_lengths.append(password_length)                # O(1)
        return password_lengths                                     # O(1)

    for value in S:                                                 # O(N)
        if value.isupper():                                         # O(1)
            password_valid = True                                   # O(1)
            password_length += 1                                    # O(1)
        elif value.isdigit():                                       # O(1)
            validate_password()                                     # O(1)
            password_valid = False                                  # O(1)
            password_length = 0                                     # O(1)
        else:                                                       # O(1)
            password_length += 1                                    # O(1)

    validate_password()                                             # O(1)
    max_len = -1                                                    # O(1)
    for length in password_lengths:                                 # O(<N)
        if length > max_len:                                        # O(1)
            max_len = length                                        # O(1)
    return max_len                                                  # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
