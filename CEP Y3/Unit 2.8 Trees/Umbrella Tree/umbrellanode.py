class Node:
    __slots__ = ('key', 'val', 'left', 'right')
    def __init__(self, key, value):
        self.key,self.val = key,value
        self.left = self.right = None
    def __str__(self): return str((self.key, self.val))
    __repr__ = __str__
