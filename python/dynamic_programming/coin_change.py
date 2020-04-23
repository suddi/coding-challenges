def solution(coins, target):                                        # O(M * N)
    """
    You are given coins of different denominations and a total amount of money.

    Write a function to compute the fewest number of coins that you need
    to make up that amount.

    If that amount of money cannot be made up by any combination of the coins,
    return -1.

    >>> solution([1, 2, 5], 11)
    3
    >>> solution([2, 5], 6)
    3
    >>> solution([2], 3)
    -1
    >>> solution([10], 5)
    -1
    """
    min_coins = [0] + [-1] * target                                 # O(N)

    for coin in coins:                                              # O(M)
        if coin > target:                                           # O(1)
            continue                                                # O(1)

        for i in range(1, target + 1):                              # O(N)
            if min_coins[i - coin] == -1:                           # O(1)
                continue                                            # O(1)

            if min_coins[i] != -1:                                  # O(1)
                min_coins[i] = min(1 + min_coins[i - coin], \
                    min_coins[i])                                   # O(1)
            else:                                                   # O(1)
                min_coins[i] = 1 + min_coins[i - coin]              # O(1)

    return min_coins[target]                                        # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
