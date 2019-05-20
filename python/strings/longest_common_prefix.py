# -*- coding: utf-8 -*-

def solution(strs):                                                # O(M * N)
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    >>> solution(['flower', 'flow', 'flight'])
    'fl'
    >>> solution(['dog', 'racecar', 'car'])
    ''
    >>> solution(['amazing', 'amazingly', 'amazing'])
    'amazing'
    >>> solution([])
    ''
    """
    output = ''                                                     # O(1)
    length = len(strs)                                              # O(1)

    if length == 0:                                                 # O(1)
        return output                                               # O(1)
    elif length == 1:
        return strs[0]                                              # O(1)

    options = strs[0]                                               # O(1)
    for i in range(1, length):                                      # O(M)
        word = strs[i]                                              # O(1)
        for j in range(0, len(word)):                               # O(N)
            if j >= len(options):                                   # O(1)
                break                                               # O(1)

            char = options[j]                                       # O(1)
            if word[j] != char:                                     # O(1)
                break                                               # O(1)
            output += char                                          # O(1)
        options = output                                            # O(1)
        output = ''                                                 # O(1)

    return options                                                  # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
