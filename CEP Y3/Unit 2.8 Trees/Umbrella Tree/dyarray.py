#Dynamic Array ADT
import ctypes

class DyArray:
    '''
Implementation of a dynamically resizable array using ctypes arrays

Includes the following dynamic array functions: append, insert, remove, pop, & merge'''

    def __init__(self, size):
        '''Declares a ctypes array of the given size filled with None

    Time complexity: O(n)

    E.g:
    >>> a = DyArray(5)
    >>> print(a._size, a._capacity, a._elements[:])
    5 10 [None, None, None, None, None]                      '''

        self._size = size
        self._capacity = size * 2
        PyArrayType  =  ctypes.py_object * (self._capacity)
        self._elements = PyArrayType(*([None] * self._capacity))

    def __len__(self):
        '''Returns the length of the sub-array

    Time complexity: O(1)

    E.g:
    >>> a = DyArray(5)
    >>> print(len(a))
    5                                 '''

        return self._size

    def __setitem__(self, index, value):
        '''Sets the given value as the value of the given index

    Time complexity: O(1)

    E.g:
    >>> a = DyArray(5)
    >>> a[4] = 1
    >>> print(a[4])
    1                                                  '''

        assert 0 <= index < self._size, "Array subscript out of range"
        self._elements[index] = value

    def __getitem__(self,index):
        '''Retrieves the value of the given index

    Time complexity: O(1)

    E.g:
    >>> a = DyArray(5)
    >>> print(a[4])
    None                                 '''

        assert 0 <= index < self._size, "Array subscript out of range"
        return self._elements[index]

    def  __iter__ (self):
        ''' Iterates through the sub-array to access all the elements

    Time complexity: O(1)

    E.g:
    >>> a = DyArray(5)
    >>> for i in a:
            print(i)
        None\nNone\nNone\nNone\nNone                             '''

        return iter(self._elements[:self._size])

    def __str__ (self):
        '''Returns a string of the sub-array

    Time complexity: O(1)

    E.g:
    >>> a = DyArray(5)
    >>> print(a)
    [None, None, None, None, None]   '''

        return str(self._elements[:self._size])

    __repr__ = __str__

    def resize(self, size):
        '''Replaces current array with larger array twice of
        the given size, but with the same elements

    Time complexity: O(n)

    E.g:
    >>> a = DyArray(5)
    >>> print(a)
    [None, None, None, None, None]
    >>> a.resize(7)
    [None, None, None, None, None, None, None]      '''

        assert size >= self._size , "Size must be at least " + str(self._size)

        newElements = (ctypes.py_object * (size * 2))(*([None] * size * 2))
        ctypes.memmove(newElements, self._elements, ctypes.sizeof(self._elements))
        self._elements = newElements
        self._size = size
        self._capacity = size * 2

    def append(self, value):
        '''Adds element to the end of the array,
        and resizes array if it is full

    Time complexity (Worst-Case): O(n)
    Time complexity (Average): O(1)

    E.g:
    >>> a = DyArray(5)
    >>> print(a)
    [None, None, None, None, None]
    >>> a.append(5)
    >>> print(a)
    [None, None, None, None, None, 5]  '''

        if self._capacity - self._size <= 1:
            self.resize(self._size)

        self._elements[self._size] = value
        self._size += 1

    def insert(self, index, value):
        '''Insert value into element of index x,
        pushing all proceeding values forward,
        and resizes array if it is full

    Time complexity: O(n)

    E.g:
    >>> a = DyArray(5)
    >>> print(a)
    [None, None, None, None, None]
    >>> a.insert(2, 5)
    >>> print(a)
    [None, None, 5, None, None, None]   '''

        if index < 0:
            index += self._size
        assert index <= self._size, "Array subscript out of range"

        if self._capacity - self._size <= 1:
            self.resize(self._size)

        for i in range(self._size, 0, -1):
            if i >= index:
                self._elements[i+1] = self._elements[i]

        self._elements[index] = value

        self._size += 1
    def pop(self, index = -1):
        '''Removes and returns value of element of given index
        (-1 by default), and resizes array if it is too big

    Time complexity: O(n)

    E.g:
    >>> a = DyArray(5)
    >>> a.append(5)
    >>> print(a.pop())
    5                                                  '''

        if index < 0:
            index += self._size
        tmp = self._elements[index]

        for i in range(self._size):
            if i > index:
                self._elements[i-1] = self._elements[i]
        self._size -= 1

        if (self._size * 2) <= self._capacity:
            self.resize(self._size)
        return tmp

    def remove(self, index):
        '''Removes value of element of given index
        (-1 by default), and resizes array if it is too big

    Time complexity: O(n)

    E.g:
    >>> a = DyArray(5)
    >>> a.append(5)
    >>> print(a)
    [None, None, None, None, None, 5]
    >>> a.remove(5)
    [None, None, None, None, None]                  '''

        if index < 0:
            index += self._size

        for i in range(self._size):
            if i > index:
                self._elements[i-1] = self._elements[i]
        self._size -= 1

        if (self._size * 2) <= self._capacity:
            self.resize(self._size)

    def merge(self, arrayB):
        '''Adds all values from another arrayB into an array,
        expanding array to accomodate both arrays if needed

    Time complexity: O(n)

    E.g:
    >>> a = DyArray(5)
    >>> a[4] = 1
    >>> b = DyArray(4)
    >>> a.merge(b)
    >>> print(a)
    >>> [None, None, None, None, 5, None, None, None, None]'''

        length = self._size
        if arrayB._size >= (self._capacity - self._size):
            self.resize(self._size + arrayB._size)
        else:
            self._size += arrayB.size
        for i in range(len(arrayB)):
            self._elements[length + i] = arrayB[i]
