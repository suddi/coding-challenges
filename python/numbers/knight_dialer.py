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

    # >>> solution(6, 2)
    # 6
    # >>> solution(1, 3)
    # 9
    """
    print(starting_point, hops)

    # connections = {
    #     1: (8, 6),
    #     2: (7, 9),
    #     3: (4, 8),
    #     4: (3, 9, 0),
    #     5: (),
    #     6: (1, 7, 0),
    #     7: (2, 6),
    #     8: (1, 3),
    #     9: (2, 4),
    #     0: (4, 6)
    # }

    # if starting_point == 5:
    #     return 1

    # dialed = {}
    # queue = [starting_point]
    # for hop in range(0, hops):
    #     length = len(queue)
    #     for i in range(0, length):
    #         current_position = queue.pop(0)
    #         if dialed.get(current_position):
    #             dialed[current_position] += 1
    #         else:
    #             dialed[current_position] = 1
    #         queue += connections[current_position]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
