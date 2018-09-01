#Dynamic Array ADT
import ctypes
PyArrayType = lambda x: ctypes.py_object * x
array = lambda x: PyArrayType(x)(*[None]*x)

class DyArray:
    __slots__ = ("size", "capacity", "elements")
    def __init__(self, size):
        if size > 0: self.size, self.capacity = size, size * 2
        else: self.size, self.capacity = 0, 1
        self.elements = array(self.capacity)

    def __setitem__(self, index, value):
        if isinstance(index, int):
            if 0 <= index < self.size: self.elements[index] = value
            else: raise IndexError("Invalid index")
        else: raise TypeError("Invalid argument type")

    def __getitem__(self,index):
        if isinstance(index, slice): return self.elements[index.start:index.stop]
        elif isinstance(index, int):
            if 0 <= index < self.size: return self.elements[index]
            else: raise IndexError("Invalid index")
        else: raise TypeError("Invalid argument type")

    def __delitem__(self, index): return self.remove(index)
    def __len__(self): return self.size
    def  __iter__ (self): return iter(self.elements[:self.size])
    def __str__ (self): return str(self.elements[:self.size])
    __repr__ = __str__

    def resize(self):
        newElements = array(self.capacity * 2)
        ctypes.memmove(newElements, self.elements, ctypes.sizeof(self.elements))
        self.capacity, self.elements = self.capacity * 2, newElements

    def append(self, value):
        if self.size >= self.capacity: self.resize()
        self.elements[self.size], self.size = value, self.size + 1

    def insert(self, index, value):
        if index < 0: index += self.size
        if index > self.size: raise IndexError("Invalid index")
        if self.size >= self.capacity: self.resize()
        for i in range(self.size, -1, -1):
            if i >= index: self.elements[i] = self.elements[i-1]
        self.elements[index], self.size = value, self.size + 1

    def pop(self):
        tmp = self.elements[self.size]
        self.size -= 1
        return tmp

    def remove(self, index=-1):
        if index < 0: index += self.size
        if index > self.size: raise IndexError("Invalid index")
        tmp = self.elements[index]
        for i in range(self.size):
            if i > index: self.elements[i-1] = self.elements[i]
        self.size -= 1
        return tmp

    def merge(self, arrayB):
        length = self.size
        while (arrayB.size + self.size) >= self.capacity: self.resize()
        self.size += arrayB.size
        for i in range(len(arrayB)): self.elements[length + i] = arrayB[i]
