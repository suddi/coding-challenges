def solution(A):                                                    # O(N)
    """
    Given an array find the first non-repeating integers in the array

    >>> solution([3, 2, 3, 2, 5, 4, 3, 4])
    5
    >>> solution([3, 2, 3, 2, '%', 5, 4, 'd', 3, 4])
    5
    >>> solution([3, 2, 3, 2, 5, 4, 3, 4, 8])
    5
    >>> solution([3, 2, 3, 2, 5, 4, 3, 4, 5])
    """
    occurrences = {}                                                # O(1)
    for count, value in enumerate(A):                               # O(N)
        if isinstance(value, int):                                  # O(1)
            if value in occurrences:                                # O(1)
                occurrences[value]['count'] += 1                    # O(1)
            else:                                                   # O(1)
                occurrences[value] = {
                    'position': count,
                    'count': 1
                }                                                   # O(1)

    first_value = None                                              # O(1)
    min_position = float('inf')                                     # O(1)
    for key, value in occurrences.items():                          # O(N)
        if value['count'] == 1:                                     # O(1)
            if not first_value:                                     # O(1)
                first_value = key                                   # O(1)
                min_position = value['position']                    # O(1)
            elif value['position'] < min_position:                  # O(1)
                first_value = key                                   # O(1)
                min_position = value['position']                    # O(1)

    return first_value                                              # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
