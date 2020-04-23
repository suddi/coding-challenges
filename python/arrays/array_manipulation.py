def solution(array_size, queries):
    """
    Starting with a 1-indexed array of zeros and a list of operations,
    for each operation add a value to each of the array element between
    two given indices, inclusive. Once all operations have been performed,
    return the maximum value in your array.

    For example, the length of your array of zeros.
    Your list of queries is as follows:
        a b k
        1 5 3
        4 8 7
        6 9 1

    Add the values of  between the indices  and  inclusive:
    index->	 1   2   3   4   5   6   7   8   9   10
            [0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
            [3,  3,  3,  3,  3,  0,  0,  0,  0,  0]
            [3,  3,  3, 10, 10,  7,  7,  7,  0,  0]
            [3,  3,  3, 10, 10,  8,  8,  8,  1,  0]
    The largest value is 10 after all operations are performed.

    >>> solution(10, [(1, 5, 3), (4, 8, 7), (6, 9, 1)])
    10
    >>> solution(5, [(1, 2, 100), (2, 5, 100), (3, 4, 100)])
    200
    """
    array = []
    for _ in range(0, array_size):
        array.append(0)

    max_value = float('-inf')
    for (a, b, k) in queries:
        i = a - 1
        j = b - 1
        while i < j:
            array[i] += k
            max_value = max(array[i], max_value)
            i += 1

    return max_value

if __name__ == '__main__':
    import doctest
    doctest.testmod
