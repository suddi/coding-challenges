# -*- coding: utf-8 -*-

def solution(a, b):
    """
    Detect whether two strings are the same, but rotated strings.
    eg. "aabbcc" and "bccaab" are the same but rotated

    >>> solution('aabbcc', 'bccaab')
    True
    >>> solution('aabbcc', 'bccaabb')
    False
    """
    length_a = len(a)                                               # O(1)
    length_b = len(b)                                               # O(1)
    if (length_a != length_b):                                      # O(1)
        return False                                                # O(1)

    for i in xrange(0, length_a):                                   # O(N)
        if a == b:                                                  # O(1)
            return True                                             # O(1)
        a = a[1:] + a[0]                                            # O(1)

    return False                                                    # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
