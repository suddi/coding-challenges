def solution(coins, target):
    """
    You are given coins of different denominations and a total amount of
    money amount.

    Write a function to compute the fewest number of coins that you need
    to make up that amount.

    If that amount of money cannot be made up by any combination of the coins,
    return -1.

    # >>> solution([1, 2, 5], 11)
    # 3
    # >>> solution([2, 5], 6)
    # 3
    # >>> solution([2], 3)
    # -1
    """
    usable_coins = []
    max_usable_coin = 0

    for coin in coins:
        if coin > max_usable_coin and coin <= target:
            max_usable_coin = coin

        if coin <= target:
            usable_coins.append(coin)

    # if max_usable_coin == target:
    #     return 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
