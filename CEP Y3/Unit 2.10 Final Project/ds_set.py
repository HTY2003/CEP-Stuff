from ds_hashtable import HashTable
from ds_dyarray import DyArray

class Set:
    '''
    Set ADT for CEP Final Project
    -----------------------------
    This set is inspired by the standard Python set in that it is implemented using a hash table
    with dummy values, allowing for fast constant O(1) lookup time on average, making union, intersections,
    and insertions of values fast by efficiently checking for duplicates.

    O(1) lookup up and deletion time is only ensured by a hash table that uses cuckoo hashing.
    The implementation of cuckoo hashing hash table this class uses can be found in ds_hashtable.py.

    This grants the contact book simple and fast 'AND' and 'OR' searches when
    searching for users with specific attributes and specific values.
    '''
    __slots__ = ('size', 'lookup')

    #---BUILT-IN FUNCTIONS---
    def __init__(self, iterator=[]):
        '''Initializes hash table of default size 100 and length'''
        self.lookup = HashTable()
        for i in iterator: self.lookup[i] = None
        self.size = self.lookup.taken

    def __str__(self):
        '''
        Returns string of all values in the set
        Time complexity: O(n)

        E.g:
        >> a = Set()
        >> a.add(1)
        >> a.add(1)
        >> print(a)
        [1]
        '''
        array = DyArray(0, capacity=self.size)
        for i in self.lookup:
            if i[0] != None: array.append(i[0])
        return str(array)

    def __len__(self):
        '''
        Returns number of values in the set
        Time complexity: O(1)

        E.g:
        >> a = Set()
        >> a.add(1)
        >> a.add(2)
        >> print(len(a))
        1
        '''
        return self.size

    def __iter__(self):
        '''
        Iterates through all values in the set
        Time complexity: O(n)

        E.g:
        >> a = Set()
        >> a.add(1)
        >> a.add(2)
        >> for i in a:
        >>     print(i)
        1
        2
        '''
        return iter(self.lookup)

    def __contains__(self, key):
        '''
        Returns whether the key is in the set
        Time complexity: O(1)

        E.g:
        >> a = Set()
        >> a.add(1)
        >> print(1 in a)
        True
        >> print(2 in a)
        False
        '''
        return key in self.lookup

    __repr__ = __str__

    #---SET FUNCTIONS---
    def add(self, key):
        '''
        Add key into set if key is not already in set
        Time complexity (Average): O(log n)
        Time complexity (Worst case): O(n)

        E.g:
        >> a = Set()
        >> a.add(1)
        >> print(a)
        [1]
        '''
        self.lookup[key] = None
        self.size = self.lookup.taken

    def delete(self, key):
        '''
        Remove key from set if key is in set
        Time complexity: O(1)

        E.g:
        >> a = Set([1])
        >> print(a)
        [1]
        >> a.delete(1)
        >> print(a)
        []
        '''
        del self.lookup[key]
        self.size = self.lookup.taken

    def union(self, setB):
        '''
        Create a new set with all values from both sets (self and setB)
        Time complexity: O(min(n1, n2))

        E.g:
        >> a = Set([1, 2, 3])
        >> b = Set([1, 4, 5])
        >> print(a.union(b))
        [2, 5, 4, 1, 3]
        '''
        newset = Set()
        #takes the longer of the two as a base
        if len(setB) >= self.size:
            newset.lookup = setB.lookup
            for i in self.lookup:
                if i != (None, None): newset.lookup[i[0]] = None
        else:
            newset.lookup = self.lookup
            for i in setB.lookup:
                if i != (None, None): newset.lookup[i[0]] = None
        newset.size = newset.lookup.taken
        return newset

    def intersect(self, setB):
        '''
        Create a new set with values that only appear in both sets (self and setB)
        Time complexity: O(min(n1, n2))

        E.g:
        >> a = Set([1, 2, 3])
        >> b = Set([1, 4, 5])
        >> print(a.intersect(b))
        [1]
        '''
        newset = Set()
        #takes the longer of the two as a base
        if len(setB) >= self.size:
            for i in self.lookup:
                if i != (None, None):
                    if i[0] in setB.lookup: newset.lookup[i[0]] = None
        else:
            for i in setB.lookup:
                if i != (None, None):
                    if i[0] in self.lookup: newset.lookup[i[0]] = None
        newset.size = newset.lookup.taken
        return newset

    def copy(self):
        '''
        Create a shallow copy of the set
        Time complexity: O(1)
        '''
        newset=Set()
        newset.lookup = self.lookup
        newset.size = newset.lookup.taken
        return newset

    def tolist(self):
        '''
        Return a list containing all values in the set
        Time complexity: O(n)
        '''
        def generate():
            for i in self.lookup:
                if i[0] != None: yield i[0]
        return list(generate())
