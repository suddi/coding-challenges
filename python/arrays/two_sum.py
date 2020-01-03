def solution(A, target):                                            # O(N)
    """
    Write a function that will return the indexes to be used to add up numbers
    to reach a given target.

    >>> solution([1, 2, 3, 4, 5], 5)
    [1, 2]
    >>> solution([5, 3, 2], 6)
    []
    """
    remaining = {}                                                  # O(1)

    for count, value in enumerate(A):                               # O(N)
        if value in remaining:                                      # O(1)
            return [remaining[value], count]                        # O(1)
        remaining[target - value] = count                           # O(1)

    return []                                                       # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
