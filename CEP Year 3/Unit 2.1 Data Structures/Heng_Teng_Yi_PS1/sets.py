import numpy as np

class Set(object):
    def __init__(self, lyst=[]):
        self.array = np.unique(np.array(lyst))

    def __str__(self):
        return "{" + str(self.array.tolist())[1:-1] + "}"

    def __iter__(self):
        return np.nditer(self.array)

    def __getitem__(self, i):
        return self.array.tolist()[i]

    def __and__(self,setB):
        lyst = np.intersect1d(self.array, setB.array, assume_unique=True).tolist()
        return Set(lyst)

    def __add__(self,setB):
        lyst = np.union1d(self.array, setB.array).tolist()
        return Set(lyst)

    def __len__(self):
        return self.array.size

    def __contains__(self,i):
        return i in self.array

    __repr__ = __str__

    def add(self, element):
        self.array = np.unique(np.append(self.array, element))

    def remove(self, element):
        if element in self.array:
            self.array = np.delete(self.array, np.where(self.array == element))
        else:
            raise ValueError("element not in array")

    def equals(self, setB):
        return np.array_equal(self.array, setB.array)

    def isSubsetOf(self, setB):
        return all(np.isin(self.array, setB.array, assume_unique=True))

    def properSubsetOf(self, setB):
        return self.isSubsetOf(setB) and not self.equals(setB)
