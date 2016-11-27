# -*- coding: utf-8 -*-

def solution(a, b):
    """
    Given 2 strings, write a function to compute how many deletions are necessary to
    transform one string to an anagram of the other.
    An anagram is defined as a string, that contains the same letters with the same
    number of occurences as another word.

    Similar to src.hash_tables.ransom_note.

    >>> solution('cdegfbc', 'abbcfhi')
    8
    >>> solution('abc', 'dba')
    2
    """
    list_a = list(a)                                                # O(N)
    list_b = list(b)                                                # O(N)
    total_length = len(list_a) + len(list_b)                        # O(1)

    anagram = []                                                    # O(1)
    for char in list_a:                                             # O(N)
        if char in list_b:                                          # O(1)
            anagram.append(char)                                    # O(1)
            list_b.remove(char)                                     # O(N)

    deletions_needed = total_length - (2 * len(anagram))            # O(1)
    return deletions_needed                                         # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
