# Implementation of the Queue ADT using a linked list.
class LLQueue :
    def __init__( self ):
        self._qhead = None
        self._qtail = None
        self._count = 0
    def isEmpty( self ):
        return self._qhead is None
    def __len__( self ):
        return self._count
    def enqueue( self, item ):
        node = self._QueueNode( item )
        if self.isEmpty() :
            self._qhead = node
        else :
            self._qtail.next = node
        self._qtail = node
        self._count += 1
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self._qhead
        if self._qhead is self._qtail :
            self._qtail = None

        self._qhead = self._qhead.next
        self._count -= 1
        return node.item

    # ...
    # Private storage class for creating the linked list nodes.
    class _QueueNode:
        def __init__( self, item ):
            self.item = item
            self.next = None
    
if __name__ == "__main__":
    lq = LLQueue()
    
    for i in range(5):
        lq.enqueue(i)

    while not lq.isEmpty():
        print(lq.dequeue())
