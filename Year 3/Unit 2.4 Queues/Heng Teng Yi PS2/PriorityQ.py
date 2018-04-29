#Dynamic Array ADT
import ctypes
class PriorityQueue:
    """An unbounded priority queue that stores priorities in a binary heap in the form of a ctypes
array, and appends their corresponding item to other ctypes arrays in a dictionary             """

    def __init__(self, alist = []):
        """Declares the priority queue by adding elements from a list (empty by default)
into their respective arrays, and heapsorts the priorities                           """

        assert type(alist) is list, "Input provided must be list"
        self._qList = _Array(len(alist) + 1)
        self._size = len(alist)
        self._nameDict = {}

        for i in range(self._size):
            self._qList[i + 1] = alist[i][1]
            try:
                self._nameDict[alist[i][1]].append(alist[i][0])
            except KeyError:
                self._nameDict[alist[i][1]] = _Array(1)
                self._nameDict[alist[i][1]][0] = alist[i][0]

        self._build(alist)

    def __str__(self):
        """Returns a string of a list of all the priorities within the binary heap

Time complexity: O(1)

E.g:
>>> a = PriorityQueue([(0,1),(0,2)])
>>> print(a)
[1,2]                                                                          """

        return str(self._qList._elements[1:self._size + 1])

    def __len__(self):
        """Returns the length of the priority queue

Time complexity: O(1)

E.g:
>>> a = PriorityQueue([(0,1),(0,2)])
>>> print(len(a))
2                                               """

        return self._size

    def _swapUp(self,index):
        """Sorts the binary heap by swapping the element in given index p with p // 2
if the element in index p// 2 is higher in value, before repeating the function if needed"""

        nextindex = index // 2
        if nextindex > 0:
          if self._qList[index] < self._qList[nextindex]:
             tmp = self._qList[nextindex]
             self._qList[nextindex] = self._qList[index]
             self._qList[index] = tmp
             self._swapUp(nextindex)

    def _swapDown(self,index):
        """Sorts the binary heap by swapping the element in given index p with 2p or 2p + 1,
if the element in index 2p or 2p + 1 is lower in value, before repeating the function if needed"""

        nextindex = index * 2
        if nextindex <= self._size:
            if not (nextindex + 1 > self._size or self._qList[nextindex] < self._qList[nextindex+1]):
                nextindex += 1
            if self._qList[index] > self._qList[nextindex]:
                tmp = self._qList[index]
                self._qList[index] = self._qList[nextindex]
                self._qList[nextindex] = tmp
            self._swapDown(nextindex)

    def _build(self,alist):
        """Sorts the initialized binary heap using the _swapDown function"""

        index = len(alist) // 2
        while index > 0:
            self._swapDown(index)
            index -= 1

    def isEmpty(self):
        """Returns a boolean of whether the priority queue is empty

Time complexity: O(1)

E.g:
>>> a = PriorityQueue([(0,1),(0,2)])
>>> print(a.isEmpty())
True                                                            """

        return self._size == 0

    def push(self, element):
        """Pushes an element into the priority queue, adding the
priority and name each into the respective binary heap and dictionary,
and then sorts the binary heap using the _SwapUp function

Time complexity (Worst-case): O(n)
Time complexity (Average): O(log n)

E.g:
>>> a = PriorityQueue([(0,2),(0,3)])
>>> print(a)
[2,3]
>>> a.push((0,1))
>>> print(a)
[1,2,3]                                                          """

        try:
            self._nameDict[element[1]].append(element[0])
        except KeyError:
            self._nameDict[element[1]] = _Array(1)
            self._nameDict[element[1]][0] = element[0]

        self._qList.append(element[1])
        self._size += 1
        self._swapUp(self._size)

    def peek(self):
        """Returns the name and priority of the item with the earliest enqueue and highest priority

Time complexity: O(1)

E.g:
>>> a = PriorityQueue([(0,2),(0,3)])
>>> print(a.peek())
(0,2)                                                                                 """

        return (self._qList[1], self._nameDict[priority])

    def pop(self):
        """Removes and returns the the name and priority of the item with the earliest enqueue and highest priority

Time complexity (Worst-case): O(n)
Time complexity (Average): O(log n)

E.g:
>>> a = PriorityQueue([(0,2),(0,3)])
>>> print(a.pop(), a)
(0,2) [(0,3)]                                                                                                   """
        tmp = self._qList[1]
        self._qList[1] = self._qList[self._size]
        self._qList[self._size] = tmp
        priority = self._qList.pop()
        self._size -= 1
        self._swapDown(1)
        return (priority, self._nameDict[priority].pop(0))

class _Array:
    def __init__(self, size):
        assert size > 0 , "Array size must be > 0"
        self._size = size
        self._capacity = size * 2
        PyArrayType  =  ctypes.py_object * (self._capacity)
        self._elements = PyArrayType(*([0] * self._capacity))

    # Return the length of the sub-array
    def __len__(self):
        return self._size

    # Gets the value of the index element
    def __getitem__(self,index):
        assert 0 <= index < self._size, "Array subscript out of range"
        return self._elements[index]

    #Sets a value in the index element
    def __setitem__(self, index, value):
        assert 0 <= index < self._size, "Array subscript out of range"
        self._elements[index] = value

    def  __iter__ (self):
        return iter(self._elements[:self._size])

    #Returns a string of the array
    def __str__ (self):
        return str(self._elements[:self._size])

    __repr__ = __str__

    def resize(self, size):
        assert size >= self._size , "Size must be at least " + str(self._size)

        newElements = (ctypes.py_object * (size * 2))(*([0] * size * 2))
        ctypes.memmove(newElements, self._elements, ctypes.sizeof(self._elements))
        self._elements = newElements
        self._size = size
        self._capacity = size * 2

    def append(self, value):
        if self._capacity - self._size <= 1:
            self.resize(self._size)
        self._elements[self._size] = value
        self._size += 1

    def pop(self, index = -1):
        if index < 0:
            index += self._size
        tmp = self._elements[index]
        for i in range(self._size):
            if i > index:
                self._elements[i-1] = self._elements[i]
        self._size -= 1
        return tmp
