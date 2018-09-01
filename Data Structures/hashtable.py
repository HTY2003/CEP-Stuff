import sys
import math
import ctypes
from dyarray import DyArray

if sys.version_info[0] == 3: _get_byte = lambda c: c
else: _get_byte = ord
PyArrayType = lambda x: ctypes.py_object * x
array = lambda x: PyArrayType(x)(*[(None,None)]*x)

class HashTable:
    __slots__ = ("_size", "_taken", "_data")
    def __init__(self, size=512, autocal=False):
        if autocal:
            self._size = 2
            while size > self._size: self._size *= 2
        else: self._size = size
        assert math.log2(self._size).is_integer(), "Hash table size must be a power of 2"
        self._taken, self._data = 0, array(self._size)

    def __str__(self):
        string = "{"
        for i in self._data:
            if i[0] is not None: string += str(i[0]) + ': ' + str(i[1]) + " , "
        return string[:-3] + "}"

    __repr__ = __str__
    def __len__(self): return self._size
    def __iter__(self): return iter(self._data)
    def __sorted__(self):
        sortlist = []
        for i in self._data:
            if i[0]: sortlist.append(i)
        sortlist.sort()
        return sortlist

    def __contains__(self, key):
        return True if self.__search(key) else False

    def __setitem__(self,key,value):
        self.checkrehash()
        self.__quadprobe(key,value)
        self._taken += 1

    def  __getitem__(self,key):
        result = self.__search(key)
        if result: return result[1]
        else: raise KeyError(str(key))

    def __delitem__(self,key):
        foundindex = self.__search(key)
        if foundindex: self._data[foundindex[0]], self._taken = (None, None), self._taken - 1
        else: raise KeyError(str(key))
        self.checkrehash()
        return foundindex[1]

    def rehash(self,size):
        self._taken, self._data, olddata = 0, array(self._size), self._data
        for i in olddata:
            if i[0] is not None: self.add(i[0], i[1])

    def checkrehash(self,max=75,min=0,multiplier=2,divisor=2):
        if self._taken >= (self._size * max / 100): self.rehash(int(self._size * multiplier))
        elif self._taken <= (self._size * min / 100): self.rehash(int(self._size / divisor))

    def keys(self): return list(i[0] for i in self._data if i[0] is not None)
    def values(self): return list(i[1] for i in self._data if i[0] is not None)

    def __fnv1(self, data):
        if data == 0: data = "0"
        if isinstance(data, int): data = bytes(data)
        else: data = bytes(data, "utf-8")
        hval = 0x811c9dc5
        for byte in data: hval = ((hval * 0x01000193) % (2**32)) ^ _get_byte(byte)
        return hval % self._size

    def __quadprobe(self,key,value):
        baseindex = testindex = self.__fnv1(key)
        for i in range(1, self._size+1):
            if self._data[testindex][0] == key or self._data[testindex][0] is None:
                self._data[testindex] = (key, value)
                return
            else: testindex = (int(baseindex + (i**2+i)/2)) % self._size

    def __search(self,key):
        baseindex = testindex = self.__fnv1(key)
        for i in range(1, self._size+1):
            if self._data[testindex][0] == key: return testindex, self._data[testindex][1]
            elif self._data[testindex][0] is not None: testindex = (int(baseindex + (i**2+i)/2)) % self._size

if (7, None): print(1)
