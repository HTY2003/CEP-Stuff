from ds_hashtable import HashTable
from ds_dyarray import DyArray

class Set:
    __slots__ = ('size', 'lookup')
    def __init__(self, iterator=[]):
        self.lookup = HashTable(32)
        for i in iterator: self.lookup[i] = None
        self.size = self.lookup.taken

    def __str__(self):
        string = ''
        for i in self.lookup:
            if i[0] != None: string += str(i[0]) + ', '
        return '{' + string [:-2] + '}'

    __repr__ = __str__
    def __len__(self): return self.size
    def __iter__(self): return iter(self.lookup)
    def __contains__(self, key):
        try:
            return True if key in self.lookup else False
        except KeyError: return False

    def add(self, key):
        self.lookup[key] = None
        self.size = self.lookup.taken

    def delete(self, key): del self.lookup[key]

    def union(self, setB):
        newset = Set()
        if len(setB) >= self.size:
            newset.lookup = setB.lookup
            for i in self.lookup:
                if i != (None, None): newset.lookup[i[0]] = None
        else:
            newset.lookup = self.lookup
            for i in setB.lookup:
                if i != (None, None): newset.lookup[i[0]] = None
        return newset

    def intersect(self, setB):
        newset = Set()
        for i in self.lookup:
            if i != (None, None):
                if i[0] in setB: newset.lookup[i[0]] = None
        return newset

    def copy(self):
        newset=Set()
        newset.lookup = self.lookup
        return newset

    def tolist(self):
        def generate():
            for i in self.lookup:
                if i[0] != None: yield i[0]
        return list(generate())
