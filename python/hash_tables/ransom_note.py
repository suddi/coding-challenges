# -*- coding: utf-8 -*-

def solution(magazine, ransom):                                     # O(N^2)
    """
    Similar to src.strings.making_anagrams, detect if 2 strings can be equated by
    only removing some words.

    >>> solution('give me one grand today night', 'give one grand one today')
    False
    >>> solution('give me one grand today night', 'give one grand today')
    True
    """
    list_a = magazine.split(' ')                                    # O(N)
    list_b = ransom.split(' ')                                      # O(N)

    for word in list_b:                                             # O(N)
        if word in list_a:                                          # O(1)
            list_a.remove(word)                                     # O(N)
        else:                                                       # O(1)
            return False                                            # O(1)

    return True                                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
