def binary_search(array, k, pos):
    i = 0
    j = len(array) - 1

    while i < j:
        mid = ((j - i) // 2) + i

        if array[mid] > k:
            j = mid
        elif array[mid] < k:
            i = mid
        else:
            if pos == 'start':
                if mid == i or array[mid - 1] != k:
                    return mid
                j = mid
            elif pos == 'end':
                if mid == j or array[mid + 1] != k:
                    return mid
                elif mid + 1 == j and array[mid + 1] == k:
                    return mid + 1
                i = mid

def solution(array, k):
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
    length = len(array)
    if not length:
        return 0

    start = binary_search(array, k, 'start')
    end = binary_search(array, k, 'end')

    return end - start + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
