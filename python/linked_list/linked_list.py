# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, value):
        if value:
            self.head = Node(value)
            self.length = 1
        else:
            self.head = None
            self.length = 0

    def print_list(self):
        """
        Prints linked list values sequentially

        >>> test = LinkedList(42)
        >>> test.print_list()
        42
        """
        current_node = self.head
        while current_node:
            print current_node.value,
            if current_node.next:
                print '->',
            current_node = current_node.next

    def traverse(self, position):
        """
        Treverses linked list to given position

        >>> node = LinkedList(42).insert(31).insert(30, 0).traverse(20)
        >>> print(node.value) if node else 'N/A'
        N/A

        >>> node = LinkedList(42).insert(22, 1).insert(12, 1).insert(95) \
            .insert(1, 0).traverse(3)
        >>> print(node.value) if node else 'N/A'
        22
        """
        if position >= self.length:
            return None

        current_node = self.head
        i = 0
        while current_node and i < position:
            current_node = current_node.next
            i += 1

        if current_node:
            return current_node
        return None

    def insert(self, value, position = None):
        """
        Inserts values into the LinkedList

        >>> LinkedList(42).insert(31).insert(30, 0).print_list()
        30 -> 42 -> 31

        >>> LinkedList(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .print_list()
        1 -> 42 -> 12 -> 22 -> 95
        """
        if position is None:
            position = self.length
        elif position > self.length:
            raise Exception('Cannot insert into non-existent position in linked list')

        node = self.traverse(position - 1)
        if not node:
            raise Exception('Could not find node at position %d' % (position or self.length))

        if position == 0:
            self.head = Node(value)
            self.head.next = node
        else:
            next_node = node.next
            node.next = Node(value)
            node.next.next = next_node
        self.length += 1

        return self

if __name__ == '__main__':
    import doctest
    doctest.testmod()
