# pylint: disable-msg=line-too-long

def retrieve_array(digits):                                         # O(N)
    """
    Take a number and transform it into an array

    >>> retrieve_array(123456789)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> retrieve_array(-123456789)
    [-1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    string = "{0}".format(digits)                                   # O(1)
    length = len(string)                                            # O(1)

    array = []                                                      # O(1)
    minus = False                                                   # O(1)
    for i in range(0, length):                                      # O(N)
        digit = string[i]                                           # O(1)
        if digit == '-':                                            # O(1)
            minus = True                                            # O(1)
        elif minus:                                                 # O(1)
            array.append(int(digit) * -1)                           # O(1)
            minus = False                                           # O(1)
        else:                                                       # O(1)
            array.append(int(digit))                                # O(1)

    return array                                                    # O(1)

def concatenate_number(a, b):
    """
    Concatenates two number together

    >>> concatenate_number(4, 2)
    42
    >>> concatenate_number(-4, 2)
    -42
    >>> concatenate_number(-43, 2)
    -432
    >>> concatenate_number(0, 7)
    7
    """
    if a >= 0:
        return (a * 10) + b
    return (a * 10) - b

def calculate_computation(computation, num, operation):
    """
    If values exist in array concatenate with operation, else return number

    >>> calculate_computation([], 42, '+')
    [42]
    >>> calculate_computation([112], 42, '^')
    [112, '^', 42]
    """
    if computation:
        return computation + [operation, num]
    return [num]

def concatenate_or_append(value, output):
    """
    Either concatenate a list or append to it, in order to keep list flattened
    as list of lists

    >>> concatenate_or_append([42], [])
    [[42]]
    >>> concatenate_or_append([[42, 49]], [[23, 35]])
    [[23, 35], [42, 49]]
    """
    if isinstance(value[0], list):
        output += value
    else:
        output.append(value)

    return output

def find_paths(summed_value, previous_number, computation, index, array):
    """
    Find the different combinations that add upto summed_value from
    the combination of numbers provided in array.

    >>> find_paths(6, 1, [], 1, [1, 2, 3])
    [[1, '+', 2, '+', 3]]
    >>> find_paths(100, 1, [], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    [[1, '+', 2, '+', 3, '-', 4, '+', 5, '+', 6, '+', 78, '+', 9], [1, '+', 2, '+', 34, '-', 5, '+', 67, '-', 8, '+', 9], [1, '+', 23, '-', 4, '+', 56, '+', 7, '+', 8, '+', 9], [1, '+', 2, '-', 3, '+', 4, '+', 5, '+', 6, '+', 78, '+', 9], [12, '+', 3, '+', 4, '+', 5, '-', 6, '-', 7, '+', 89], [12, '+', 3, '-', 4, '+', 5, '+', 67, '+', 8, '+', 9], [12, '-', 3, '-', 4, '+', 5, '-', 6, '+', 7, '+', 89], [123, '-', 45, '-', 67, '+', 89]]
    """
    if index >= len(array):
        if summed_value == previous_number:
            if previous_number >= 0:
                return computation + ['+', previous_number]
            return computation + ['-', previous_number]
        return False

    current_digit = array[index]
    concat_number = concatenate_number(previous_number, current_digit)

    plus_paths = find_paths(
        summed_value - previous_number,
        current_digit,
        calculate_computation(computation, previous_number, '+'),
        index + 1,
        array
    )
    minus_paths = find_paths(
        summed_value + previous_number,
        current_digit,
        calculate_computation(computation, previous_number, '-'),
        index + 1,
        array
    )
    concat_paths = find_paths(
        summed_value,
        concat_number,
        computation,
        index + 1,
        array
    )

    paths = []
    if plus_paths:
        concatenate_or_append(plus_paths, paths)
    if minus_paths:
        concatenate_or_append(minus_paths, paths)
    if concat_paths:
        concatenate_or_append(concat_paths, paths)

    return paths

def solution(A, summed_value=100):
    """
    Compute to 100: Given the digits 123456789, build an expression
    by inserting "+" or "-" anywhere BETWEEN the digits so that it
    results to 100.

    Example: 1 + 23 - 4 + 5 + 6 + 78 - 9 = 100

    >>> solution(123, 6)
    [[1, '+', 2, '+', 3]]
    >>> solution(123, 7)
    []
    >>> solution(123456789)
    [[1, '+', 2, '+', 3, '-', 4, '+', 5, '+', 6, '+', 78, '+', 9], [1, '+', 2, '+', 34, '-', 5, '+', 67, '-', 8, '+', 9], [1, '+', 23, '-', 4, '+', 56, '+', 7, '+', 8, '+', 9], [1, '+', 2, '-', 3, '+', 4, '+', 5, '+', 6, '+', 78, '+', 9], [12, '+', 3, '+', 4, '+', 5, '-', 6, '-', 7, '+', 89], [12, '+', 3, '-', 4, '+', 5, '+', 67, '+', 8, '+', 9], [12, '-', 3, '-', 4, '+', 5, '-', 6, '+', 7, '+', 89], [123, '-', 45, '-', 67, '+', 89]]
    """
    array = retrieve_array(A)
    return find_paths(summed_value, array[0], [], 1, array)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
