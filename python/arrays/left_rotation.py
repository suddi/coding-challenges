def solution1(A, k):                                                 # O(N^2)
    """
    Write a function to left rotate a list a by k number of times.
    eg. [1, 2, 3]
        if k = 1, then result = [2, 3, 1]
        if k = 2, then result = [3, 1, 2]

    >>> solution1([1, 2, 3, 4, 5], 4)
    [5, 1, 2, 3, 4]
    >>> solution1([1, 2, 3], 1)
    [2, 3, 1]
    >>> solution1([1, 2, 3], 2)
    [3, 1, 2]
    >>> solution1([1, 2, 3], 22)
    [2, 3, 1]
    """
    def rotate(value):                                              # O(N)
        v = value.pop(0)                                            # O(N)
        value.append(v)                                             # O(1)
        return value                                                # O(1)

    for _i in range(0, k):                                          # O(N)
        A = rotate(A)                                               # O(N)
    return A                                                        # O(1)

def solution2(A, k):                                                # O(N)
    """
    Write a function to left rotate a list a by k number of times.
    eg. [1, 2, 3]
        if k = 1, then result = [2, 3, 1]
        if k = 2, then result = [3, 1, 2]

    >>> solution2([1, 2, 3, 4, 5], 4)
    [5, 1, 2, 3, 4]
    >>> solution2([1, 2, 3], 1)
    [2, 3, 1]
    >>> solution2([1, 2, 3], 2)
    [3, 1, 2]
    >>> solution2([1, 2, 3], 22)
    [2, 3, 1]
    """
    output = []                                                     # O(1)

    for i in range(0, len(A)):                                      # O(N)
        output.append(None)                                         # O(1)

    for i, value in enumerate(A):                                   # O(N)
        pos = (len(A) - k + i) % len(A)                             # O(1)
        output[pos] = value                                         # O(1)

    return output                                                   # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
