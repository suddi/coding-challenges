def solution(A, k):                                                 # O(N)
    """
    Write  a  program  to create k characters long snippets from sentences A.

    >>> solution('' + \
        'Featuring stylish rooms and moorings for recreation boats, ' + \
        'Room Mate Aitana is a designer hotel built in 2013 on an island ' + \
        'in the IJ River in Amsterdam.', 30)
    'Featuring stylish rooms and...'
    """
    more_string = '...'                                             # O(1)
    array = A.split(' ')                                            # O(N)
    output = ''                                                     # O(1)

    for value in array:                                             # O(N)
        if len(value) + len(output) > k:                            # O(1)
            return output + more_string                             # O(1)
        output = (output + ' ' + value).strip()                     # O(1)
    return output + more_string                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
