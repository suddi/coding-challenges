from random import (seed, randint)

from python.numbers.missing_number import solution

def create_input_array():
    length = randint(1, 1000)
    remove_index = randint(1, length)
    input_array = []
    for i in range(0, length + 1):
        input_array.append(i)

    expected_result = input_array[remove_index]
    del input_array[remove_index]
    return (input_array, expected_result)

def test_solution():
    seed(1)
    for _ in range(0, 100):
        input_array, expected_result = create_input_array()

        result = solution(input_array)

        assert result == expected_result
