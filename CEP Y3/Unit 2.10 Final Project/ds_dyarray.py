#Dynamic Array ADT
import ctypes
PyArrayType = lambda x: ctypes.py_object * x
array = lambda x: PyArrayType(x)(*[None]*x)

class DyArray:
    '''
    Dynamic Array ADT for CEP Final Project
    ----------------------------------------
    This is my final version of dynamically resizing ctypes array, which has some changes from the original.

    Firstly, the user can choose not to resize the array by setting the 'capacity' setting to be the same as size.
    This gives this class functionality to be as space-efficient as a tuple if needed (as long as the specified size is not exceeded).

    Secondly, the array only resize (doubles in size) when it is full.
    This is to allow the above feature and to be as space-efficient as possible, especially in a tree-heavy project like this one.

    Finally, slicing is finally possible with __getitem__. Huzzah!

    As for where this data structure is used, it is the base of the hashtable which powers the set, the AVL and Splay trees,
    and served as lists in front-end and the Contact Book class. So it's used in everything.
    '''

    __slots__ = ("size", "capacity", "elements")

    #---BUILT-IN FUNCTIONS---
    def __init__(self, size=1, capacity=None, iterator=[]):
        '''
        Initializes array with the size of capacity (size*2 if not given), or the size of the given iterator
        If iterator is given, all elements from iterator will transferred to the array to create a DyArray equivalent
        '''
        if capacity is not None: assert capacity >= size, 'Capacity must be more than or equal to size'
        if not iterator:
            if size > 0: self.size, self.capacity = size, size * 2
            else: self.size, self.capacity = 0, 1
            if capacity:
                if capacity >= self.size: self.capacity=capacity
            self.elements = array(self.capacity)
        else:
            self.size, self.capacity = len(iterator), len(iterator)
            self.elements = PyArrayType(self.size)(*list(iterator))

    def __str__ (self):
        '''
        Returns a string of the array
        Time complexity: O(1)

        E.g:
        >> a = DyArray(4)
        >> print(a)
        [None, None, None, None]
        '''
        return str(self.elements[:self.size])

    def __len__(self):
        '''
        Returns the length of the array
        Time complexity: O(1)

        E.g:
        >> a = DyArray(4)
        >> print(len(a))
        4
        '''
        return self.size

    def  __iter__ (self):
        '''
        Iterates through each value in the array
        Time complexity: O(n)

        E.g:
        >> a = DyArray(4)
        >> for i in a:
        >>     print(i)
        None
        None
        None
        None
        '''
        return iter(self.elements[:self.size])

    def __setitem__(self, index, value):
        '''
        Set the given index of the array to the given value
        Time complexity: O(1)

        E.g:
        >> a = DyArray(4)
        >> print(a)
        [None, None, None, None]
        >> a[0] = 1
        >> print(a)
        [1, None, None, None]
        '''
        if isinstance(index, int):
            if 0 <= index < self.size: self.elements[index] = value
            else: raise IndexError("Invalid index")
        else: raise TypeError("Invalid argument type")

    def __getitem__(self,index):
        '''
        Returns the value or slice of the array
        Time complexity: O(1)
        E.g:
        >> a = DyArray(iterator=[1, 2, 3, 4])
        >> print(a)
        [1, 2, 3, 4]
        >> print(a[1], a[:-1])
        1, [1, 2, 3]
        '''
        if isinstance(index, slice): return self.elements[index.start:index.stop]
        elif isinstance(index, int):
            if 0 <= index < self.size: return self.elements[index]
            else: raise IndexError("Invalid index")
        else: raise TypeError("Invalid argument type")

    def __delitem__(self, index):
        '''Same as self.remove(index)'''
        return self.remove(index)

    __repr__ = __str__

    #---ARRAY FUNCTIONS---
    def append(self, value):
        '''
        Appends given value to the end of the array
        Time complexity: O(1)

        E.g:
        >> a = DyArray(2)
        >> print(a)
        [None, None]
        >> a.append(1)
        >> print(a)
        [None, None, 1]
        '''
        if self.size >= self.capacity: self.resize()
        self.elements[self.size], self.size = value, self.size + 1

    def insert(self, index, value):
        '''
        Inserts value into the array based on the given index
        Time complexity (Average): O(log n)
        Time complexity (Worst case): O(n)

        E.g:
        >> a = DyArray(2)
        >> print(a)
        [None, None]
        >> a.insert(1, 1)
        >> print(a)
        [None, 1, None]
        '''
        if index < 0: index += self.size
        if index > self.size: raise IndexError("Invalid index")
        if self.size >= self.capacity: self.resize()
        for i in range(self.size, -1, -1):
            if i >= index: self.elements[i] = self.elements[i-1]
        self.elements[index], self.size = value, self.size + 1

    def pop(self):
        '''
        Returns and removes the last value in the array
        Time complexity: O(1)

        E.g:
        >> a = DyArray(2)
        >> print(a)
        [None, None]
        >> a.append(1)
        >> print(a)
        [None, None, 1]
        >> print(a.pop())
        1
        >> print(a)
        [None, None]
        '''
        tmp = self.elements[self.size]
        self.size -= 1
        return tmp

    def remove(self, index=-1):
        '''
        Returns and removes the value of the given index from the array
        Time complexity (Average): O(log n)
        Time complexity (Worst case): O(n)

        E.g:
        >> a = DyArray(2)
        >> print(a)
        [None, None]
        >> a.insert(1, 1)
        >> print(a)
        [None, 1, None]
        >> print(a.remove(1))
        1
        '''
        if index < 0: index += self.size
        if index > self.size: raise IndexError("Invalid index")
        tmp = self.elements[index]
        for i in range(self.size):
            if i > index: self.elements[i-1] = self.elements[i]
        self.size -= 1
        return tmp

    def resize(self):
        '''
        Doubles the existing capacity of the array
        Time complexity: O(n)

        E.g:
        >> a = DyArray(2)
        >> print(a)
        [None, None]
        >> a.resize()
        >> print(a)
        [None, None, None, None]
        '''
        newElements = array(self.capacity * 2)
        ctypes.memmove(newElements, self.elements, ctypes.sizeof(self.elements))
        self.capacity, self.elements = self.capacity * 2, newElements

    def merge(self, arrayB):
        '''
        Merge another array into the existing array
        Time complexity: O(n)

        E.g:
        >> a = DyArray(2)
        >> b = DyArray(5)
        >> b[0] = 0
        >> print(a, b)
        [None, None] [0, None, None, None, None]
        >> a.merge(b)
        >> print(a)
        [None, None, 0, None, None, None, None]
        '''
        length = self.size
        while (arrayB.size + self.size) >= self.capacity: self.resize()
        self.size += arrayB.size
        for i in range(len(arrayB)): self.elements[length + i] = arrayB[i]
