def solution(coins, target):                                        # O(M * N)
    """
    Given a value n, if we want to make change for N cents, and we have an
    infinite supply of each of coins = {S1, S2, .. , Sm} valued coins,
    how many ways can we make the change?

    The order of coins doesn't matter.
    For example, for n = 4 and coins = [1, 2, 3], there are four solutions:
        [1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3].
    So output should be 4.

    For n = 10 and coins = [2, 5, 3, 6], there are five solutions:
        [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5].
    So the output should be 5.

    >>> solution([1, 2, 3], 4)
    4
    >>> solution([2, 5, 3, 6], 10)
    5
    """
    coin_possibilities = [1] + [0] * (target + 1)                   # O(N)

    for coin in coins:                                              # O(M)
        for i in range(coin, target + 1):                           # O(N)
            coin_possibilities[i] += coin_possibilities[i - coin]   # O(1)

    return coin_possibilities[target]                               # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
