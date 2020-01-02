# -*- coding: utf-8 -*-

class Node():
    def __init__(self, value):                                      # O(1)
        self.value = value                                          # O(1)
        self.next = None                                            # O(1)

class Queue():
    def __init__(self, value=None):                                 # O(1)
        if value is not None:                                       # O(1)
            self.head = Node(value)                                 # O(1)
            self.length = 1                                         # O(1)
        else:                                                       # O(1)
            self.head = None                                        # O(1)
            self.length = 0                                         # O(1)
        self.tail = self.head                                       # O(1)

    def get_length(self):                                           # O(1)
        """
        Returns the length of the Queue

        >>> Queue(42).insert(22).insert(12).insert(95).insert(1).get_length()
        5
        """
        return self.length                                          # O(1)

    def pretty_print(self):                                         # O(N)
        """
        Pretty prints Queue values sequentially

        >>> Queue(42).pretty_print()
        42
        """
        string = ''                                                 # O(1)
        current_node = self.head                                    # O(1)
        while current_node:                                         # O(N)
            string += str(current_node.value) + ' '                 # O(1)
            if current_node.next:                                   # O(1)
                string += '<- '                                     # O(1)
            current_node = current_node.next                        # O(1)

        if string:                                                  # O(1)
            print(string.strip())                                   # O(1)

    def access(self, position):                                     # O(N)
        """
        Accesses Queue at a given position

        >>> Queue(42).insert(31).insert(30).access(20)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position 20 in Queue

        >>> Queue(42).insert(31).insert(30).access(-1)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position -1 in Queue

        >>> Queue(42).insert(22).insert(12).insert(95).insert(1).access(3).value
        95
        """
        if position >= self.length or position < 0:                 # O(1)
            raise Exception('Cannot find non-existent position ' \
                + '%d in Queue' % position)                         # O(1)

        current_node = self.head                                    # O(1)
        i = 0                                                       # O(1)
        while current_node and i < position:                        # O(N)
            current_node = current_node.next                        # O(1)
            i += 1                                                  # O(1)

        return current_node                                         # O(1)

    def search(self, value):                                        # O(N)
        """
        Searches for value in Queue and returns position

        >>> Queue(42).insert(31).insert(30).search(31)
        1

        >>> Queue(42).insert(22).insert(12).insert(95).insert(1).search(22)
        1

        >>> Queue(42).insert(22).insert(12).insert(95).insert(1).search(52)
        -1
        """
        current_node = self.head                                    # O(1)
        i = 0                                                       # O(1)
        while current_node and i < self.length:                     # O(N)
            if current_node.value == value:                         # O(1)
                return i                                            # O(1)
            current_node = current_node.next                        # O(1)
            i += 1                                                  # O(1)

        return -1                                                   # O(1)

    def insert(self, value):                                        # O(1)
        """
        Inserts values into the Queue, only possible at the end

        Insert covers 1 case:
        1) Insert at the end of the Queue                           # O(1)

        >>> Queue(42).insert(31).insert(30).pretty_print()
        42 <- 31 <- 30

        >>> Queue(42).insert(22).insert(12).insert(95).insert(1).pretty_print()
        42 <- 22 <- 12 <- 95 <- 1
        """
        self.tail.next = Node(value)                                # O(1)
        self.tail = self.tail.next                                  # O(1)
        self.length += 1                                            # O(1)

        return self                                                 # O(1)

    def delete(self):                                               # O(1)
        """
        Deletes value in Queue by position, only possible at the beginning

        Delete covers 1 case:
        1) Delete at the beginning of the Queue                     # O(1)

        >>> Queue(42).insert(31).insert(30).delete().delete().pretty_print()
        30

        >>> Queue(42).insert(22).insert(12).insert(95).insert(1) \
            .delete().delete().delete().pretty_print()
        95 <- 1

        >>> Queue(42).insert(22).insert(12).insert(95).insert(1) \
            .delete().delete().delete().delete().delete().delete().delete() \
            .delete().pretty_print()
        """
        if self.head:                                               # O(1)
            self.head = self.head.next                              # O(1)
            self.length -= 1                                        # O(1)

        return self                                                 # O(1)

    def push(self, value):                                          # O(1)
        """
        Push a value at the end of the queue to demonstrate FIFO capability of Queue

        >>> Queue(42).push(31).push(30).pretty_print()
        42 <- 31 <- 30

        >>> Queue(42).push(22).push(12).push(95).push(1).pretty_print()
        42 <- 22 <- 12 <- 95 <- 1
        """
        self.tail.next = Node(value)                                # O(1)
        self.tail = self.tail.next                                  # O(1)
        self.length += 1                                            # O(1)

        return self                                                 # O(1)

    def pop(self):                                                  # O(1)
        """
        Pop a value out at the of the queue to demonstrate FIFO capability of Queue

        >>> Queue(42).push(31).push(30).pop()
        42

        >>> Queue(42).push(22).push(12).push(95).push(1).pop()
        42

        >>> Queue().pop()
        """
        if self.head:                                               # O(1)
            value = self.head.value                                 # O(1)
            self.head = self.head.next                              # O(1)
            self.length -= 1                                        # O(1)
            return value                                            # O(1)

        return None                                                 # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
