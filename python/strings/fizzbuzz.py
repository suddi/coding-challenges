# pylint: disable-msg=line-too-long

def solution(N):
    """
    Write a function that returns an array containing the numbers from 1 to N,
    where N is the parametered value. N will never be less than 1.

    Replace certain values however if any of the following conditions are met:
        - If the value is a multiple of 3: use the value 'Fizz' instead
        - If the value is a multiple of 5: use the value 'Buzz' instead
        - If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead

    >>> solution(42)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz']
    """
    array = []
    for i in range(1, N + 1):
        value = i
        is_multiple_of_3 = i % 3 == 0
        is_multiple_of_5 = i % 5 == 0

        if is_multiple_of_3 and is_multiple_of_5:
            value = 'FizzBuzz'
        elif is_multiple_of_3:
            value = 'Fizz'
        elif is_multiple_of_5:
            value = 'Buzz'

        array.append(value)

    return array
