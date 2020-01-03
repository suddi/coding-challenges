def solution(nums, val):                                            # O(N)
    """
    Given an array nums and a value val, remove all instances of that value
    in-place and return the new length.

    >>> solution([3, 2, 2, 3], 3)
    2
    >>> solution([0, 1, 2, 2, 3, 0, 4, 2], 2)
    5
    >>> solution([2], 3)
    1
    >>> solution([3, 3], 5)
    2
    """
    if len(nums) == 1 and nums[0] != val:                           # O(1)
        return 1                                                    # O(1)

    i = 0                                                           # O(1)
    j = len(nums) - 1                                               # O(1)

    while i <= j:                                                   # O(N)
        if nums[i] == val and nums[j] != val:                       # O(1)
            nums[i], nums[j] = nums[j], nums[i]                     # O(1)
            i += 1                                                  # O(1)
            j -= 1                                                  # O(1)

        if nums[i] != val:                                          # O(1)
            i += 1                                                  # O(1)

        if nums[j] == val:                                          # O(1)
            j -= 1                                                  # O(1)

    return i                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
