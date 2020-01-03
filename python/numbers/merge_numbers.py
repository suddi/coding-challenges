def solution(A, B):                                                 # O(M+N)
    """
    Write a function to combine 2 numbers such that numbers are merged by their position.
    eg. 111 and 222 becomes 121212

    >>> solution(1000, 2321)
    12030201

    >>> solution(10000, 10000)
    -1

    >>> solution(1111111, 2)
    12111111
    """
    A = str(A)                                                      # O(len(A))
    B = str(B)                                                      # O(len(B))
    length_A = len(A)                                               # O(1)
    length_B = len(B)                                               # O(1)

    if length_A + length_B >= len('100000000'):                     # O(1)
        return -1                                                   # O(1)

    i = 0                                                           # O(1)
    j = 0                                                           # O(1)
    C = ''                                                          # O(1)
    flag = True                                                     # O(1)
    while i < length_A or j < length_B:                             # O(len(A) + len(B))
        if flag:                                                    # O(1)
            C += A[i]                                               # O(1)
            i += 1                                                  # O(1)
            if j < length_B:                                        # O(1)
                flag = False                                        # O(1)
        else:                                                       # O(1)
            C += B[j]                                               # O(1)
            j += 1                                                  # O(1)
            if i < length_A:                                        # O(1)
                flag = True                                         # O(1)
    return int(C)                                                   # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
