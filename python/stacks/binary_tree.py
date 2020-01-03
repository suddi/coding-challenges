class Node():
    def __init__(self):                                             # O(1)
        self.left = None                                            # O(1)
        self.right = None                                           # O(1)

def get_paths(index, stack):                                        # O(logN)
    """
    >>> get_paths(10, [])
    ['left', 'right', 'left']
    """
    if index == 1:                                                  # O(1)
        return stack                                                # O(1)

    is_odd = index % 2                                              # O(1)
    if not is_odd:                                                  # O(1)
        parent_node = index / 2                                     # O(1)
        stack.append('left')                                        # O(1)
        return get_paths(parent_node, stack)                        # O(1)

    parent_node = (index - 1) / 2                                   # O(1)
    stack.append('right')                                           # O(1)
    return get_paths(parent_node, stack)                            # O(logN)

def solution(root, index):                                          # O(logN)
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
    if index < 1:                                                   # O(1)
        return False                                                # O(1)
    if index == 1 and root:                                         # O(1)
        return True                                                 # O(1)

    paths = get_paths(index, [])                                    # O(logN)
    current_node = root                                             # O(1)
    while paths:                                                    # O(<N)
        path = paths.pop()                                          # O(1)
        node = getattr(current_node, path)                          # O(1)
        if not node:                                                # O(1)
            return False                                            # O(1)
        current_node = node                                         # O(1)
    return True                                                     # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
