def solution(S):                                                    # O(N)
    """
    Given a string S of upper case characters, from which you have to retrieve
    the 7 letters:
    "B", "A", "L", "L" "O", "O", "N"

    return how many times you can retrieve these characters from string S.

    >>> solution('AGEASEBESLOLOBN')
    1
    >>> solution('AGEASEBESLOLOBNDSOENOLBOLVA')
    2
    >>> solution('XEBEALPLOWQOA')
    0
    """
    characters = {
        'B': 0,
        'A': 0,
        'L': 0,
        'O': 0,
        'N': 0
    }                                                               # O(1)
    occurences = {
        'B': 1,
        'A': 1,
        'L': 2,
        'O': 2,
        'N': 1
    }                                                               # O(1)

    keys = characters.keys()                                        # O(1)
    for letter in S:                                                # O(N)
        if letter in keys:                                          # O(1)
            characters[letter] += 1                                 # O(1)

    num_moves = float('inf')                                        # O(1)
    for key in keys:                                                # O(1)
        move = characters[key] // occurences[key]                   # O(1)
        num_moves = min(num_moves, move)                            # O(1)

    return num_moves                                                # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
