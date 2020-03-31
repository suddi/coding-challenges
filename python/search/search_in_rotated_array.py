def get_pivot(nums):                                                # O(N)
    min_value = float('inf')                                        # O(1)
    min_position = -1                                               # O(1)
    for i, value in enumerate(nums):                                # O(N)
        if value < min_value:                                       # O(1)
            min_value = value                                       # O(1)
            min_position = i                                        # O(1)

    return (min_value, min_position)                                # O(1)

def get_mapping_function(min_position, length):                     # O(1)
    def map_to_value(position):                                     # O(1)
        return (position + min_position) % length                   # O(1)

    return map_to_value                                             # O(1)

def solution(nums, target):                                         # O(N)
    """
    Suppose an array sorted in ascending order is
    rotated at some pivot unknown to you beforehand.

    (i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]).

    You are given a target value to search.
    If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).

    >>> solution([4, 5, 6, 7, 0, 1, 2], 0)
    4
    >>> solution([4, 5, 6, 7, 0, 1, 2], 3)
    -1
    """
    _, min_position = get_pivot(nums)                               # O(N)
    length = len(nums)                                              # O(1)
    mapping_function = get_mapping_function(min_position, length)   # O(1)

    start = 0                                                       # O(1)
    end = length - 1                                                # O(1)

    if nums[mapping_function(start)] == target:                     # O(1)
        return mapping_function(start)                              # O(1)
    if nums[mapping_function(end)] == target:                       # O(1)
        return mapping_function(end)                                # O(1)

    while start < end:                                              # O(N)
        mid = (end - start) // 2                                    # O(1)

        if target == mapping_function(mid):                         # O(1)
            return mapping_function(mid)                            # O(1)

        if target > nums[mid]:                                      # O(1)
            start = mid                                             # O(1)
        else:                                                       # O(1)
            end = mid                                               # O(1)

    return -1                                                       # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
