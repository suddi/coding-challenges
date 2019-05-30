# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self):
        self.left = None
        self.right = None

def get_paths(index, stack):
    """
    >>> get_paths(10, [])
    ['left', 'right', 'left']
    """
    if index == 1:
        return stack

    is_odd = index % 2
    if not is_odd:
        parent_node = index / 2
        stack.append('left')
        return get_paths(parent_node, stack)

    parent_node = (index - 1) / 2
    stack.append('right')
    return get_paths(parent_node, stack)

def solution(root, index):
    """
    You are given a complete binary tree; on the last level,
    it’s possible that not all leaves exist (but the ones that do,
    will be filled in in order from left to right). Example:

                    [1]

            [2]                 [3]

      [4]       [5]        [6]     [7]

    [8] [9]  [10] [11]  [12] [13]

    Nodes don’t have any values attached to them, just information about
    their children.
    By going through the tree, one level at a time, from left to right,
    you can assign an index to each node (as in the example above).

    Write a function that determines if a node with a given
    index exists in the tree or not.
    """
    if index < 1:
        return False
    elif index == 1 and root:
        return True

    paths = get_paths(index, [])
    current_node = root
    while paths:
        path = paths.pop()
        node = getattr(current_node, path)
        if not node:
            return False
        current_node = node
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
