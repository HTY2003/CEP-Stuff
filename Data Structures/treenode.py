class Node:
    __slots__=('key', 'val', 'left', 'right')
    def __init__(self, key, value): self.key, self.val, self.left, self.right = key, value, None, None
    def __str__(self): return str((self.key, self.val))
    __repr__=__str__

class AVLNode:
    __slots__=('key', 'val', 'left', 'right', 'height')
    def __init__(self, key, value): self.key, self.val, self.left, self.right, self.height = key, value, None, None, 1
    def __str__(self): return str((self.key, self.val))
    __repr__=__str__
