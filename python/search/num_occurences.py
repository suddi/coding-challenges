def binary_search(array, k, pos):                                   # O(logN)
    i = 0                                                           # O(1)
    j = len(array) - 1                                              # O(1)

    while i < j:                                                    # O(logN)
        mid = ((j - i) // 2) + i                                    # O(1)

        if array[mid] > k:                                          # O(1)
            j = mid                                                 # O(1)
        elif array[mid] < k:                                        # O(1)
            i = mid                                                 # O(1)
        else:                                                       # O(1)
            if pos == 'start':                                      # O(1)
                if mid == i or array[mid - 1] != k:                 # O(1)
                    return mid                                      # O(1)
                j = mid                                             # O(1)
            elif pos == 'end':                                      # O(1)
                if mid == j or array[mid + 1] != k:                 # O(1)
                    return mid                                      # O(1)

                if mid + 1 == j and array[mid + 1] == k:            # O(1)
                    return mid + 1                                  # O(1)
                i = mid                                             # O(1)

def solution(array, k):                                             # O(logN)
    """
    Given a sorted array, get the number of occurences of k

    # >>> solution([1, 1, 1, 2, 3], 1)
    # 3
    # >>> solution([1, 2, 3, 4, 4, 4], 3)
    # 1
    >>> solution([1, 1, 1, 1, 1], 1)
    5
    >>> solution([], 1)
    0
    """
    length = len(array)                                             # O(1)
    if not length:                                                  # O(1)
        return 0                                                    # O(1)

    start = binary_search(array, k, 'start')                        # O(logN)
    end = binary_search(array, k, 'end')                            # O(logN)

    return end - start + 1                                          # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
