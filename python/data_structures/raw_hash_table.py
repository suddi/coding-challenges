def create_hash(key, size):                                         # O(1)
    """
    Creates a hash by taking the first character in a string, getting its
    ASCII value and apply a modular function to the provided size

    >>> create_hash(42, 5)
    4
    >>> create_hash(42, 4)
    0
    >>> create_hash(122.12, 4)
    1
    >>> create_hash('apple', 128)
    97
    >>> create_hash('apple', 97)
    0
    """
    if isinstance(key, (int, float)):                               # O(1)
        key_string = '{0}'.format(key)                              # O(1)
        char = key_string[0]                                        # O(1)
        return int(char) % size                                     # O(1)
    return ord(key[0]) % size                                       # O(1)

def find(array, key):                                               # O(N)
    """
    Find an element in an array of tuples

    >>> find([('human', 42), ('cat', 22)], 'cat')
    1
    >>> find([('human', 42), ('cat', 22)], 'dog')
    -1
    """
    length = len(array)                                             # O(1)
    for i in range(0, length):                                      # O(N)
        element = array[i]                                          # O(1)
        if element[0] == key:                                       # O(1)
            return i                                                # O(1)

    return -1                                                       # O(1)

class HashTable():
    def __init__(self, size=128):                                   # O(1)
        self.table = [[] for _ in range(0, size)]                   # O(1)
        self.size = size                                            # O(1)
        self.length = 0                                             # O(1)

    def get_length(self):                                           # O(1)
        """
        Returns the length of the HashTable

        >>> HashTable().insert('human', 42).insert('cat', 22) \
            .insert('dog', 12).insert('cat', 95).insert('ant', 1) \
            .get_length()
        4
        """
        return self.length                                          # O(1)

    def pretty_print(self):                                         # O(N^2)
        """
        Pretty prints HashTable values sequentially

        >>> HashTable().insert('human', 42).insert('cat', 22) \
            .insert('dog', 12).insert('cat', 95).insert('ant', 1) \
            .pretty_print()
        ('ant', 1)
        ('cat', 95)
        ('dog', 12)
        ('human', 42)
        """
        string = ''                                                 # O(1)
        for array in self.table:                                    # O(N)
            for element in array:                                   # O(N)
                string += "('{0}', {1})\n".format(
                    element[0], element[1]
                )                                                   # O(1)

        if string:                                                  # O(1)
            print(string.strip())                                   # O(1)

    def access(self, key):                                          # O(1)
        """
        Accesses HashTable at a given key

        >>> HashTable().insert('human', 42).insert('cat', 22) \
            .insert('dog', 12).insert('cat', 95).insert('ant', 1) \
            .access('cat')
        ('cat', 95)
        >>> HashTable().insert('human', 42).insert('cat', 22) \
            .insert('dog', 12).insert('cat', 95).insert('ant', 1) \
            .access('pig')
        """
        hash_key = create_hash(key, self.size)                      # O(1)
        position = find(self.table[hash_key], key)                  # O(<N)
        if position > -1:                                           # O(1)
            return self.table[hash_key][position]                   # O(1)
        return None                                                 # O(1)

    def insert(self, key, value):                                   # O(1)
        """
        Inserts a key-value pair into the HashTable

        >>> HashTable().insert('human', 42).insert('cat', 22) \
            .insert('dog', 12).insert('cat', 95).insert('ant', 1) \
            .access('cat')
        ('cat', 95)
        """
        hash_key = create_hash(key, self.size)                      # O(1)
        # NOTE: We can either apply linear probing or chaining
        #       Here we are applying chaining
        position = find(self.table[hash_key], key)                  # O(<N)
        store = (key, value)                                        # O(1)
        if position > -1:                                           # O(1)
            self.table[hash_key][position] = store                  # O(1)
        else:                                                       # O(1)
            self.table[hash_key].append(store)                      # O(1)
            self.length += 1                                        # O(1)

        return self                                                 # O(1)

    def delete(self, key):
        """
        Delete a key-value from the HashTable

        >>> HashTable().insert('human', 42).insert('cat', 22) \
            .insert('dog', 12).insert('cat', 95).insert('ant', 1) \
            .delete('cat').access('cat')
        """
        hash_key = create_hash(key, self.size)                      # O(1)
        position = find(self.table[hash_key], key)                  # O(<N)
        if position > -1:                                           # O(1)
            del self.table[hash_key][position]                      # O(1)

        return self                                                 # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
