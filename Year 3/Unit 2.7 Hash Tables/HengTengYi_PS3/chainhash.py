import sys
import math
import ctypes
from collections import deque

if sys.version_info[0] == 3:
    _get_byte = lambda c: c
else:
    _get_byte = ord

class HashTable:
    """
    Hash table that uses separate chaining to assign to assign key-value pairs

    Separate chaining eliminates the need for collision resolution through probing,
    by chaining values together in a list in the index(hashed key),
    and the FNV1 hash which is fast and random allows for more even spacing between
    values, reducing lookup times.
    """

    def __init__(self,size):
        """
        Initializes hash table array to the size specified. Prime numbers recommended.

        Example usage:
        >>> a = HashTable(37)                                                    """

        #Initializes array and variables
        self._size = size
        self._taken = 0
        PyArrayType  =  ctypes.py_object * self._size
        self._data = PyArrayType(*([None] * self._size))

    def __len__(self):
        """
        Returns current length of hash table array

        Time complexity: O(1)

        Example usage:
        >>> a = HashTable(37)
        >>> print(len(a))
        37                                     """
        return self._size

    def __str__(self):
        """
        Returns string of a hash table array, containing each array index, key, and value it maps to

        Time complexity: O(n)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Jerry", "Tom")
        >>> a.add("Tom", "Jerry")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Jerry : Tom
            Tom : Jerry                                                                                """

        #Heavily formats array into a readable format
        string = ""
        substring = ""
        for index in range(self._size):
            if self._data[index] is None:
                string += str(index) + (" " * (6-len(str(index)))) + "None" + "\n"
            else:
                substring += str(index) + (" " * (6-len(str(index))))
                for i in self._data[index]:
                    substring += str(i[0]).strip("\n") + " : " + str(i[1]).strip("\n") + "\n      "
                string += substring
                string = string [:-5]
                string += "\n"
                substring = ""
        # And returns it
        return string

    __repr__ = __str__

    def __iter__(self):
        """
        Loops through the values(not the keys) of the hash table array
        None values are not iterated.

        Time complexity: O(n)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Jerry", "Tom")
        >>> a.add("Tom", "Jerry")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Jerry : Tom
            Tom : Jerry
        >>> for i in a:
        >>>     print(i)
        Tom
        Jerry                                         """

        values = deque()
        #Loops through original array
        for item in self._data:
            #ignores None values
            if item is not None:
                for subitem in item:
                    values.append(subitem[1])
        return iter(values)


    def __setitem__(self,key,value):
        "Same as self.add(key,value): " + self.add.__doc__
        return self.add(key,value)

    def __getitem__(self,key):
        "Same as self.get(key): " + self.get.__doc__
        return self.get(key)

    def __delitem__(self,key):
        "Same as self.remove(key): " + self.remove.__doc__
        return self.remove(key)

    def __fnv1(self,data):
        """
        Function(hidden) that converts integers and strings into bytes
        before hashing them into index values using the FNV1 algorithm,
        designed for speed and randomness for less collisions.
        """

        #The hash has problems with 0, so it's converted to a string
        if data == 0:
            data = "0"
        #Converts integers and strings to bytes
        if isinstance(data, int):
            data = bytes(data)
        else:
            data = bytes(data, 'utf-8')
        #Hashes bytes through the __fnv1 algorithm into a 32-bit value
        hval = 0x811c9dc5
        for byte in data:
            hval = (hval * 0x01000193) % (2**16)
            hval = hval ^ _get_byte(byte)
        #Returns modulus of hashed value by the size of the hash table
        return hval % self._size

    def __chain(self,key,value):
        """
        Function(hidden) that adds value to the list in the index of the array.
        Since the collections.deque object has O(1) append time, this action is pretty fast.
        """
        #Hashes the key into the index
        index = self.__fnv1(key)
        #Starts chain if it doesn't exist yet
        if self._data[index] is None:
            self._taken += 1
            self._data[index] = deque()
        #Adds value to deque in index
        self._data[index].append((key,value))

    def __search(self,key):
        """
        Function(hidden) that attempts to find the value in the chain which
        the key maps to. If the key is not found, None is returned.
        """
        #Hashes the key into the index
        index = self.__fnv1(key)
        #Search through any non-empty chains in the index
        if self._data[index] is not None:
            for i in range(len(self._data[index])):
                if self._data[index][i][0] is key:
                    return index, self._data[index][i][1]
        #If the index is empty, return None, None
        return None, None

    def add(self,key,value):
        """
        Function that assigns value to the hash table array using the
        FNV1-hashed version of the key as the array index

        Two of the same keys CAN be used in one table, but when searching,
        only the value of the first instance of the key will be returned until it is removed

        Time complexity: O(1)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Jerry","Tom")
        >>> a.add("Tom","Jerry")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Jerry : Tom
            Tom : Jerry                                             """
        #Chains value to the chain in that index
        #The collection.deque allows appending to be O(1), hence the fast speed
        self.__chain(key, value)

    def get(self,key):
        """
        Function that retrieves and returns the value which the key maps to
        If the key is not in the hash table, it returns None.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Jerry", "Tom")
        >>> print(a.get("Jerry"))
        Tom                                                                                                 """
        return self.__search(key)[1]

    def remove(self,key):
        """
        Function that returns and removes the value which the key maps to
        If the key is not in the hash table, it returns None.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Jerry", "Tom")
        >>> a.add("Tom", "Jerry")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Jerry : Tom
            Tom : Jerry
        >>> a.remove("Tom")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Jerry : Tom                                                                """

        index = self.__search(key)
        try:
            #removes value from the deque in the index
            self._data[index[0]].remove((key,index[1]))
            if len(self._data[index[0]]) == 0:
                #account for loss of a filled deque
                self._taken -= 1
            return index
        #return None if index is not a deque object
        except ValueError:
            return None

    def used(self):
        """
        Function that returns the number of chains in the array
        This can be used if the user wants to see how full or empty the array is,
        and use the self.rehash() function to resize the array accordingly.

        This does NOT refer to the number of key-value pairs in the array, just the
        number of non-empty chains in the array which the pairs are stored in.

        Time complexity: O(1)

        E.g:
        >>> a = HashTable(1)
        >>> a.add("Jerry","Tom")
        >>> a.add("Tom", "Jerry")
        >>> print a.used()
        1                                                                    """
        #Return number of non-empty chains in hash table
        return self._taken

    def checkrehash(self,max=80,min=20,multiplier=2,divisor=2):
        """
        Function a user can use to resize the array based on how full it is (no. of chains in the array)
        If the array exceeds <max> % capacity(80% by default) in use, the array will multiply itself by the multiplier (2 by default).
        If the array goes under <min>% capacity(20% by default), the array will divide itself by the divisor (2 by default).

        This allows users to trim or expand their arrays without interfering with their liberty to resize at will.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        E.g:
        >>> print(A.used(), len(A))
        4 5
        >>> A.checkrehash()
        >>> print(A.used(), len(A))
        4 10                                                                             """

        assert min <= max, "Minimum cannot exceed maximum"
        #Resizes array if too full
        if self._taken >= (self._size * max / 100):
            self.rehash(int(self._size * multiplier))
        #If not, resize if too empty
        elif self._taken <= (self._size * min / 100):
            self.rehash(int(self._size / divisor))

    def rehash(self,size):
        """
        Function that resizes the hash table array to the specified size,
        allowing it to store more key-value pairs.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = HashTable(10)
        >>> print(len(a))
        10
        >>> a.resize(128)
        >>> print(len(a))
        128                                                                              """

        self._size = size
        self._taken = 0
        self._olddata = self._data
        #Makes new array of specified size
        PyArrayType  =  ctypes.py_object * self._size
        self._data = PyArrayType(*([None] * self._size))
        #If index is not None, it is added to the new array
        for item in self._olddata:
            if item is not None:
                for subitem in item:
                    self.add(subitem[0], subitem[1])
        self._olddata = 0
