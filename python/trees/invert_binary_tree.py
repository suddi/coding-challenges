class Node():
    def __init__(self, value):                                      # O(1)
        self.value = value                                          # O(1)
        self.left = None                                            # O(1)
        self.right = None                                           # O(1)

class Tree():
    def __init__(self, value=None):                                 # O(1)
        if value is not None:                                       # O(1)
            self.root = Node(value)                                 # O(1)
        else:                                                       # O(1)
            self.root = None                                        # O(1)

def convert_array_to_nodes(array, index, tree=None, position=None):
    """
    Convert a binary tree in array form to one in node form
    """
    if index < len(array):
        node = Node(array[index])
        if position:
            setattr(tree, position, node)
        else:
            tree = node

        convert_array_to_nodes(array, 2 * index + 1, tree, 'left')
        convert_array_to_nodes(array, 2 * index + 2, tree, 'right')

    if index:
        return None
    return tree

def convert_nodes_to_array(tree, array=None, position=0):
    """
    Convert a binary tree in node form to array
    """
    if tree:
        if array:
            array.append(tree.value)
        else:
            array = [tree.value]
        convert_nodes_to_array(tree.left, array, 2 * position + 1)
        convert_nodes_to_array(tree.right, array, 2 * position + 2)

    if position:
        return None
    return array

def invert_binary_tree(node):
    if node:
        invert_binary_tree(node.left)
        invert_binary_tree(node.right)
        node.left, node.right = node.right, node.left

def solution(array):
    """
    Given a binary tree with nodes, invert it

    # >>> solution([3, 2, 1])
    # [3, 1, 2]
    # >>> solution([2, 4, 5, 6, 3, 1])
    # [2, 5, 4, 6, 1, 3]
    """
    tree = Tree()
    tree = convert_array_to_nodes(array, 0)
    invert_binary_tree(tree)
    return convert_nodes_to_array(tree)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
