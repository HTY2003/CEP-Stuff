class LLNode:
    __slots__ = ("val", "next")
    def __init__(self, val, next=None): self.val, self.next = val, next
    def __str__(self): return str(self.val)
    
