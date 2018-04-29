from carray import Array

class CQueue :
    def __init__( self, maxSize ) :
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = Array( maxSize )
    def isEmpty( self ) :
        return self._count == 0

    # A new operation specifically for the circular array.
    def isFull( self ) :
        return self._count == len(self._qArray)

    def __len__( self ) :
        return self._count

    def enqueue( self, item ):
        assert not self.isFull(), "Cannot enqueue to a full queue."
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1
        
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        item = self._qArray[ self._front ]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item


if __name__ == "__main__":
    cq = CQueue(5)
    
    for i in range(5):
        cq.enqueue(i)

    while not cq.isEmpty():
        print(cq.dequeue())
