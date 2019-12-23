# -*- coding: utf-8 -*-

def solution(A, B):                                                 # O(N)
    """
    Detect whether two strings are the same, but rotated strings.
    eg. "aabbcc" and "bccaab" are the same but rotated

    >>> solution('aabbcc', 'bccaab')
    True
    >>> solution('aabbcc', 'bccaabb')
    False
    """
    length_A = len(A)                                               # O(1)
    length_B = len(B)                                               # O(1)
    if length_A != length_B:                                        # O(1)
        return False                                                # O(1)

    for _ in range(0, length_A):                                   # O(N)
        if A == B:                                                  # O(1)
            return True                                             # O(1)
        A = A[1:] + A[0]                                            # O(1)

    return False                                                    # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
