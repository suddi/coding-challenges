def solution(A):                                                    # O(N/2)
    """
    Write a function to reverse a list without affecting special characters and
    without using the built-in function.

    >>> solution(['a', ',', 'b', '$', 'c'])
    ['c', ',', 'b', '$', 'a']
    >>> solution(['A', 'b', ',', 'c', ',', 'd', 'e', '!', '$'])
    ['e', 'd', ',', 'c', ',', 'b', 'A', '!', '$']
    """
    i = 0                                                           # O(1)
    j = len(A) - 1                                                  # O(1)

    while i < j:                                                    # O(N/2)
        if not A[i].isalpha():                                      # O(1)
            i += 1                                                  # O(1)

        if not A[j].isalpha():                                      # O(1)
            j -= 1                                                  # O(1)

        if A[i].isalpha() and A[j].isalpha():                       # O(1)
            A[i], A[j] = A[j], A[i]                                 # O(1)
            i += 1                                                  # O(1)
            j -= 1                                                  # O(1)
    return A                                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
