#Dynamic Array ADT
import ctypes

class Array:
    def __init__(self, size):
        assert size > 0 , "Array size must be > 0"
        self._size = size
        self._capacity = size * 2
        PyArrayType  =  ctypes.py_object * (size * 2)
        self._elements = PyArrayType(*([None] * self._capacity))

    # Return the length of the sub-array
    def __len__(self):
        return self._size

    # Gets the value of the index element
    def __getitem__(self,index):
        assert 0 <= index < self._size, "Array subscript out of range"
        return self._elements[index]

    #Sets a value in the index element
    def __setitem__(self, index, value):
        assert index >= 0 and index < self._size, "Array subscript out of range"
        self._elements[index] = value

    #Returns an array iterator for traversing the elements
    def  __iter__ (self):
        return iter(self._elements[:self._size])

    #Returns a list of the array
    def __str__ (self):
        return str(self._elements[:self._size])

    __repr__ = __str__

    #Clear the array by setting each element to the given value
    def clear(self,value):
        for i in range(self._capacity):
            self._elements[i] = value

    '''DYNAMIC ARRAY FUNCTIONS (resize, append, insert, pop, remove, and combine)
    Based mostly off the Python List implementation in slides'''

    '''resize(size): Creates a new array with the same elements but different size,
    such that it has x spaces for elements and x additional spaces'''
    def resize(self, size):
        assert size >= self._size , "Size must be at least " + str(self._size)

        newElements = (ctypes.py_object * (size * 2))(*([None] * size * 2))
        ctypes.memmove(newElements, self._elements, ctypes.sizeof(self._elements))
        self._elements = newElements
        self._size = size
        self._capacity = size * 2

    '''combine(arrayB): Adds all values from arrayB into array, expanding
    array to accomodate both arrays if capacity is full'''
    def combine(self, arrayB):
        length = self._size
        if arrayB._size >= (self._capacity - self._size):
            self.resize(self._size + arrayB._size)
        else:
            self._size += arrayB.size
        for i in range(len(arrayB)):
            self._elements[length + i] = arrayB[i]

    '''append(value): Adds element to the end of the array,
    and doubles array capacity if it is full'''
    def append(self, value):
        if self._capacity - self._size <= 1:
            self.resize(self._size)
        self._elements[self._size] = value
        self._size += 1

    '''insert(index, value):
    Insert value into element of index x,
    pushing all values following x forward,
    and doubles array capacity if it is full'''
    def insert(self, index, value):
        if index < 0:
            index += self._size
        assert index <= self._size, "Array subscript out of range"

        if self._capacity - self._size <= 1:
            self.resize(self._size)

        for i in range(0, self._size, -1):
            if i >= index:
                self._elements[i+1] = self._elements[i]
        self._elements[index] = value
        self._size += 1

    '''pop(index = -1): Removes and returns value of element of index n (-1 by default),
    and downsizes capacity if less than half the capacity is used'''
    def pop(self, index = -1):
        if index < 0:
            index += self._size
        assert 0 <= index < self._size, "Array subscript out of range"
        self._elements[self._size] = self._elements[index]

        if index == self._size - 1:
            self._elements[index] = None
            self._size -= 1
        else:
            for i in range(self._size):
                if i > index:
                    self._elements[i-1] = self._elements[i]
            self._size -= 1

        if self._size < self._capacity / 2:
            self.resize(self._size)
        return self._elements[self._size]

    '''remove(index): Removes value of element of index n, and downsizes
    capacity if less than half the capacity is used'''
    def remove(self, index):
        if index < 0:
            index += self._size
        assert 0 <= index < self._size, "Array subscript out of range"

        for i in range(self._size):
            if i > index:
                self._elements[i-1] = self._elements[i]
        self._size -= 1

        if self._size < self._capacity / 2:
            self.resize(self._size)

    '''
    Time complexity for all functions: O(n)
    Analysis: The extra capacity in the array makes appending and removing
    faster despite the extra storage used, since one only needs to set the
    index and increase the size (only resizing when needed).

    However, functions that add or remove specific indexes(pop, insert, remove)
    require moving the indexes individually, so they'll take longer depending
    on array size.

    The resize is also faster thanks to the ctypes.memmove function, which
    directly copies bytes from the old array to the new larger one, instead
    of looping through it and adding elements 1-by-1.
    '''

a = Array(9)
a[2] = 2
a[5] = 5
a.pop(2)
print(len(a), a)
a.append(100)
a.remove(0)
print(len(a), a)
b = Array(5)
b[4] = 69
b.combine(a)
print(len(b), b)
