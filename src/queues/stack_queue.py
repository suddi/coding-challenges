# -*- coding: utf-8 -*-

def prepare_dequeue(A):                                             # O(N)
    queue = []                                                      # O(1)
    for i in xrange(0, len(A)):                                     # O(N)
        queue.append(A.pop())                                       # O(1)
    return queue                                                    # O(1)

def solution(operations):                                           # O(N^2)
    """
    Create a FIFO queue using stack operations only.

    >>> solution([('enqueue', 1), ('enqueue', 3), ('enqueue', 5), ('enqueue', 4), ('dequeue',), ('enqueue', 1), ('dequeue',)])
    1
    3
    """
    enqueue = []                                                    # O(1)
    dequeue = []                                                    # O(1)

    for operation in operations:                                    # O(N)
        if operation[0] == 'enqueue' and operation[1]:              # O(1)
            enqueue.append(operation[1])                            # O(1)
        elif operation[0] == 'dequeue':                             # O(1)
            if not dequeue:                                         # O(1)
                dequeue = prepare_dequeue(enqueue)                  # O(N)
            print dequeue.pop()                                     # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
