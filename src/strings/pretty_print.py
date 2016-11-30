# -*- coding: utf-8 -*-

def solution(A):
    """
    Given a list of tuples, pretty print it to show the associated key and value as columns in a table.
    eg. [('hello', 3), ('world', 2), ('this', 5), ('is', 2), ('fun', 9), ('hello', 1)]
    should become:
    hello world this is fun
    4
          2
                5
                     2
                        9

    >>> solution([('hello', 3), ('world', 2), ('this', 5), ('is', 200), ('fun', 9), ('hello', 1)])
    hello world this is  fun
    4
          2
                5
                     200
                         9
    """
    keys = []                                                       # O(1)
    mapped = {}                                                     # O(1)
    for key, value in A:                                            # O(N)
        if not key in mapped:                                       # O(1)
            mapped[key] = value                                     # O(1)
            keys.append(key)                                        # O(1)
        else:                                                       # O(1)
            mapped[key] += value                                    # O(1)

    lengths = {}                                                    # O(1)
    for key, value in mapped.iteritems():                           # O(N)
        lengths[key] = max(len(key), len(str(value))) + 1           # O(1)

    return_string = ''                                              # O(1)
    for key in keys:                                                # O(N)
        return_string += key + ' ' * (lengths[key] - len(key))      # O(1)
    return_string = return_string.strip()                           # O(1)
    return_string += '\n'                                           # O(1)

    previous_spacing = ''                                           # O(1)
    for key in keys:                                                # O(1)
        value = str(mapped[key])                                    # O(1)
        return_string += previous_spacing + value + '\n'            # O(1)
        previous_spacing += ' ' * lengths[key]                      # O(1)

    print return_string.strip()                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
