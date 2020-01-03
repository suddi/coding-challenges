def solution1(magazine, ransom):                                     # O(N^2)
    """
    Similar to src.strings.making_anagrams, detect if 2 strings can be equated by
    only removing some words.

    >>> solution1('give me one grand today night', 'give one grand one today')
    False
    >>> solution1('give me one grand today night', 'give one grand today')
    True
    >>> solution1('give me one grand one today night', 'give one grand today')
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

def solution2(magazine, ransom):                                    # O(N)
    """
    Similar to src.strings.making_anagrams, detect if 2 strings can be equated by
    only removing some words.

    >>> solution2('give me one grand today night', 'give one grand one today')
    False
    >>> solution2('give me one grand today night', 'give one grand today')
    True
    >>> solution2('give me one grand one today night', 'give one grand today')
    True
    """
    list_a = magazine.split(' ')                                    # O(N)
    list_b = ransom.split(' ')                                      # O(N)

    i = 0                                                           # O(1)
    j = 0                                                           # O(1)
    length_magazine = len(list_a)                                   # O(1)
    length_ransom = len(list_b)                                     # O(1)
    while j < length_ransom:                                        # O(N)
        if list_a[i] == list_b[j]:                                  # O(1)
            i += 1                                                  # O(1)
            j += 1                                                  # O(1)
        else:                                                       # O(1)
            i += 1                                                  # O(1)

        if i == length_magazine:                                    # O(1)
            return False                                            # O(1)

    return True                                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
