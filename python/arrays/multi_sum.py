def solution(A, target):                                            # O(N)
    """
    Write a function that will return True if consecutive values in provided list A
    adds up to the target.

    >>> solution([5, 7, 3, 4, 5], 12)
    True
    >>> solution([5, 3, 2], 6)
    False
    >>> solution([1, 5, 4, -1, 12, 10, 1], 8)
    True
    """
    array = []                                                      # O(1)
    lookup_array = {}                                               # O(1)

    summed_value = 0                                                # O(1)
    for value in A:                                                 # O(N)
        summed_value += value                                       # O(1)
        if summed_value == target:                                  # O(1)
            return True                                             # O(1)
        array.append(summed_value)                                  # O(1)
        lookup_array[summed_value] = True                           # O(1)

    length = len(array)                                             # O(1)
    for i in range(length - 1, -1, -1):                             # O(N)
        value = array[i]                                            # O(1)
        lookup_value = value - target                               # O(1)
        if lookup_value in lookup_array:                            # O(1)
            return True                                             # O(1)

    return False                                                    # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
