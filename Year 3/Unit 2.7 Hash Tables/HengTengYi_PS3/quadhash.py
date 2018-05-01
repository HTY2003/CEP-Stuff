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
    Hash table that uses quadratic probing and the FNV1 hash to assign key-value pairs

    The FNV1 hashing algorthm is used to hash a key, using the hashed key as the index
    which stores a value in an array. To handle colliding hashes, a quadratic probe of
    (i*i+i)/2 is applied, allowing the hash to visit every index in the array.

    When a key is called, the value can be returned, since the value is mapped to the key.
    In addition, the table size (which must be a power of 2) is doubled when the table is full.
    """

    def __init__(self, size=64, autocal=False):
        """
        Initializes the hash table array of size given (64 by default)

        The size of the array must be 64 by default, or any other power of 2 specified.
        AssertionError raised if the table size given is not a power if 2 (unless autocal is enabled).

        When autocal is enabled, the program will upsize any non-power of 2 to the next highest power of 2
        such that the table will not resize when given number of elements are added, saving valuable time.

        Example usage:
        >>> a = HashTable()
        >>> print(len(a))
        64
        >>> b = HashTable(5, autocal = True)
        >>> print(len(b))
        8
        >>> c = HashTable(16)
        >>> print(len(c))
        16                                                                                            """

        #Auto-calculates if enabled
        if autocal:
            self._size = 2
            while size > self._size:
                self._size *= 2
        else:
        #If not, asserts power of 2 table size
            assert math.log2(size).is_integer(), "Hash table size must be a power of 2"
            self._size = size
        #Initializes starting array and variables
        self._taken = 0
        PyArrayType  =  ctypes.py_object * self._size
        self._data = PyArrayType((*[(None, None)] * self._size))

    def __len__(self):
        """
        Returns current length of hash table array

        Time complexity: O(1)

        Example usage:
        >>> a = HashTable(64)
        >>> print(len(a))
        64                                     """
        return self._size

    def __str__(self):
        """
        Returns string of  hash table array, containing (in order) each array index, key and value it maps to

        Time complexity: O(n)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Tom" , "Tom")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Tom : Tom                                                                                       """

        string = ""
        #formats array to a string that doesn't make you feel nauseous
        for i in range(self._size):
            if self._data[i][1] is not None:
                string += str(i) +\
                "    " +\
                str(self._data[i][0]).strip("\n") +\
                " : " +\
                str(self._data[i][1]).strip("\n") +\
                "\n"
            else:
                string += str(i) + "    None\n"
        #returns it
        return string

    __repr__ = __str__

    def __iter__(self):
        """
        Loops through the values (not keys) of the hash table array
        None values are not iterated in the loop.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Tom", "Tom")
        >>> for i in a:
        >>>     print(i)
        Tom                                                       """

        values = deque()
        #Loops through original array
        for i in self._data:
            #Excludes None values since they're useless
            if i[1] is not None:
                #Adds them to a new list
                values.append(i[1])
        return iter(values)

    def __setitem__(self,key,value):
        "Same as self.add(key,value): " + self._add.__doc__
        self.add(key, value)

    def __getitem__(self,key):
        "Same as self.get(key): " + self.get.__doc__
        return self.get(key)

    def __delitem__(self,key):
        "Same as self.remove(key): " + self.remove.__doc__
        return self.remove(key)

    def __fnv1(self, data):
        """
        Function (hidden) that converts integers and strings into bytes
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
            data = bytes(data, "utf-8")
        #Hashes bytes through the FNV1 algorithm into a 32-bit value
        hval = 0x811c9dc5
        for byte in data:
            hval = (hval * 0x01000193) % (2**32)
            hval = hval ^ _get_byte(byte)
        #Returns modulus of hashed value by the size of the hash table
        return hval % self._size

    def __quadprobe(self,key,value):
        """
        Function (hidden) that attempts to assigns values to the given index(hashed key).
        Should the index already be filled, a quadratic probe of (i*i+1)/2 will be
        applied to the original index until the value is assigned.

        With this probe, along with the hash table being a power of two, every index
        in the hash table array will be visited, ensuring there is no unused space
        in the array before it is resized and rehashed, eliminating wasted memory.
        """

        #Derives array index from hashed key using the self.__fnv1 function
        index = self.__fnv1(key)
        baseindex = index
        testindex = index
        #Tries to assign value to every index, looping through the entire array if need
        for i in range(1, self._size+1):
            #Assign value if that slot is empty
            if self._data[testindex][0] is None or self._data[testindex][0] is "":
                self._data[testindex] = (key, value)
                return
            elif self._data[testindex][0] is not key:
                #Applies probe and tries again if it fails
                testindex = int(baseindex + (i**2+i)/2)
                testindex %= self._size
            else:
                #Returns error for duplicate keys
                raise ValueError("Key has already been used in hash table")

    def __search(self,key):
        """
        Function(hidden) that goes through the same quadratic probe in self._quadprobe
        to look for which value the key maps to before returning the found value.
        """

        #Derives array index from hashed key using the self.__fnv1 function
        index = self.__fnv1(key)
        baseindex = index
        testindex = index
        for i in range(1, self._size+1):
            #Checks if data in array's index corresponds to the hash value
            if self._data[testindex][0] == key:
                return testindex, self._data[testindex][1]
            elif self._data[testindex][0] is None:
                return None, None
            else:
                #Applies the probe and tries again if it fails
                testindex = int(baseindex + (i**2+i)/2)
                testindex %= self._size
        return None, None

    def add(self,key,value):
        """
        Function that use the input key-value pairs and assigns the given value
        to the hash table array with the FNV1-hashed key as the array index

        Raises ValueError if two of the same keys are in one table. (keys must be unique)

        Also doubles array size if table is completely full

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n^2)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Jerry", "Tom")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Jerry : Tom                                                     """

        #Resizes array when table is full
        if self._taken + 1 == self._size:
            self.rehash(self._size*2)
        #Attempts to assign value to the index, and applies quadratic probe if needed using the self.__quadprobe function
        self.__quadprobe(key,value)
        self._taken += 1

    def get(self,key):
        """
        Function that retrieves and returns the value which the given key maps to
        If the key is not in the hash table, it returns None.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Jerry", "Tom")
        >>> print(a.get("Jerry"))
        Tom                                                                             """

        #Searches for the key's value using the self._search function and returns value
        return self.__search(key)[1]

    def remove(self,key):
        """
        Function that retrieves and returns the value which the given key is mapped to,
        then sets the index slot to empty, removing the key-value pair from the
        hash table. If the key is not in the hash table, it returns None.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = HashTable(4)
        >>> a.add("Jerry", "Tom")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Jerry : Tom
        >>> a.remove("Jerry")
        >>> print(a)
        0   None
        1   None
        2   None
        3   None
                                                                                    """
        #Finds index using self.__search function
        foundindex = self.__search(key)
        #Sets key value in found index to "", our special flag that allows the search probe to continue in the future
        #also sets value to None
        if foundindex[0] is not None:
            self._data[foundindex[0]] = ("", None)
            self._taken -= 1
        #Returns index, like in self.__search()
        return foundindex[1]

    def used(self):
        """
        Function that returns the number of non-empty indexes in the array
        Can be used if the user wants to see how full or empty the array is.

        Time complexity: O(1)

        E.g:
        >>> a = HashTable(4)
        >>> a.add("Tom", "Tom")
        >>> a.add(1, "hi")
        >>> a.add("Hello Earth", "Hello Mars")
        >>> print a.used()
        3                                                                   """
        return self._taken

    def checkrehash(self,max=80,min=20,multiplier=2,divisor=2):
        """
        Function that can be used to resize the array based on how full it is

        If the array exceeds <max> % capacity(80% by default) in use, the array will multiply itself by the multiplier (2 by default).
        If the array goes under <min>% capacity(20% by default), the array will divide itself by the divisor (2 by default).

        This allows users to trim or expand their arrays without interfering with their liberty to resize at will.

        Time complexity(average): O(n)
        Time complexity(worst-case): O(n^2)

        E.g:
        >>> A = HashTable(5)
        >>> for i in range(4):
        >>>     A.add(i)
        >>> print(A.used(), len(A))
        4 5
        >>> A.checkrehash()
        >>> print(A.used(), len(A))
        4 10                                                                           """

        assert min <= max, "Minimum cannot exceed maximum"
        #Resizes array if too full
        if self._taken >= (self._size * max / 100):
            self.rehash(int(self._size * multiplier))
        #If not, resize if too empty
        elif self._taken <= (self._size * min / 100):
            self.rehash(int(self._size / divisor))

    def rehash(self,size,autocal=False):
        """
        Function that resizes the hash table array to the specified size, allowing it to store more key-value pairs.

        The specified size must be a power of 2 and able to fit all elements.
        If not, AssertionError is raised (unless autocal is enabled).

        If autocal is enabled, the function will automatically upscale any
        non-power of 2 to the next nearest power of 2.

        Time complexity(average): O(n)
        Time complexity(worst-case): O(n^2)

        Example usage:
        >>> a = HashTable()
        >>> print(len(a))
        64
        >>> a.resize(128)
        >>> print(len(a))
        128                                                                              """

        if autocal:
            #Auto-calculates size
            self._size = 2
            while size > self._size:
                self._size *= 2
        else:
            #or asserts size rules
            assert math.log2(size).is_integer(), "Hash table size must be a power of 2"
            assert self._taken <= size, "Existing elements cannot fit within array of size specified"
            self._size = size

        self._taken = 0
        self._olddata = self._data
        #Makes new array twice the original size
        PyArrayType  =  ctypes.py_object * self._size
        self._data = PyArrayType(*([(None, None)] * self._size))
        #Assigns each value in the old array one-by-one to the new array
        for i in self._olddata:
            if i[0] is not None and i[0] is not "":
                self.add(i[0], i[1])
        self._olddata = 0
