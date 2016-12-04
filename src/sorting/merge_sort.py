# -*- coding: utf-8 -*-

def get_list(A, start, finish):                                     # O(N)
    new_list = [0] * (finish - start + 1)                           # O(N)
    for i in xrange(start, finish + 1):                             # O(N)
        new_list[i - start] = A[i]                                  # O(1)
    return new_list                                                 # O(N)

def apply_sort(A, B):                                               # O(N)
    len_A = len(A)                                                  # O(1)
    len_B = len(B)                                                  # O(1)
    i = 0                                                           # O(1)
    j = 0                                                           # O(1)
    output = []                                                     # O(1)

    def compile_rest(array, index, length):                         # O(N)
        compiled = []                                               # O(1)
        if index != length:                                         # O(1)
            for x in xrange(index, length):                         # O(N)
                compiled.append(array[x])                           # O(1)
        return compiled                                             # O(1)

    while i < len_A and j < len_B:                                  # O(N)
        if A[i] <= B[j]:                                            # O(1)
            output.append(A[i])                                     # O(1)
            i += 1                                                  # O(1)
        else:                                                       # O(1)
            output.append(B[j])                                     # O(1)
            j += 1                                                  # O(1)

    output.extend(compile_rest(A, i, len_A))                        # O(N)
    output.extend(compile_rest(B, j, len_B))                        # O(N)

    return output                                                   # O(1)

def merge(A, B, left, right):                                       # O(N)
    for i in xrange(left, right + 1):                               # O(N)
        A[i] = B[i - left]                                          # O(1)

def merge_sort(A, left, right):
    if left < right:                                                # O(1)
        middle = left + ((right - left) / 2)                        # O(1)

        merge_sort(A, left, middle)                                 # O(NlogN)
        merge_sort(A, middle + 1, right)                            # O(NlogN)

        left_list = get_list(A, left, middle)                       # O(N)
        right_list = get_list(A, middle + 1, right)                 # O(N)

        new_list = apply_sort(left_list, right_list)                # O(N)
        merge(A, new_list, left, right)                             # O(N)

def solution(A):                                                    # O(NlogN)
    """
    Sort numbers in list A using merge sort.

    >>> solution([5, 2, 2, 4, 1, 3, 7, 9])
    [1, 2, 2, 3, 4, 5, 7, 9]
    >>> solution([2, 4, 6, 2, 0, 8])
    [0, 2, 2, 4, 6, 8]
    >>> solution([1, 3, 5, 7, 3, 9, 1, 5])
    [1, 1, 3, 3, 5, 5, 7, 9]
    """
    length = len(A)                                                 # O(1)
    merge_sort(A, 0, length - 1)                                    # O(NlogN)
    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
