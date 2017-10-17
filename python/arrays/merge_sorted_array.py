# -*- coding: utf-8 -*-

def solution(A, B):                                                 # O(N)
    """
    Create a sorted list out of two sorted sub-lists.
    You cannot use library methods and sorted data structures like TreeSets to sort.
    You can assume that all elements are greater zero.

    >>> solution([1, 2, 10, 10, 10], [2, 8, 12])
    [1, 2, 2, 8, 10, 10, 10, 12]
    >>> solution([1], [2, 2, 2, 2])
    [1, 2, 2, 2, 2]
    >>> solution([1, 1, 1, 1], [2, 2, 2, 2])
    [1, 1, 1, 1, 2, 2, 2, 2]
    """
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
