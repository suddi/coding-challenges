# -*- coding: utf-8 -*-

class HashTable():
    def __init__(self, key, value):                                 # O(1)
        if value is not None:                                       # O(1)
            self.hash_table = {key: value}                          # O(1)
            self.length = 1                                         # O(1)
        else:                                                       # O(1)
            self.hash_table = {}                                    # O(1)
            self.length = 0                                         # O(1)

    def get_length(self):                                           # O(1)
        """
        Returns the length of the HashTable

        >>> HashTable('human', 42).insert('cat', 22).insert('dog', 12) \
            .insert('cat', 95).insert('ant', 1).get_length()
        4
        """
        return self.length                                          # O(1)

    def pretty_print(self):                                         # O(N)
        """
        Pretty prints HashTable values sequentially

        >>> HashTable('human', 42).pretty_print()
        ('human', 42)
        """
        string = ''                                                 # O(1)
        for key, value in self.hash_table.items():                  # O(N)
            string += "('%s', %s) " % (key, value)                  # O(1)

        if string:                                                  # O(1)
            print(string.strip())                                   # O(1)

    def access(self, key):                                          # O(1)
        """
        Accesses HashTable at a given key

        >>> HashTable('human', 42).insert('cat', 31).insert('dog', 30) \
            .access('rabbit')
        Traceback (most recent call last):
        Exception: Cannot find non-existent key `rabbit` in HashTable

        >>> HashTable('human', 42).insert('cat', 22).insert('dog', 12) \
            .insert('rabbit', 95).insert('ant', 1).access('dog')
        12
        """
        value = self.hash_table.get(key)
        if not value:
            raise Exception('Cannot find non-existent key ' \
                + '`%s` in HashTable' % key)                        # O(1)

        return value                                                # O(1)

    def search(self, value):                                        # O(N)
        """
        Searches for value in HashTable and returns key

        >>> HashTable('human', 42).insert('cat', 31).insert('dog', 30) \
            .search(31)
        'cat'

        >>> HashTable('human', 42).insert('cat', 22).insert('dog', 12) \
            .insert('rabbit', 95).insert('ant', 1).search(22)
        'cat'

        >>> HashTable('human', 42).insert('cat', 22).insert('dog', 12) \
            .insert('rabbit', 95).insert('ant', 1).search(52)
        """
        for key, table_value in self.hash_table.items():            # O(N)
            if table_value == value:                                # O(1)
                return key                                          # O(1)

        return None                                                 # O(1)

    def insert(self, key, value):                                   # O(1)
        """
        Inserts key and value into the HashTable

        >>> HashTable('human', 42).insert('cat', 31).insert('cat', 30) \
            .pretty_print()
        ('human', 42) ('cat', 30)

        >>> HashTable('human', 42).insert('cat', 22).insert('dog', 12) \
            .insert('rabbit', 95).insert('ant', 1).pretty_print()
        ('human', 42) ('cat', 22) ('dog', 12) ('rabbit', 95) ('ant', 1)
        """
        existing_value = self.hash_table.get(key)                   # O(1)
        self.hash_table[key] = value                                # O(1)
        if not existing_value:                                      # O(1)
            self.length += 1                                        # O(1)

        return self                                                 # O(1)

    def delete(self, key):                                          # O(1)
        """
        Deletes value in HashTable by key

        >>> HashTable('human', 42).insert('cat', 31).insert('dog', 30) \
            .delete('cat').delete('dog').pretty_print()
        ('human', 42)

        >>> HashTable('human', 42).insert('cat', 22).insert('cat', 12) \
            .insert('dog', 95).insert('ant', 1).delete('ant').delete('cat') \
            .delete('cat').delete('dog').delete('human').delete('cat') \
            .delete('dog').delete('human').delete('ant').pretty_print()
        """
        existing_value = self.hash_table.get(key)                   # O(1)
        if existing_value:                                          # O(1)
            del self.hash_table[key]                                # O(1)
            self.length -= 1                                        # O(1)

        return self                                                 # O(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
