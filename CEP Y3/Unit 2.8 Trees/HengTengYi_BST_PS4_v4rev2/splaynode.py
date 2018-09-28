class Node:
    '''Binary node that contains a key, a value, and left and right pointers to future children'''
    #allocate static amount of memory to variables instead of a dynamic dictionary
    #this can reduce up to 40% of RAM
    __slots__ = ('key', 'val', 'left', 'right')

    def __init__(self, key, value):
        self.key,self.val = key,value
        self.left = self.right = None

    def __str__(self):
        return str((self.key, self.val))
    __repr__ = __str__
