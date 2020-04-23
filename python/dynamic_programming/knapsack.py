def solution(capacity, items):                                      # O(M * N)
    """
    Given the capacity of the knapsack and items specified by weights and values,
    return the maximum summarized value of the items that can be fit in the
    knapsack.

    Example:
        capacity = 5, items(value, weight) = [(60, 5), (50, 3), (70, 4), (30, 2)]
        result = 80 (items valued 50 and 30 can both be fit in the knapsack)

    >>> solution(5, [(60, 5), (50, 3), (70, 4), (30, 2)])
    80
    """
    result = [(0, 0)] * (capacity + 1)                              # O(1)

    for value, weight in items:                                     # O(N)
        if weight > capacity:                                       # O(1)
            continue                                                # O(1)

        for i in range(1, len(result)):                             # O(M)
            calc_weight = max(weight + result[i - weight][1], \
                result[i][1])                                       # O(1)
            if calc_weight <= i:                                    # O(1)
                result[i] = (
                    max(value + result[i - weight][0], result[i][0]),
                    calc_weight
                )                                                   # O(1)

    return result[capacity][0]                                      # O(1)

if __name__ == '__main__':
    solution(5, [(60, 5), (50, 3), (70, 4), (30, 2)])
