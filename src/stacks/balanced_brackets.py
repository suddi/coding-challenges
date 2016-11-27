# -*- coding: utf-8 -*-

def solution(expression):
    """
    Write a function to detect if brackets/parantheses are balanced, given an input string.
    eg. "[{}]" is balanced, "[{)}]" is not

    >>> solution('{[()]}')
    True
    >>> solution('[{}]')
    True
    >>> solution('[{)}]')
    False
    """
    brackets = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    openers = brackets.keys()                                       # O(N)
    closers = brackets.values()                                     # O(N)
    stack = []                                                      # O(1)
    for char in expression:                                         # O(N)
        if char in openers:                                         # O(1)
            stack.append(char)                                      # O(1)
        elif char in closers:                                       # O(1)
            if not len(stack):                                      # O(1)
                return False                                        # O(1)
            last_char = stack.pop()                                 # O(1)
            if last_char not in brackets or \
                brackets[last_char] != char:                        # O(1)
                return False                                        # O(1)
        else:                                                       # O(1)
            return False                                            # O(1)

    if len(stack):                                                  # O(1)
        return False                                                # O(1)
    return True                                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
