# -*- coding: utf-8 -*-

class Array(object):
    def __init__(self, value=None):                                 # O(1)
        if value is not None:                                       # O(1)
            self.array = [value]                                    # O(1)
            self.length = 1                                         # O(1)
        else:                                                       # O(1)
            self.array = []                                         # O(1)
            self.length = 0                                         # O(1)

    def get_length(self):                                           # O(1)
        """
        Returns the length of the Array

        >>> Array(42).insert(22, 1).insert(12, 1).insert(95) \
            .insert(1, 0).get_length()
        5
        """
        return self.length                                          # O(1)

    def pretty_print(self):                                         # O(N)
        """
        Pretty prints Array values sequentially

        >>> Array(42).pretty_print()
        42
        """
        for count, value in enumerate(self.array):                  # O(N)
            print value,                                            # O(1)
            if count < self.length - 1:                             # O(1)
                print '-',                                          # O(1)

    def access(self, position):                                     # O(1)
        """
        Accesses Array at a given position

        >>> Array(42).insert(31).insert(30, 0).access(20)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position 20 in Array

        >>> Array(42).insert(31).insert(30, 0).access(-1)
        Traceback (most recent call last):
        Exception: Cannot find non-existent position -1 in Array

        >>> Array(42).insert(22, 1).insert(12, 1).insert(95) \
            .insert(1, 0).access(3)
        22
        """
        if position >= self.length or position < 0:
            raise Exception('Cannot find non-existent position ' \
                + '%d in Array' % position)                         # O(1)

        return self.array[position]                                 # O(1)

    def search(self, value):                                        # O(N)
        """
        Searches for value in Array and returns position

        >>> Array(42).insert(31).insert(30, 0).search(31)
        2

        >>> Array(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .search(22)
        3

        >>> Array(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .search(52)
        -1
        """
        for count, array_value in enumerate(self.array):            # O(N)
            if array_value == value:                                # O(1)
                return count                                        # O(1)

        return -1                                                   # O(1)

    def insert(self, value, position=None):                         # O(N)
        """
        Inserts values into the Array

        Insert covers 2 cases:
        1) Insert at the end of the Array                           # O(1)
        2) Insert elsewhere in the Array                            # O(N)

        >>> Array(42).insert(31).insert(30, 0).pretty_print()
        30 - 42 - 31

        >>> Array(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .pretty_print()
        1 - 42 - 12 - 22 - 95
        """
        if position is None or position == self.length:             # O(1)
            self.array.append(value)                                # O(1)
        elif position > self.length or position < 0:                # O(1)
            raise Exception('Cannot find non-existent position ' \
                + '%d in Array' % position)                         # O(1)
        else:                                                       # O(1)
            self.array.insert(position, value)                      # O(1)
        self.length += 1                                            # O(1)

        return self                                                 # O(1)

    def delete(self, position=None):                                # O(N)
        """
        Deletes value in Array by position

        Delete covers 2 cases:
        1) Delete at the end of the Array                           # O(1)
        2) Delete elsewhere in the Array                            # O(N)

        >>> Array(42).insert(31).insert(30, 0).delete(1).delete().pretty_print()
        30

        >>> Array(42).insert(22, 1).insert(12, 1).insert(95).insert(1, 0) \
            .delete().delete(0).delete(1).pretty_print()
        42 - 22

        >>> Array(42).insert(22).insert(12).insert(95).insert(1) \
            .delete().delete().delete().delete().delete().delete().delete() \
            .delete().pretty_print()
        """
        if not self.length:                                         # O(1)
            return self                                             # O(1)
        if position is None or position == self.length - 1:         # O(1)
            self.array.pop()                                        # O(1)
        elif position >= self.length or position < 0:               # O(1)
            raise Exception('Cannot find non-existent position ' \
                + '%d in Array' % position)                         # O(1)
        else:                                                       # O(1)
            self.array.pop(position)                                # O(N)
        self.length -= 1                                            # O(1)

        return self                                                 # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
