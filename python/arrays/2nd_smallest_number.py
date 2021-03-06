def solution_1(A):                                                  # O(N)
    """
    Write a function to find the 2nd smallest number in a list.

    >>> solution_1([4, 4, -5, 3, 2, 3, 7, 7, 8, 8])
    2
    >>> solution_1([-1, -2, -15, -1, -2, -1, -2])
    -2
    >>> solution_1([1, 1, 1, 1])
    """
    min_1 = None                                                    # O(1)
    min_2 = None                                                    # O(1)

    for value in A:                                                 # O(N)
        if not min_1:                                               # O(1)
            min_1 = value                                           # O(1)
        elif value < min_1:                                         # O(1)
            min_1, min_2 = value, min_1                             # O(1)
        elif value > min_1:                                         # O(1)
            if not min_2 or value < min_2:                          # O(1)
                min_2 = value                                       # O(1)

    return min_2                                                    # O(1)

def solution_2(A):                                                  # O(N)
    """
    Write a function to find the 2nd smallest number in a list.

    >>> solution_2([4, 4, -5, 3, 2, 3, 7, 7, 8, 8])
    2
    >>> solution_2([-1, -2, -15, -1, -2, -1, -2])
    -2
    >>> solution_2([1, 1, 1, 1])
    1
    """
    min_1 = float('inf')                                            # O(1)
    min_2 = float('inf')                                            # O(1)

    for value in A:                                                 # O(N)
        if value <= min_1:                                          # O(1)
            min_1, min_2 = value, min_1                             # O(1)
        elif value < min_2:                                         # O(1)
            min_2 = value                                           # O(1)

    return min_2                                                    # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
