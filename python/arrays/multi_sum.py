# -*- coding: utf-8 -*-

def solution(A, target):                                            # O(N)
    """
    Write a function that will return True if consecutive values in provided list A
    adds up to the target.

    >>> solution([5, 7, 3, 4, 5], 12)
    True
    >>> solution([5, 3, 2], 6)
    False
    """
    i = 0                                                           # O(1)
    total = 0                                                       # O(1)
    for value in A:                                                 # O(N)
        if total == target:                                         # O(1)
            return True                                             # O(1)
        elif total < target:                                        # O(1)
            total += value                                          # O(1)
        else:                                                       # O(1)
            total -= A[i]                                           # O(1)
            i += 1                                                  # O(1)

    if total == target:                                             # O(1)
        return True                                                 # O(1)
    return False                                                    # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
