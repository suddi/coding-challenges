def solution(A):                                                    # O(N)
    """
    Given an array of integers find the only unique value in an array of pairs

    >>> solution([3, 2, 3, 2, 5, 4, 4])
    5
    >>> solution([3, 2, 3, 2, 5, 4, 3, 4, 8, 5, 3])
    8
    >>> solution([3, 2, 3, 2, 5, 4, 4, 5])
    """
    num = 0                                                         # O(1)
    for value in A:                                                 # O(N)
        num ^= value                                                # O(1)

    if num:                                                         # O(1)
        return num                                                  # O(1)
    return None                                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
