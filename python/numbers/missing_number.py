def solution(A):                                                    # O(N)
    """
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
    find the one that is missing from the array.

    Your algorithm should run in linear runtime complexity.
    Could you implement it using only constant extra space complexity?

    >>> solution([3, 0, 1])
    2
    >>> solution([9, 6, 4, 2, 3, 5, 7, 0, 1])
    8
    """
    length = len(A)                                                 # O(1)
    summed_value = 0                                                # O(1)
    total = 0                                                       # O(1)
    for i in range(0, length + 1):                                  # O(N)
        summed_value += i                                           # O(1)
        if i < length:                                              # O(1)
            total += A[i]                                           # O(1)

    return summed_value - total                                     # O(N)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
