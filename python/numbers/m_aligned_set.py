def solution(A, M):                                                 # O(M + N)
    """
    Given a set of numbers A (eg. [-3, -2, 1, 0, 8, 7, 1]),
    and another number M (eg. 3)

    Find the largest subset you can form with numbers that are a
    multiple of M different from each other.

    In the example above, 4 is the answer with the subset [-2, 1, 7, 1].
    Each of these numbers are a subset of 3 different from each other.

    >>> solution([-3, -2, 1, 0, 8, 7, 1], 3)
    4
    """
    remainders = []                                                 # O(1)
    for _ in range(0, M):                                           # O(M)
        remainders.append(0)                                        # O(1)

    for value in A:                                                 # O(N)
        remainder = value % M                                       # O(1)
        remainders[remainder] += 1                                  # O(1)

    return max(remainders)                                          # O(N)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
