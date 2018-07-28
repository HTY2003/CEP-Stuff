class Node:
    '''Binary node that contains a key, a value, and left and right pointers to future children'''
    #allocate static amount of memory to variables instead of a dynamic dictionary
    #this can reduce up to 40% of RAM
    __slots__ = ('key', 'val', 'left', 'right')
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        return str((self.key, self.val))

    def __getitem___(self, index):
        if index == 0: return self.key
        if index == 1: return self.val

    __repr__ = __str__
