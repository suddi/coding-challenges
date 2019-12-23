# -*- coding: utf-8 -*-

from collections import deque

def compute_squares(k):                                             # O(N)
    """
    Compute squares upto a value k

    >>> compute_squares(26)
    [1, 4, 9, 16, 25]
    >>> compute_squares(128)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    >>> compute_squares(0)
    []
    >>> compute_squares(1)
    [1]
    """
    array = []                                                      # O(1)
    for i in range(1, k + 1):                                       # O(N)
        square_value = i * i                                        # O(1)
        if square_value < k + 1:                                    # O(1)
            array.append(square_value)                              # O(1)
        else:                                                       # O(1)
            return array                                            # O(1)

    return array                                                    # O(1)

def get_values_greater_than(values, A):                             # O(N)
    """
    From a ascendingly sorted array of values, get values > A

    >>> get_values_greater_than([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121], 64)
    [121, 100, 81, 64]
    >>> get_values_greater_than([1], 1)
    [1]
    """
    num_values = len(values)                                        # O(1)
    array = []                                                      # O(1)
    for i in range(num_values - 1, -1, -1):                         # O(N)
        value = values[i]                                           # O(1)
        if value >= A:                                              # O(1)
            array.append(value)                                     # O(1)
        else:                                                       # O(1)
            return array                                            # O(1)

    return array                                                    # O(1)

def ready_queue(A, queue, output):                                  # O(N)
    possible_values = get_values_greater_than(
        compute_squares(A),
        (A / 2) - 1
    )                                                               # O(N)
    for value in possible_values:                                   # O(N)
        queue.append({
            'output': output + [value],
            'remainder': A - value
        })                                                          # O(1)
    return queue                                                    # O(1)

def process_queue(queue):                                           # O(N^2)
    while queue:                                                    # O(N)
        element = queue.popleft()                                   # O(1)
        remainder, output = element['remainder'], element['output'] # O(1)
        if not remainder:                                           # O(1)
            return output                                           # O(1)
        elif remainder > 0:                                         # O(1)
            ready_queue(remainder, queue, output)                   # O(1)

    return []                                                       # O(1)

def solution(A):                                                    # O(N^2)
    """
    For a given value A, compute the number with the fewest number of
    squared values and return them within an array.

    eg. 26 can be computed with squared values [25, 1] or [16, 9, 1], but the
        answer is only [25, 1] as we are looking for the fewest number of
        squared values

    >>> solution(26)
    [25, 1]
    >>> solution(128)
    [64, 64]
    >>> solution(33)
    [25, 4, 4]
    >>> solution(256)
    [256]
    """
    queue = deque()                                                 # O(1)
    ready_queue(A, queue, [])                                       # O(N)
    return process_queue(queue)                                     # O(N^2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
