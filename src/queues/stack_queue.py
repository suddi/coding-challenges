# -*- coding: utf-8 -*-

def prepare_dequeue(A):
    queue = []
    for i in xrange(0, len(A)):
        queue.append(A.pop())
    return queue

def solution(operations):
    """
    Create a FIFO queue using stack operations only.

    >>> solution([('enqueue', 1), ('enqueue', 3), ('enqueue', 5), ('enqueue', 4), ('dequeue',), ('enqueue', 1), ('dequeue',)])
    1
    3
    """
    enqueue = []
    dequeue = []

    for operation in operations:
        if operation[0] == 'enqueue' and operation[1]:
            enqueue.append(operation[1])
        elif operation[0] == 'dequeue':
            if not dequeue:
                dequeue = prepare_dequeue(enqueue)
            print dequeue.pop()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
