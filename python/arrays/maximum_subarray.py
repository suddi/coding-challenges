def solution(A):                                                    # O(N)
    """
    Given an integer array nums, find the contiguous subarray
    (containing at least one number) which has the largest sum and
    return its sum.

    >>> solution([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> solution([-2, -1, -3, 1])
    1
    """
    summed_values = []                                              # O(1)
    summed_value = 0                                                # O(1)

    for value in A:                                                 # O(N)
        summed_value += value                                       # O(1)
        summed_values.append(summed_value)                          # O(1)

    min_point = float('inf')                                        # O(1)
    largest_sum = 0                                                 # O(1)

    for value in summed_values:                                     # O(N)
        if value < min_point:                                       # O(1)
            min_point = value                                       # O(1)
        elif value - min_point > largest_sum:                       # O(1)
            largest_sum = value - min_point                         # O(1)

    return largest_sum                                              # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
