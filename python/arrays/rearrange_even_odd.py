def solution(A):                                                    # O(N)
    """
    Given a variable length array of integers, partition them such that the even
    integers precede the odd integers in the array. Your must operate on the array
    in-place, with a constant amount of extra space. The answer should scale
    linearly in time with respect to the size of the array.

    >>> solution([7, 7, 4, 0, 9, 8, 2, 4, 1, 9])
    [4, 2, 4, 0, 8, 9, 7, 7, 1, 9]
    """
    i = 0                                                           # O(1)
    j = len(A) - 1                                                  # O(1)
    while i < j:                                                    # O(<N)
        if A[i] % 2 == 0:                                           # O(1)
            i += 1                                                  # O(1)

        if A[j] % 2 == 1:                                           # O(1)
            j -= 1                                                  # O(1)

        if A[i] % 2 == 1 and A[j] % 2 == 0:                         # O(1)
            A[i], A[j] = A[j], A[i]                                 # O(1)
            i += 1                                                  # O(1)
            j -= 1                                                  # O(1)

    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
