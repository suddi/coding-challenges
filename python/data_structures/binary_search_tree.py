class Node():
    def __init__(self, value):                                      # O(1)
        self.value = value                                          # O(1)
        self.left = None                                            # O(1)
        self.right = None                                           # O(1)

class Tree():
    def __init__(self, value=None):                                 # O(1)
        if value is not None:                                       # O(1)
            self.root = Node(value)                                 # O(1)
            self.height = 1                                         # O(1)
            self.size = 1                                           # O(1)
        else:                                                       # O(1)
            self.root = None                                        # O(1)
            self.height = 0                                         # O(1)
            self.size = 0                                           # O(1)

    def get_height(self):                                           # O(1)
        """
        Returns the height of the Tree

        >>> Tree(42).insert(22).insert(12).insert(95).insert(1).get_height()
        4
        """
        return self.height                                          # O(1)

    def get_size(self):
        """
        Returns the size of the Tree

        >>> Tree(42).insert(22).insert(12).insert(95).insert(1).get_size()
        5
        """
        return self.size                                            # O(1)

    def convert_to_array(self, node, form='preorder'):              # O(N)
        """
        Converts Tree structure to array

        >>> tree = Tree(42).insert(50).insert(21).insert(12).insert(14).insert(99) \
            .insert(4).insert(65)
        >>> tree.convert_to_array(tree.root)
        [42, 21, 12, 4, 14, 50, 99, 65]

        >>> tree = Tree(42).insert(50).insert(21).insert(12).insert(14).insert(99) \
            .insert(4).insert(65)
        >>> tree.convert_to_array(tree.root, 'preorder')
        [42, 21, 12, 4, 14, 50, 99, 65]

        >>> tree = Tree(42).insert(50).insert(21).insert(12).insert(14).insert(99) \
            .insert(4).insert(65)
        >>> tree.convert_to_array(tree.root, 'inorder')
        [4, 12, 14, 21, 42, 50, 65, 99]

        >>> tree = Tree(42).insert(50).insert(21).insert(12).insert(14).insert(99) \
            .insert(4).insert(65)
        >>> tree.convert_to_array(tree.root, 'postorder')
        [4, 14, 12, 21, 65, 99, 50, 42]

        >>> tree = Tree(42).insert(50).insert(21).insert(12).insert(14).insert(99) \
            .insert(4).insert(65)
        >>> tree.convert_to_array(tree.root, 'levelorder')
        [42, 21, 50, 12, 99, 4, 14, 65]

        >>> tree = Tree(42).insert(50).insert(21).insert(12).insert(14).insert(99) \
            .insert(4).insert(65)
        >>> tree.convert_to_array(tree.root, 'noorder')
        Traceback (most recent call last):
        Exception: Unknown form requested `noorder` for Tree
        """
        def set_by_position(node, position, array):                 # O(1)
            if node:                                                # O(1)
                array[position] = node.value                        # O(1)

        def convert_by_level(node, position, array):                # O(N)
            if not node:                                            # O(1)
                return array                                        # O(1)

            left_position = (2 * position) + 1                      # O(1)
            set_by_position(node.left, left_position, array)        # O(1)

            right_position = (2 * position) + 2                     # O(1)
            set_by_position(node.right, right_position, array)      # O(1)

            convert_by_level(node.left, left_position, array)       # O(N)
            convert_by_level(node.right, right_position, array)     # O(N)

            return array                                            # O(1)

        if not node:                                                # O(1)
            return []                                               # O(1)

        if form == 'preorder':                                      # O(1)
            return [node.value] + self.convert_to_array(node.left, form) + \
                self.convert_to_array(node.right, form)             # O(N)
        if form == 'inorder':                                       # O(1)
            return self.convert_to_array(node.left, form) + [node.value] + \
                self.convert_to_array(node.right, form)             # O(N)
        if form == 'postorder':                                     # O(1)
            return self.convert_to_array(node.left, form) + \
                self.convert_to_array(node.right, form) + \
                [node.value]                                        # O(N)
        if form == 'levelorder':                                    # O(1)
            array = [None] * (pow(2, self.height) - 1)              # O(N)
            set_by_position(self.root, 0, array)                    # O(1)
            convert_by_level(self.root, 0, array)                   # O(N)
            return [x for x in array if x]                          # O(N)

        raise Exception('Unknown form requested `%s` for Tree' \
            % form)                                                 # O(1)

    def pretty_print(self):                                         # O(N)
        """
        Pretty prints Tree values sequentially

        >>> Tree(42).insert(50).insert(21).pretty_print()
        42 21 50

        >>> Tree(42).insert(50).insert(21).insert(12).insert(14).insert(99) \
            .insert(4).insert(65).pretty_print()
        42 21 12 4 14 50 99 65
        """
        array = self.convert_to_array(self.root)                    # O(N)
        string = ''
        for value in array:                                         # O(N)
            string += str(value) + ' '                              # O(1)

        if string:                                                  # O(1)
            print(string.strip())                                   # O(1)

    def access(self, position):                                     # O(N)
        """
        Accesses Tree at a given position

        >>> Tree(42).insert(31).insert(30).access(20)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position 20 in Tree

        >>> Tree(42).insert(31).insert(30).access(-1)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position -1 in Tree

        >>> Tree(42).insert(22).insert(12).insert(95).insert(1).access(3).value
        12
        """
        def get_movements(current_position, movements):             # O(log(N))
            if current_position == 0:                               # O(1)
                return movements                                    # O(1)

            is_odd = current_position % 2                           # O(1)
            if is_odd:                                              # O(1)
                movements.append('left')                            # O(1)
                parent_position = (current_position - 1) / 2        # O(1)
                return get_movements(parent_position, movements)    # O(log(N))

            movements.append('right')                               # O(1)
            parent_position = (current_position - 2) / 2            # O(1)
            return get_movements(parent_position, movements)        # O(log(N))

        def traverse_movements(node, movements):                    # O(log(N))
            if not node:                                            # O(1)
                return None                                         # O(1)
            if not movements:                                       # O(1)
                return node                                         # O(1)

            movement = movements.pop()                              # O(1)
            next_node = getattr(node, movement)                     # O(1)
            return traverse_movements(next_node, movements)         # O(log(N))

        max_position = pow(2, self.height) - 1                      # O(1)
        if position > max_position or position < 0:                 # O(1)
            raise Exception('Cannot find non-existent position %s in Tree' \
                % position)                                         # O(1)

        movements = get_movements(position, [])                     # O(log(N))
        return traverse_movements(self.root, movements)             # O(log(N))

    def search(self, value):                                        # O(log(N))
        """
        Searches for value in Tree and returns position

        >>> Tree(42).insert(31).insert(30).search(31)
        1

        >>> Tree(42).insert(22).insert(12).insert(95).insert(1).search(1)
        7

        >>> Tree(42).insert(22).insert(12).insert(95).insert(1).search(52)
        -1
        """
        def find(node, find_value, position):                       # O(log(N))
            if not node:                                            # O(1)
                return -1                                           # O(1)
            if node.value == find_value:                            # O(1)
                return position                                     # O(1)

            if find_value < node.value:                             # O(1)
                return find(node.left, find_value, \
                    (2 * position) + 1)                             # O(log(N))
            return find(node.right, find_value, \
                (2 * position + 2))                                 # O(log(N))

        return find(self.root, value, 0)                            # O(log(N))

    def get_parent(self, value, position, height=1):                # O(log(N))
        """
        Get parent node for value in the Tree from a position
        """
        if not position:                                            # O(1)
            return None, height                                     # O(1)
        if value == position.value:                                 # O(1)
            return position, height                                 # O(1)

        lessThan = value < position.value                           # O(1)
        if lessThan and position.left:                              # O(1)
            return self.get_parent(value, position.left, \
                height + 1)                                         # O(log(N))
        if not lessThan and position.right:                         # O(1)
            return self.get_parent(value, position.right, \
                height + 1)                                         # O(log(N))

        return position, height                                     # O(1)

    def insert(self, value):                                        # O(log(N))
        """
        Inserts values into the Tree

        >>> Tree(42).insert(31).insert(30).pretty_print()
        42 31 30

        >>> Tree(42).insert(22).insert(12).insert(95).insert(1).pretty_print()
        42 22 12 1 95

        >>> Tree().insert(40).insert(22).insert(72).insert(-1).pretty_print()
        40 22 -1 72
        """
        parent, height = self.get_parent(value, self.root)          # O(log(N))
        node = Node(value)                                          # O(1)
        if not parent:                                              # O(1)
            self.root = node                                        # O(1)
        elif parent.value > value:                                  # O(1)
            parent.left = node                                      # O(1)
        elif parent.value < value:                                  # O(1)
            parent.right = node                                     # O(1)
        self.height = max(self.height, height + 1)                  # O(1)
        self.size += 1                                              # O(1)

        return self                                                 # O(1)

    def delete(self, position):                                     # O(log(N))
        """
        Deletes value in Tree by position

        # >>> Tree(42).insert(31).insert(30).delete(1).pretty_print()
        # 42 30

        # >>> Tree(42).insert(22).insert(12).insert(95).insert(1) \
        #     .delete(7).delete(0).pretty_print()

        # >>> Tree(42).insert(22).insert(12).insert(95).insert(1) \
        #     .delete(2).delete(1).delete(1).delete(1).delete(1).delete(1) \
        #     .delete(1).delete(1).pretty_print()
        # Traceback (most recent call last):
        # Exception: Cannot find non-existent position 1 in Tree
        """
        def get_parent_position(current_position):                  # O(1)
            is_odd = current_position % 2                           # O(1)
            if is_odd:                                              # O(1)
                return (current_position - 1) / 2                   # O(1)
            return (current_position - 2) / 2                       # O(1)

        def get_child_path(current_position):                       # O(1)
            is_odd = current_position % 2                           # O(1)
            if is_odd:                                              # O(1)
                return 'left'                                       # O(1)
            return 'right'                                          # O(1)

        if position == 0:                                           # O(1)
            self.root = None                                        # O(1)
            self.height = 0                                         # O(1)
            self.size = 0                                           # O(1)
            return self                                             # O(1)

        max_position = pow(2, self.height) - 1                      # O(1)
        if position > max_position or position < 0:                 # O(1)
            raise Exception('Cannot find non-existent position %s in Tree' \
                % position)                                         # O(1)

        parent_position = get_parent_position(position)             # O(1)
        parent_node = self.access(parent_position)                  # O(log(N))
        if not parent_node:                                         # O(1)
            return self                                             # O(1)

        child_path = get_child_path(position)                       # O(1)
        node = getattr(parent_node, child_path)                     # O(1)

        if not node.left and not node.right:                        # O(1)
            setattr(parent_node, child_path, None)                  # O(1)
        elif node.left and not node.right:                          # O(1)
            setattr(parent_node, child_path, node.left)             # O(1)
        elif node.right and not node.left:                          # O(1)
            setattr(parent_node, child_path, node.right)            # O(1)
        else:                                                       # O(1)
            right_node = node.right                                 # O(1)
            print(right_node)                                       # O(1)

        self.size -= 1                                              # O(1)
        return self                                                 # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
