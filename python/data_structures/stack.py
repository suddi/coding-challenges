class Stack():
    def __init__(self, value=None):                                 # O(1)
        if value is not None:                                       # O(1)
            self.stack = [value]                                    # O(1)
            self.length = 1                                         # O(1)
        else:                                                       # O(1)
            self.stack = []                                         # O(1)
            self.length = 0                                         # O(1)

    def get_length(self):                                           # O(1)
        """
        Returns the length of the Stack

        >>> Stack(42).insert(22).insert(12).insert(95).insert(1).get_length()
        5
        """
        return self.length                                          # O(1)

    def pretty_print(self):                                         # O(N)
        """
        Pretty prints Stack values sequentially

        >>> Stack(42).pretty_print()
        42
        """
        string = ''                                                 # O(1)
        for count, value in enumerate(self.stack):                  # O(N)
            string += str(value) + ' '                              # O(1)
            if count < self.length - 1:                             # O(1)
                string += '-> '                                     # O(1)

        if string:                                                  # O(1)
            print(string.strip())                                   # O(1)

    def access(self, position):                                     # O(N)
        """
        Accesses Stack at a given position

        >>> Stack(42).insert(31).insert(30).access(20)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position 20 in Stack

        >>> Stack(42).insert(31).insert(30).access(-1)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position -1 in Stack

        >>> Stack(42).insert(22).insert(12).insert(95).insert(1).access(3)
        95
        """
        if position >= self.length or position < 0:
            raise Exception('Cannot find non-existent position ' \
                + '%d in Stack' % position)                         # O(1)

        for count, stack_value in enumerate(self.stack):            # O(N)
            if count == position:                                   # O(1)
                return stack_value                                  # O(1)

        return -1                                                   # O(1)

    def search(self, value):                                        # O(N)
        """
        Searches for value in Stack and returns position

        >>> Stack(42).insert(31).insert(30).search(31)
        1

        >>> Stack(42).insert(22).insert(12).insert(95).insert(1).search(22)
        1

        >>> Stack(42).insert(22).insert(12).insert(95).insert(1).search(52)
        -1
        """
        for count, stack_value in enumerate(self.stack):            # O(N)
            if stack_value == value:                                # O(1)
                return count                                        # O(1)

        return -1                                                   # O(1)

    def insert(self, value):                                        # O(1)
        """
        Inserts value into the Stack, only possible at the end

        Insert covers 1 case:
        1) Insert at the end of the Stack                           # O(1)

        >>> Stack(42).insert(31).insert(30).pretty_print()
        42 -> 31 -> 30

        >>> Stack(42).insert(22).insert(12).insert(95).insert(1).pretty_print()
        42 -> 22 -> 12 -> 95 -> 1
        """
        self.stack.append(value)                                    # O(1)
        self.length += 1                                            # O(1)

        return self                                                 # O(1)

    def delete(self):                                               # O(1)
        """
        Deletes value in Stack, only possible at the end

        Delete covers 1 case:
        1) Delete at the end of the Stack                           # O(1)

        >>> Stack(42).insert(31).insert(30).delete().delete().pretty_print()
        42

        >>> Stack(42).insert(22).insert(12).insert(95).insert(1) \
            .delete().delete().delete().pretty_print()
        42 -> 22

        >>> Stack(42).insert(22).insert(12).insert(95).insert(1) \
            .delete().delete().delete().delete().delete().delete().delete() \
            .delete().pretty_print()
        """
        if self.length:                                             # O(1)
            self.stack.pop()                                        # O(1)
            self.length -= 1                                        # O(1)

        return self                                                 # O(1)

    def push(self, value):                                          # O(1)
        """
        Push a value at the end of the stack to demonstrate LIFO capability of Stack

        >>> Stack(42).push(31).push(30).pretty_print()
        42 -> 31 -> 30

        >>> Stack(42).push(22).push(12).push(95).push(1).pretty_print()
        42 -> 22 -> 12 -> 95 -> 1
        """
        self.stack.append(value)                                    # O(1)
        self.length += 1                                            # O(1)

        return self                                                 # O(1)

    def pop(self):                                                  # O(1)
        """
        Pop a value out at the of the stack to demonstrate LIFO capability of Stack

        >>> Stack(42).push(31).push(30).pop()
        30

        >>> Stack(42).push(22).push(12).push(95).push(1).pop()
        1

        >>> Stack().pop()
        """
        if not self.length:                                         # O(1)
            return None                                             # O(1)

        value = self.stack.pop()                                    # O(1)
        self.length -= 1                                            # O(1)

        return value                                                # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
