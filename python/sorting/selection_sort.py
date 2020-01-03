def solution(A):                                                    # O(N^2)
    """
    Sort numbers in list A using selection sort.

    >>> solution([5, 2, 2, 4, 1, 3, 7, 9])
    [1, 2, 2, 3, 4, 5, 7, 9]
    >>> solution([2, 4, 6, 2, 0, 8])
    [0, 2, 2, 4, 6, 8]
    >>> solution([1, 3, 5, 7, 3, 9, 1, 5])
    [1, 1, 3, 3, 5, 5, 7, 9]
    """
    length = len(A)                                                 # O(1)

    for i in range(0, length - 1):                                  # O(N)
        current_min = i                                             # O(1)
        for j in range(i + 1, length):                              # O(N)
            if A[j] < A[current_min]:                               # O(1)
                current_min = j                                     # O(1)

        if current_min != i:                                        # O(1)
            A[current_min], A[i] = A[i], A[current_min]             # O(1)

    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
