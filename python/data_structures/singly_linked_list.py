class Node():
    def __init__(self, value):                                      # O(1)
        self.value = value                                          # O(1)
        self.next = None                                            # O(1)

class LinkedList():
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
        Returns the length of the LinkedList

        >>> LinkedList(42).insert(22, 1).insert(12, 1).insert(95) \
            .insert(1, 0).get_length()
        5
        """
        return self.length                                          # O(1)

    def pretty_print(self):                                         # O(N)
        """
        Pretty prints LinkedList values sequentially

        >>> LinkedList(42).pretty_print()
        42
        """
        string = ''                                                 # O(1)
        current_node = self.head                                    # O(1)
        while current_node:                                         # O(N)
            string += str(current_node.value) + ' '                 # O(1)
            if current_node.next:                                   # O(1)
                string += '-> '                                     # O(1)
            current_node = current_node.next                        # O(1)

        if string:                                                  # O(1)
            print(string.strip())                                   # O(1)

    def access(self, position):                                     # O(N)
        """
        Accesses LinkedList at a given position

        >>> LinkedList(42).insert(31).insert(30, 0).access(20)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position 20 in LinkedList

        >>> LinkedList(42).insert(31).insert(30, 0).access(-1)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position -1 in LinkedList

        >>> LinkedList(42).insert(22, 1).insert(12, 1).insert(95) \
            .insert(1, 0).access(3).value
        22
        """
        if position >= self.length or position < 0:                 # O(1)
            raise Exception('Cannot find non-existent position ' \
                + '%d in LinkedList' % position)                    # O(1)

        current_node = self.head                                    # O(1)
        i = 0                                                       # O(1)
        while current_node and i < position:                        # O(N)
            current_node = current_node.next                        # O(1)
            i += 1                                                  # O(1)

        return current_node                                         # O(1)

    def search(self, value):                                        # O(N)
        """
        Searches for value in LinkedList and returns position

        >>> LinkedList(42).insert(31).insert(30, 0).search(31)
        2

        >>> LinkedList(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .search(22)
        3

        >>> LinkedList(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .search(52)
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

    def insert(self, value, position=None):                         # O(N)
        """
        Inserts values into the LinkedList

        Insert covers 3 cases:
        1) Insert at the end of the LinkedList                      # O(1)
        2) Insert at the beginning of the LinkedList                # O(1)
        3) Insert in the middle of the LinkedList                   # O(N)

        >>> LinkedList(42).insert(31).insert(30, 0).pretty_print()
        30 -> 42 -> 31

        >>> LinkedList(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .pretty_print()
        1 -> 42 -> 12 -> 22 -> 95
        """
        if position is None or position == self.length:             # O(1)
            self.tail.next = Node(value)                            # O(1)
            self.tail = self.tail.next                              # O(1)
        elif position == 0:                                         # O(1)
            node = self.head                                        # O(1)
            self.head = Node(value)                                 # O(1)
            self.head.next = node                                   # O(1)
        else:                                                       # O(1)
            node = self.access(position - 1)                        # O(N)
            next_node = node.next                                   # O(1)
            node.next = Node(value)                                 # O(1)
            node.next.next = next_node                              # O(1)
        self.length += 1                                            # O(1)

        return self                                                 # O(1)

    def delete(self, position=None):                                # O(N)
        """
        Deletes value in LinkedList by position

        Delete covers 2 cases:
        1) Delete at the beginning of the LinkedList                # O(1)
        2) Delete elsewhere in the LinkedList                       # O(N)

        >>> LinkedList(42).insert(31).insert(30, 0).delete(1).delete().pretty_print()
        30

        >>> LinkedList(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .delete().delete(0).delete(1).pretty_print()
        42 -> 22

        >>> LinkedList(42).insert(22).insert(12).insert(95).insert(1) \
            .delete().delete().delete().delete().delete().delete().delete() \
            .delete().pretty_print()
        """
        if position is None:                                        # O(1)
            if not self.length:                                     # O(1)
                return self                                         # O(1)
            position = self.length - 1                              # O(1)

        if position == 0:                                           # O(1)
            self.head = self.head.next                              # O(1)
        else:                                                       # O(1)
            node = self.access(position - 1)                        # O(N)
            next_node = node.next                                   # O(1)
            if next_node:                                           # O(1)
                node.next = next_node.next                          # O(1)
            else:                                                   # O(1)
                node.next = None                                    # O(1)
        self.length -= 1                                            # O(1)

        return self                                                 # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
