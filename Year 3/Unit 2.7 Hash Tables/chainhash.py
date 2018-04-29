import sys
import math
import ctypes
from collections import deque

if sys.version_info[0] == 3:
    _get_byte = lambda c: c
else:
    _get_byte = ord

class CHashTable:
    """
    Hash table that uses chained lists to handle collsions between items added,
    allowing for multiple elements to be contained within one index.
    It also uses the __fnv1 hash, designed for speed and randomness to prevent
    clustering and too many collisions.
    """

    def __init__(self,size):
        """
        Initializes hash table array to the size specified. Prime numbers recommended.

        Example usage:
        >>> a = CHashTable(37)                                                    """

        self._size = size
        self._taken = 0
        PyArrayType  =  ctypes.py_object * self._size
        self._data = PyArrayType(*([None] * self._size))

    def __len__(self):
        """
        Returns current length of hash table array

        Time complexity: O(1)

        Example usage:
        >>> a = CHashTable(37)
        >>> print(len(a))
        37                                     """

        return self._size

    def __str__(self):
        """
        Returns string of a hash table array, containing each array index and the array element it contains

        Time complexity: O(n)

        Example usage:
        >>> a = CHashTable(4)
        >>> a.add("Tom")
        >>> a.add("Jerry")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Tom    Jerry                                                                                """

        string = ""
        substring = ""
        for index in range(self._size):
            if self._data[index] is not None:
                for subitem in self._data[index]:
                    if subitem == self._data[index][0]:
                        substring += (" " * (6-len(str(index)))) + str(subitem)
                    else:
                        substring += "      " + str(subitem)
                string += str(index) + substring + "\n"
                substring = ""
            else:
                string += str(index) + "    " + str(None) + "\n\n"
        return string

    __repr__ = __str__

    def __iter__(self):
        """
        Loops through the elements of the hash table array

        Time complexity: O(n)

        Example usage:
        >>> a = CHashTable(4)
        >>> a.add("Tom")
        >>> a.add("Jerry")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Tom    Jerry
        >>> for i in a:
        >>>     print(i)
        None
        None
        None
        Tom
        Jerry                                            """
        iterlist = deque()
        for item in self._data:
            if item is None:
                iterlist.append(None)
            else:
                for subitem in item:
                    iterlist.append(subitem)
        return iter(iterlist)


    def __setitem__(self,key):
        "Same as self.add(element): " + self.add.__doc__
        return self.add(key)

    def __getitem__(self,key):
        "Same as self.get(element): " + self.get.__doc__
        return self.get(key)

    def __delitem__(self,key):
        "Same as self.remove(element): " + self.remove.__doc__
        return self.remove(key)

    def __fnv1(self,data):
        """
        Function(hidden) that converts integers and strings into bytes
        before hashing them into index values using the __fnv1 algorithm,
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

    def __chain(self,index,element):
        """
        Function(hidden) that adds element to the list in the index of the array.
        Since the collections.deque object has O(1) append time, this action is pretty fast.
        """
        if self._data[index] is None:
            self._taken += 1
            self._data[index] = deque()
        self._data[index].append(element)

    def __search(self,index,element):
        """
        Function(hidden) that attempts to find the index of the chain in which the element
        is stored in before returning it. If the element is not found, None is returned.
        """
        if self._data[index] is not None:
            if len(self._data[index]) != 0:
                for i in range(len(self._data[index])):
                    if self._data[index][i] is element:
                        return i
            else: return None
        else: return None

    def used(self):
        """
        Function that returns the number of non-empty indexes in the array
        This can be used if the user wants to see how full or empty the array is,
        and use the self.rehash() function to resize the array accordingly.
        This does NOT refer to the number of elements in the array, just the
        number of chains in the array which the elements are stored in.

        Time complexity: O(1)

        E.g:
        >>> a = CHashTable(1)
        >>> a.add("Tom")
        >>> a.add(1)
        >>> a.add("Hello Mars")
        >>> print a.used()
        1                                                                    """
        return self._taken

    def checkrehash(self,max=80,min=20,multiplier=2,divisor=2):
        """
        Function a user can use to resize the array based on how full it is
        If the array exceeds <max> % capacity(80% by default) in use, the array will
        multiply itself by the multiplier (2 by default). If the array goes under <min>%
        capacity(20% by default), the array will divide itself by the divisor (2 by default).
        This allows users to trim or expand their arrays without interfering with their
        liberty to resize at will.

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
        Function that resizes the hash table array to the specified size, allowing it to store
        more elements, done by creating a new array of the new size, and re-assigning each
        non-empty value in the array to the new array based on the new size.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = CHashTable(10)
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
        #If element is part of a chain, it is added to the new array
        for item in self._olddata:
            if item is not None:
                for subitem in item:
                    self.add(subitem)

    def add(self,element):
        """
        Function that assigns element to the hash table array using the
        __fnv1-hashed version of the element as the array index

        Time complexity: O(1)

        Example usage:
        >>> a = CHashTable(4)
        >>> a.add("Tom")
        >>> a.add("Jerry")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Tom     Jerry                                         """

        #Hashes the element into the index
        index = self.__fnv1(element)
        #Chains element to the list in that index
        #The collection.deque allows appending to be O(1), hence the fast speed
        self.__chain(index, element)

    def get(self,element):
        """
        Function that retrieves and returns the tuple of indexes which the given element can be accessed through
        If the element is not in the hash table, it returns None.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = CHashTable(4)
        >>> a.add("Tom")
        >>> print(a.get("Tom"))
        (3, 0)                                                                                              """

        #Hashes the element into the index
        index = self.__fnv1(element)
        #Returns None if element is not found
        if self.__search(index, element) is None:
            return None
        #Returns tuple of indexes otherwise
        return index, self.__search(index, element)

    def remove(self,element):
        """
        Function that retrieves and returns the indexes which the given element in stored in,
        then makes the index slot empty, removing the element from the hash table.
        If the element is not in the hash table, it returns None.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = CHashTable(4)
        >>> a.add("Tom")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Tom
        >>> a.remove("Tom")
        >>> print(a)
        0   None
        1   None
        2   None
        3


        Note: Empty spaces also signify empty slots                                     """

        index = self.__fnv1(element)
        try:
            self._data[index].remove(element)
            if len(self._data[index]) == 0:
                self._taken -= 1
            return index
        except ValueError:
            return None
