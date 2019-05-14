#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.entries = 0
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def __getitem__(self, key):
        # Get an item with subscripting syntax
        return self.get(key)

    def __setitem__(self, key, value):
        # Set item with syntax
        self.set(key, value)

    def __contains__(self, key):
        # Check if item is contained
        return self.contains(key)

    def __len__(self):
        # Check length
        return self.entries

    def __iterable__(self):
        # Use as iterable object
        return self.generate()

    # Python generator returns an object we can iterate over
    def generate(self):
        for bucket in self.buckets:
            for entry in bucket:
                yield entry

    def keys(self):
        """
        Return a list of all keys in this hash table.

        Running time: 0(l). Where (l) (n/b) The number of entries we have divided by the amount of buckets.
        Were always traversing every node in the linked list in each bucket in the hashtable and storing the 
        keys in an array.
        """
        # Store all keys in an array
        all_keys = []
        # Loop through the buckets
        for bucket in self.buckets:
            # Loop through items in buckets
            for key, value in bucket.items():
                # Append all of the keys to the keys array
                all_keys.append(key)
        # Return the array of values
        return all_keys

    def values(self):
        """
        Return a list of all values in this hash table.

        Running time: 0(l). Where (l) (n/b) The number of entries we have divided by the amount of buckets.
        Were always traversing every node in the linked list in each bucket in the hashtable and storing the
        values in an array.
        """
       # Store all values in an array
        all_values = []
        # Loop through the buckets
        for bucket in self.buckets:
            # Loop through the items in the buckets
            for key, value in bucket.items():
                # Append all the values to the values array
                all_values.append(value)
        # Return the array of values
        return all_values

    def items(self):
        """
        Return a list of all items (key-value pairs) in this hash table.

        Running time: 0(l). Where (l) (n/b) The number of entries we have divided by the amount of buckets.
        Were always traversing every node in the linked list in each bucket in the hashtable and storing the 
        key-value in an array.
        """
        # Store all items in an array 
        all_items = []
        # Loop through all of the buckets
        for bucket in self.buckets:
            # Push items to all items array
            all_items.extend(bucket.items())
        # Return all item array
        return all_items

    def length(self):
        """
        Return the number of key-value entries by traversing its buckets.

        Running time: O(1) Returning a stored variable.
        """
        return self.entries


    def contains(self, key):
        """
        Return True if this hash table contains the given key, or False.

        Running time:
        Best Case: 0(1): If the hashtabe only contains one entry or is empty
        ----------------------------------------------------------------------------
        Worst Case: 0(l). Where (l) (n/b) The number of entries we have divided by the amount of buckets.
        You have to traverse the entire hashtable to see if the linked list contains the value were searching for.
        """
        index = self._bucket_index(key)
        found = False
        # Find bucket where given key belongs
        key_value = self.buckets[index].find(lambda item: item[0] == key) # 0(l)
        # Check if key-value entry exists in bucket
        if key_value is not None:
            found = True
        # Return key-value
        return found

    def get(self, key):
        """
        Return the value associated with the given key, or raise KeyError.

        Running time:
        Best Case: 0(1): If ithe value is assocaited with the first key in the first bucket
        ----------------------------------------------------------------------------
        Worst Case: 0(l). Where (l) (n/b) The number of entries we have divided by the amount of buckets.
        You have to traverse the entire hashtable to find the item that you want
        """
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find bucket where given key belongs
        found_item = bucket.find(lambda item: item[0] == key) # 0(l)
        # Check if key-value entry exists in bucket
        if found_item is not None:
            # If found, return value associated with given key
            return found_item[1]
        # Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """
        Insert or update the given key with its associated value.

        Running time: 
        Best Case: O(1) The key value we are updating is the first item in the first bucket.
        ----------------------------------------------------------------------------
        Worst Case: 0(l). Where (l) (n/b) The number of entries we have divided by the amount of buckets.
        You have to traverse the hashtable to find the node you want to set
        """
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find bucket where given key belongs
        found_item = bucket.find(lambda item: item[0] == key)  # 0(l)
        # Check if key-value entry exists in bucket
        if found_item is not None:
            # If found, update value associated with given key
            bucket.delete(found_item) # 0(l)
            self.entries -= 1
        # Otherwise, insert given key-value entry into bucket
        bucket.append((key, value))
        self.entries += 1
    def delete(self, key):
        """
        Delete the given key from this hash table, or raise KeyError.

        Running time: 
        Best Case: O(1): The key-value being deleted is the first item in the first bucket.
        ----------------------------------------------------------------------------
        Worst Case: 0(l). Where (l) (n/b) The number of entries we have divided by the amount of buckets.
        You have to traverse the entire hashtable to find the node you want to delete
        """
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find bucket where given key belongs
        key_value = bucket.find(lambda item: item[0] == key) # 0(l)
        # Check if key-value entry exists in bucket
        if key_value is not None:
            # If found, delete entry associated with given key
            bucket.delete(key_value)
            self.entries -= 1
        # Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True 
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
