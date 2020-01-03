def solution(number):                                               # O(N)
    """
    Write a function to compute the fibonacci sequence value to the requested iteration.

    >>> solution(3)
    2
    >>> solution(10)
    55
    >>> solution(20)
    6765
    """
    m = {
        0: 0,
        1: 1
    }                                                               # O(1)

    for i in range(2, number + 1):                                  # O(N)
        m[i] = m[i - 1] + m[i - 2]                                  # O(1)

    return m[number]                                                # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
