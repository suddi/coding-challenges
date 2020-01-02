# -*- coding: utf-8 -*-

def heapify(A, length, index):                                      # O(logN)
    smallest = index                                                # O(1)
    left = 2 * index + 1                                            # O(1)
    right = 2 * index + 2                                           # O(1)

    if left < length and A[index] > A[left]:                        # O(1)
        smallest = left                                             # O(1)

    if right < length and A[smallest] > A[right]:                   # O(1)
        smallest = right                                            # O(1)

    if smallest != index:                                           # O(1)
        A[index], A[smallest] = A[smallest], A[index]               # O(1)
        heapify(A, length, smallest)                                # O(logN)

def solution(A):                                                    # O(NlogN)
    """
    Build a min heap

    >>> solution([4, 10, 3, 5, 1])
    [1, 4, 3, 5, 10]
    """
    length = len(A)                                                 # O(1)

    for i in range(length - 1, -1, -1):                             # O(N)
        heapify(A, length, i)                                       # O(logN)
    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
