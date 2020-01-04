connections = {
    1: (8, 6),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: (),
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6)
}

def dfs(position, hops, combinations, combination=''):
    if not hops:
        combination += str(position)
        combinations.append(combination)
        return combinations

    connection = connections[position]
    for next_step in connection:
        dfs(next_step, hops - 1, combinations, combination + str(position))

def solution(starting_point, hops):                                 # O(N)
    """
    Imagine you place a knight chess piece on a phone dial pad.
    This chess piece moves in an uppercase “L” shape: two steps horizontally
    followed by one vertically, or one step horizontally then two vertically.

    Suppose you dial keys on the keypad using only hops a knight can make.
    Every time the knight lands on a key, we dial that key and make another hop.
    The starting position counts as being dialed.

    How many distinct numbers can you dial in N hops from a particular starting
    position?

    >>> solution(1, 3)
    10
    >>> solution(6, 2)
    6
    >>> solution(10, 1)
    >>> solution(4, -1)
    >>> solution(4, 0)
    1
    >>> solution(5, 12)
    1
    >>> solution(4, 10)
    4608
    """
    if starting_point not in connections.keys() or hops < 0:
        return None
    if starting_point == 5 or hops == 0:
        return 1

    combinations = []
    dfs(starting_point, hops, combinations)
    combinations = set(combinations)
    return len(combinations)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
