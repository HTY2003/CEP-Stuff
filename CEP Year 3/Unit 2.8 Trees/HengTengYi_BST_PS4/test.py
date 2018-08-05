class Hi:
    def __init__(self, val, left=None):
        self.val = val
        self.left = left
    def __str__(self):
        return str(self.val)
    def newself(self, new):
        self = new

a = Hi(9, 10)
print(a)
a.newself(Hi(8, 9))
print(a, a.left)
