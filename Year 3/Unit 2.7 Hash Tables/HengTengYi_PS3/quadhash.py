import sys
import math
import ctypes

if sys.version_info[0] == 3:
    _get_byte = lambda c: c
else:
    _get_byte = ord

class QHashTable:
    """
    Hash table(size is a power of 2) that uses the FNV1 hash to assign elements to the table's array and a quadratic probe of (i*i+i)/2

    The FNV1 algorithm was designed for computing speed and randomness for less collisions to save time.
    In addition, the quadratic probe can check every index in the array (being a power of 2), ensuring
    every index in the array is taken up before the array re-sizes and rehashes everything, saving both
    valuable space and memory.
    """

    def __init__(self, size=64, autocal=False):
        """
        Initializes the hash table array of size given (64 by default)

        The size of the array must be 64 by default, or any other power of 2 specified.
        Unless autocal is enabled, the program will assert the size being a power of 2.
        If it is enabled, the program will upsize any non-power of 2 to the next highest
        power of 2 such that the table will not resize, saving valuable time.

        Example usage:
        >>> a = QHashTable()
        >>> print(len(a))
        64
        >>> b = QHashTable(5, autocal = True)
        >>> print(len(b))
        8
        >>> c = QHashTable(16)
        >>> print(len(c))
        16                                                                          """

        if autocal:
            self._size = 2
            while size > self._size:
                self._size *= 2
        else:
            assert math.log2(size).is_integer(), "Hash table size must be a power of 2"
            self._size = size
        self._taken = 0
        PyArrayType  =  ctypes.py_object * self._size
        self._data = PyArrayType(*([None] * self._size))

    def __len__(self):
        """
        Returns current length of hash table array

        Time complexity: O(1)

        Example usage:
        >>> a = QHashTable(64)
        >>> print(len(a))
        64                                    """
        return self._size

    def __str__(self):
        """
        Returns string of a hash table array, containing each array index and the array element it contains

        Time complexity: O(n)

        Example usage:
        >>> a = QHashTable(4)
        >>> print(a)
        0   None
        1   None
        2   None
        3   None                                                                                       """

        string = ""
        for i in range(self._size):
            string += str(i) + "    " + str(self._data[i]) + "\n"
        return string

    __repr__ = __str__

    def __iter__(self):
        """
        Loops through the elements of the hash table array

        Time complexity: O(n)

        Example usage:
        >>> a = QHashTable(4)
        >>> a.add("Tom")
        >>> for i in a:
        >>>     print(i)
        None
        None
        None
        Tom                                          """
        return iter(self._data)

    def __setitem__(self, element):
        "Same as self.add(): " + self._add.__doc__
        self.add(element)

    def __getitem__(self, element):
        "Same as self.get(element): " + self.get.__doc__
        return self.get(element)

    def __delitem__(self, element):
        "Same as self.remove(element): " + self.remove.__doc__
        return self.remove(element)

    def __fnv1(self, data):
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
            data = bytes(data, "utf-8")
        #Hashes bytes through the FNV1 algorithm into a 32-bit value
        hval = 0x811c9dc5
        for byte in data:
            hval = (hval * 0x01000193) % (2**32)
            hval = hval ^ _get_byte(byte)
        #Returns modulus of hashed value by the size of the hash table
        return hval % self._size

    def __quadprobe(self, index, element):
        """
        Function(hidden) that attempts to assigns elements to the given index.
        Should the index already be filled, a quadratic probe of (i*i+1)/2 will be
        applied to the original index until the element is assigned.

        With this probe, along with the hash table being a power of two, every index
        in the hash table array will be visited, ensuring there is no unused space
        in the array before it is resized and rehashed, eliminating wasted memory.
        """

        baseindex = index
        testindex = index
        #Tries to assign element to every index, looping through the entire array
        for i in range(1, self._size+1):
            #Assign element if that slot is empty
            if self._data[testindex] is None or self._data[testindex] is "":
                self._data[testindex] = element
                return
            else:
                #Applies probe and tries again if it fails
                testindex = int(baseindex + (i**2+i)/2)
                testindex %= self._size

    def __search(self,index,element):
        """
        Function(hidden) that goes through the same quadratic probe in self._quadprobe
        to look for which index the element was in before returning the found index.
        """

        baseindex = index
        testindex = index
        for i in range(1, self._size+1):
            #Checks if data in array's index corresponds to the element
            if self._data[testindex] is element:
                return testindex
            elif self._data[testindex] is None:
                return None
            else:
                #Applies the probe and tries again if it fails
                testindex = int(baseindex + (i**2+i)/2)
                testindex %= self._size
        return None

    def used(self):
        """
        Function that returns the number of non-empty indexes in the array
        This can be used if the user wants to see how full or empty the array is,
        and use the self.rehash() function to resize the array accordingly.

        Time complexity: O(1)

        E.g:
        >>> a = QHashTable(4)
        >>> a.add("Tom")
        >>> a.add(1)
        >>> a.add("Hello Mars")
        >>> print a.used()
        3                                                                   """
        return self._taken

    def checkrehash(self,max=80,min=20,multiplier=2,divisor=2):
        """Function a user can use to resize the array based on how full it is
        If the array exceeds <max> % capacity(80% by default) in use, the array will
        multiply itself by the multiplier (2 by default). If the array goes under <min>%
        capacity(20% by default), the array will divide itself by the divisor (2 by default).
        This allows users to trim or expand their arrays without interfering with their
        liberty to resize at will.

        Time complexity(average): O(n)
        Time complexity(worst-case): O(n^2)

        E.g:
        >>> A = QHashTable(5)
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
        Function that resizes the hash table array to the specified size, allowing it
        to store more elements, done by creating a new array of the new size, and
        re-assigning each non-empty value in the array to the new array based on the new size.

        The specified size must be able to fit all elements, and must be a power of 2.
        If autocal is enabled, the function will automatically upscale any non-power of 2
        to the next nearest power of 2.

        Time complexity(average): O(n)
        Time complexity(worst-case): O(n^2)

        Example usage:
        >>> a = QHashTable()
        >>> print(len(a))
        64
        >>> a.resize(128)
        >>> print(len(a))
        128                                                                              """

        if autocal:
            self._size = 2
            while size > self._size:
                self._size *= 2
        else:
            assert math.log2(size).is_integer(), "Hash table size must be a power of 2"
            assert self._taken <= size, "Existing elements cannot fit within array of size specified"
            self._size = size

        self._taken = 0
        self._olddata = self._data
        #Makes new array twice the original size
        PyArrayType  =  ctypes.py_object * self._size
        self._data = PyArrayType(*([None] * self._size))
        #Assigns each value in the old array one-by-one to the new array
        for i in self._olddata:
            if i is not None and i is not "":
                self.add(i)
        self._olddata = 0

    def add(self,element):
        """
        Function that assigns element to the hash table array using the
        FNV1-hashed version of the element as the array index

        Also upsizes array if the table is completely full

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n^2)

        Example usage:
        >>> a = QHashTable(4)
        >>> a.add("Tom")
        >>> print(a)
        0   None
        1   None
        2   None
        3   Tom                                                     """

        #Resizes array when table is full
        if self._taken + 1 == self._size:
            self.rehash(self._size*2)
        #Derives array index from hashed element using the self.__fnv1 function
        index = self.__fnv1(element)
        #Attempts to assign element to the index, and applies quadratic probe if needed using the self.__quadprobe function
        self.__quadprobe(index,element)
        self._taken += 1

    def get(self,element):
        """
        Function that retrieves and returns the index which the given element is stored in
        If the element is not in the hash table, it returns None.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = QHashTable(4)
        >>> a.add("Tom")
        >>> print(a.get("Tom"))
        3                                                                             """

        #Derives array index from hashed element using the self.__fnv1 function
        index = self.__fnv1(element)
        #Searches for the element's index using the self._search function and returns it
        return self.__search(index,element)

    def remove(self,element):
        """
        Function that retrieves and returns the index which the given element in stored in,
        then makes the index slot empty, removing the element from the hash table.
        If the element is not in the hash table, it returns None.

        Time complexity(average): O(log n)
        Time complexity(worst-case): O(n)

        Example usage:
        >>> a = QHashTable(4)
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

        Note: Empty spaces also signify empty slots.                         """

        #Finds index using self._get function
        foundindex = self.get(element)
        #Sets value in found index to "", our special flag that allows the search probe to continue in the future
        if foundindex is not None:
            self._data[foundindex] = ""
            self._taken -= 1
        #Returns index, like in self.get()
        return foundindex
