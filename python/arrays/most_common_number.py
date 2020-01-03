def solution(A):                                                    # O(N)
    """
    Write a function to find the most common number.

    >>> solution([4, 4, -5, 3, 2, 3, 7, 7, 8, 8])
    [4, 3, 7, 8]
    >>> solution([-1, -2, -15, -1, -2, -1, -2])
    [-1, -2]
    >>> solution([1, 1, 1, 1])
    [1]
    """
    freq = {}                                                       # O(1)
    max_value = float('-inf')                                       # O(1)

    for value in A:                                                 # O(N)
        if not value in freq:                                       # O(1)
            freq[value] = 1                                         # O(1)
        else:                                                       # O(1)
            freq[value] += 1                                        # O(1)

        if freq[value] > max_value:                                 # O(1)
            max_value = freq[value]                                 # O(1)

    most_common_number = []                                         # O(1)
    for key, value in freq.items():                                 # O(N)
        if value == max_value:                                      # O(1)
            most_common_number.append(key)                          # O(1)

    return most_common_number                                       # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
