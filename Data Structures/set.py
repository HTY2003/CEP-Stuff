from hashtable import HashTable
class Set:
    __slots__ = ("size", "lookup")
    def __init__(self, iterator=[]):
        self.lookup = HashTable()
        for i in iterator: self.lookup[i] = None
        self.size = self.lookup._taken

    def __str__(self):
        string = '{'
        for i in self.lookup:
            if i[0] != None: string += str(i[0]) + ", "
        return string [:-2] + '}'

    def __len__(self): return self.size
    def __iter__(self): return iter(self.lookup)
    def __contains__(self, key):
        try:
            if key in self.lookup: return True
        except KeyError: return False

    def __and__(self, setB): return self.union(setB)
    def __add__(self, key):
        self.add(key)
        return self

    def add(self, key): self.lookup[key] = None
    def delete(self, key): del self.lookup[key]
    def equal(self, setB):
        for i in self.lookup:
            if i != (None, None): if

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

    def difference(self, setB):
        newset = Set()
        for i in self.lookup:
            if i != (None, None):
                if i[0] not in setB: newset.lookup[i[0]] = None
        return newset
