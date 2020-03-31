def solution(a, b):                                                 # O(1)
    """
    Calculate the sum of two integers a and b,
    but you are not allowed to use the operator + and -.

    >>> solution(2, 3)
    5
    """
    while b != 0:                                                   # O(1)
        # carry now contains common set bits of a and b
        carry = a & b                                               # O(1)

        # Sum of bits of a and b where at east one of the bits is not set
        a = a ^ b                                                   # O(1)

        # Carry is shifted by one so that adding it to b gives the required sum
        b = carry << 1                                              # O(1)

    return a                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
