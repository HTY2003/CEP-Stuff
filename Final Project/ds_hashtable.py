import sys
import math
import ctypes
from ds_dyarray import DyArray

if sys.version_info[0] == 3: _get_byte = lambda c: c
else: _get_byte = ord
PyArrayType = lambda x: ctypes.py_object * x
array = lambda x: PyArrayType(x)(*[(None,None)]*x)

class HashTable:
    __slots__ = ('size', 'taken', 'data')
    def __init__(self, size=64, autocal=False):
        if autocal:
            self.size = 2
            while size > self.size: self.size *= 2
        else: self.size = size
        assert math.log2(self.size).is_integer(), 'Hash table size must be a power of 2'
        self.taken, self.data = 0, array(self.size)

    def __iter__(self):
        def generate():
            for i in self.data:
                if i[0] is not None: yield i
        return iter(generate())

    def __str__(self):
        string = ''
        for i in self.data:
            if i[0] is not None: string += str(i[0]) + ': ' + str(i[1]) + ' , '
        return '{' + string[:-3] + '}'

    __repr__ = __str__
    def __len__(self): return self.size
    def keys(self): return list(i[0] for i in self.data if i[0] is not None)
    def values(self): return list(i[1] for i in self.data if i[0] is not None)

    def __contains__(self, key):
        return True if self._search(key) else False

    def __setitem__(self,key,value):
        self._checkrehash()
        self._quadprobe(key,value)
        self.taken += 1

    def  __getitem__(self,key):
        result = self._search(key)
        if result: return result[1]
        else: raise KeyError(str(key))

    def __delitem__(self,key):
        foundindex = self._search(key)
        if foundindex: self.data[foundindex[0]], self.taken = (None, None), self.taken - 1
        else: raise KeyError(str(key))
        self._checkrehash()
        return foundindex[1]

    def _rehash(self,size):
        self.taken, self.data, olddata = 0, array(self.size), self.data
        for i in olddata:
            if i[0] is not None: self.add(i[0], i[1])

    def _checkrehash(self,max=80,min=0,multiplier=2,divisor=2):
        if self.taken >= (self.size * max / 100): self._rehash(int(self.size * multiplier))
        elif self.taken <= (self.size * min / 100): self._rehash(int(self.size / divisor))

    def _fnv1(self, data):
        if data == 0: data = '0'
        if isinstance(data, int): data = bytes(data)
        else: data = bytes(data, 'utf-8')
        hval = 0x811c9dc5
        for byte in data: hval = ((hval * 0x01000193) % (2**32)) ^ _get_byte(byte)
        return hval % self.size

    def _quadprobe(self,key,value):
        baseindex = testindex = self._fnv1(key)
        for i in range(1, self.size+1):
            if self.data[testindex][0] == key or self.data[testindex][0] is None:
                self.data[testindex] = (key, value)
                return
            else: testindex = (int(baseindex + (i**2+i)/2)) % self.size

    def _search(self,key):
        baseindex = testindex = self._fnv1(key)
        for i in range(1, self.size+1):
            if self.data[testindex][0] == key: return testindex, self.data[testindex][1]
            elif self.data[testindex][0] is not None: testindex = (int(baseindex + (i**2+i)/2)) % self.size
