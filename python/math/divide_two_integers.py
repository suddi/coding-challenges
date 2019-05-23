# -*- coding: utf-8 -*-

def solution(dividend, divisor):                                    # O(N)
    """
    Given two integers dividend and divisor, divide two integers without
    using multiplication, division and mod operator.

    >>> solution(10, 3)
    3
    >>> solution(7, -3)
    -2
    >>> solution(2, 3)
    0
    >>> solution(1, 1)
    1
    >>> solution(-2147483648, -1)
    2147483648
    """
    if divisor == 1:                                                # O(1)
        return dividend                                             # O(1)
    elif divisor == -1:                                             # O(1)
        return -dividend                                            # O(1)

    def get_operation(a, b):                                        # O(1)
        if (a > 0 and b < 0) or (a < 0 and b > 0):                  # O(1)
            return 'add'                                            # O(1)
        return 'subtract'                                           # O(1)

    def get_limit(a, b):                                            # O(1)
        if (b >= 0 and a > 0) or (b <= 0 and a < 0):                  # O(1)
            return True                                             # O(1)
        return False                                                # O(1)

    operation = get_operation(dividend, divisor)                    # O(1)
    i = dividend                                                    # O(1)
    count = 0                                                       # O(1)
    while get_limit(dividend, i):                                   # O(N)
        if operation == 'add':                                      # O(1)
            i += divisor                                            # O(1)
            if get_limit(dividend, i):                              # O(1)
                count -= 1                                          # O(1)
        elif operation == 'subtract':                               # O(1)
            i -= divisor                                            # O(1)
            if get_limit(dividend, i):                              # O(1)
                count += 1                                          # O(1)

    return count                                                    # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
