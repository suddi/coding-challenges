# -*- coding: utf-8 -*-

def partition(A, left, right):                                      # O(N)
    pivot = A[right]                                                # O(1)
    i = left                                                        # O(1)

    for j in range(left, right):                                   # O(N)
        if A[j] <= pivot:                                           # O(1)
            A[i], A[j] = A[j], A[i]                                 # O(1)
            i += 1                                                  # O(1)

    A[i], A[right] = A[right], A[i]                                 # O(1)
    return i                                                        # O(1)


def quick_sort(A, left, right):                                     # O(NlogN)
    if left < right:                                                # O(1)
        index = partition(A, left, right)                           # O(N)

        quick_sort(A, left, index - 1)                              # O(logN)
        quick_sort(A, index + 1, right)                             # O(logN)

def solution(A):                                                    # O(NlogN)
    """
    Sort numbers in list A using quick sort.

    >>> solution([5, 2, 2, 4, 1, 3, 7, 9])
    [1, 2, 2, 3, 4, 5, 7, 9]
    >>> solution([2, 4, 6, 2, 0, 8])
    [0, 2, 2, 4, 6, 8]
    >>> solution([1, 3, 5, 7, 3, 9, 1, 5])
    [1, 1, 3, 3, 5, 5, 7, 9]
    """
    length = len(A)                                                 # O(1)
    quick_sort(A, 0, length - 1)                                    # O(NlogN)
    return A                                                        # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
