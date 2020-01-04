def solution(A):                                                    # O(N)
    """
    Given an array A, multiply each of the values by all of the other
    values in the array except itself.

    >>> solution([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]
    """
    length = len(A)                                                 # O(1)
    if not length:                                                  # O(1)
        return 0                                                    # O(1)

    multiplication = 1                                              # O(1)
    for value in A:                                                 # O(N)
        multiplication *= value                                     # O(1)

    for i in range(0, length):                                      # O(N)
        A[i] = int(multiplication / A[i])                           # O(1)

    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
