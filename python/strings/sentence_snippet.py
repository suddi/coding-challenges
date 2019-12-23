# -*- coding: utf-8 -*-

def solution(A, k):                                                 # O(N)
    """
    Write  a  program  to create k characters long snippets from sentences A.

    >>> solution('' + \
        'Featuring stylish rooms and moorings for recreation boats, ' + \
        'Room Mate Aitana is a designer hotel built in 2013 on an island ' + \
        'in the IJ River in Amsterdam.', 30)
    'Featuring stylish rooms and...'
    """
    more_string = '...'
    array = A.split(' ')
    output = ''
    for value in array:
        if len(value) + len(output) > k:
            return output + more_string
        output = (output + ' ' + value).strip()
    return output + more_string

if __name__ == '__main__':
    import doctest
    doctest.testmod()
