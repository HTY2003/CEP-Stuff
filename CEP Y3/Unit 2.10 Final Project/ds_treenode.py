class Node:
    '''
    Node used in normal BST and Splay Tree
    Attributes: key, value, left child, right child
    '''
    __slots__=('key', 'val', 'left', 'right')
    def __init__(self, key, value): self.key, self.val, self.left, self.right = key, value, None, None
    def __str__(self): return str((self.key, self.val))
    __repr__=__str__

class AVLNode:
    ''' Node used in AVL, like the normal node but with an added attribute: height '''
    __slots__= ('key', 'val', 'left', 'right', 'height')
    def __init__(self, key, value, height=1): self.key, self.val, self.left, self.right, self.height = key, value, None, None, 1
    def __str__(self): return str((self.key, self.val))
    __repr__=__str__
