def solution(array):                                                # O(N)
    """
    Given n non-negative integers a1, a2, ..., an , where each represents
    a point at coordinate (i, ai). n vertical lines are drawn such that the
    two endpoints of line i is at (i, ai) and (i, 0).

    Find two lines, which together with x-axis forms a container,
    such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

    >>> solution([1, 8, 6, 2, 5, 4, 8, 3, 7])
    49
    >>> solution([1, 1, 1, 1, 100, 100, 1, 1, 1, 1])
    100
    """
    length = len(array)                                             # O(1)
    max_area = length - 1 * min(array[0], array[length - 1])        # O(1)

    i = 0                                                           # O(1)
    j = length - 1                                                  # O(1)
    while i < j:                                                    # O(N)
        if array[i] <= array[j]:                                    # O(1)
            i += 1                                                  # O(1)
        else:                                                       # O(1)
            j -= 1                                                  # O(1)
        area = (j - i) * min(array[i], array[j])                    # O(1)
        if area > max_area:                                         # O(1)
            max_area = area                                         # O(1)

    return max_area                                                 # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
