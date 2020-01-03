class Node():
    def __init__(self, value):                                      # O(1)
        self.value = value                                          # O(1)
        self.next = None                                            # O(1)

class LinkedList():
    def __init__(self, value):                                      # O(1)
        if value:                                                   # O(1)
            self.head = Node(value)                                 # O(1)
            self.length = 1                                         # O(1)
        else:                                                       # O(1)
            self.head = None                                        # O(1)
            self.length = 0                                         # O(1)

    def print_list(self):                                           # O(N)
        """
        Prints linked list values sequentially

        >>> test = LinkedList(42)
        >>> test.print_list()
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

    def traverse(self, position):                                   # O(N)
        """
        Treverses linked list to given position

        >>> node = LinkedList(42).insert(31).insert(30, 0).traverse(20)
        >>> print(node.value) if node else 'N/A'
        'N/A'

        >>> node = LinkedList(42).insert(22, 1).insert(12, 1).insert(95) \
            .insert(1, 0).traverse(3)
        >>> print(node.value) if node else 'N/A'
        22
        """
        if position >= self.length:                                 # O(1)
            return None                                             # O(1)

        current_node = self.head                                    # O(1)
        i = 0                                                       # O(1)
        while current_node and i < position:                        # O(N)
            current_node = current_node.next                        # O(1)
            i += 1                                                  # O(1)

        if current_node:                                            # O(1)
            return current_node                                     # O(1)
        return None                                                 # O(1)

    def insert(self, value, position=None):                         # O(1)
        """
        Inserts values into the LinkedList

        >>> LinkedList(42).insert(31).insert(30, 0).print_list()
        30 -> 42 -> 31

        >>> LinkedList(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .print_list()
        1 -> 42 -> 12 -> 22 -> 95
        """
        if position is None:                                        # O(1)
            position = self.length                                  # O(1)
        elif position > self.length:                                # O(1)
            raise Exception('Cannot insert into non-existent ' + \
                'position in linked list')                          # O(1)

        node = self.traverse(position - 1)                          # O(1)
        if not node:                                                # O(1)
            raise Exception('Could not find node at position %d' \
                % (position or self.length))                        # O(1)

        if position == 0:                                           # O(1)
            self.head = Node(value)                                 # O(1)
            self.head.next = node                                   # O(1)
        else:                                                       # O(1)
            next_node = node.next                                   # O(1)
            node.next = Node(value)                                 # O(1)
            node.next.next = next_node                              # O(1)
        self.length += 1                                            # O(1)

        return self                                                 # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
