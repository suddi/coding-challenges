def solution(prices):                                               # O(N)
    """
    Say you have an array for which the ith element is the price
    of a given stock on day i.

    If you were only permitted to complete at most one transaction
    (i.e., buy one and sell one share of the stock), design an
    algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.

    >>> solution([7, 1, 5, 3, 6, 4])
    5
    >>> solution([7, 2, 10, 1, 3])
    8
    >>> solution([7, 2, 10, 1, 3, 1, 10])
    9
    >>> solution([7, 6, 4, 3, 1])
    0
    """
    min_price = float('inf')                                        # O(1)
    max_profit = 0                                                  # O(1)

    for price in prices:                                            # O(N)
        if price < min_price:                                       # O(1)
            min_price = price                                       # O(1)
        elif price - min_price > max_profit:                        # O(1)
            max_profit = price - min_price                          # O(1)

    return max_profit                                               # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
