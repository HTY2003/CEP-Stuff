from linkedlistnode import LLNode

class TLinkedList:
    __slots__ = ("root", "length","tail")
    def __init__(self, val=None):
        if val is not None: self.root, self.length = LLNode(val), 1
        else: self.root, self.tail, self.length = None, 0
        self.tail = self.root

    def __str__(self):
        def strbuild(root, string="["):
            string += str(root) + ", "
            return strbuild(root.next, string) if root.next else string
        return strbuild(self.root)[:-2] + "]" if self.root else "[]"

    def __setitem__(self, index, val):
        position = self.root
        if position:
            if index == 0: self.root.val = val
            else:
                for i in range(index-1):
                    if position.next: position = position.next
                    else: raise IndexError("Invalid index")
                if position.next: position.next.val = val
                else: raise IndexError("Invalid index")
        else: self.root = self.tail = LLNode(val)

    def __getitem__(self, index):
        position = self.root
        if position:
            if index == 0: return position.val
            else:
                for i in range(index-1):
                    if position.next: position = position.next
                    else: raise IndexError("Invalid index")
                if position.next: return position.next.val
                else: raise IndexError("Invalid index")
        else: raise IndexError("Invalid index")

    def __iter__(self): return iter(self.LLgen())
    def __delitem__(self, index): return self.remove(index)
    def __len__(self): return self.length
    __repr__ = __str__
    def tolist(self): return list(self.LLgen())
    def LLgen(self):
        start = self.root
        while start:
            yield start
            start = start.next

    def append(self, val):
        def add(root, node):
            if root.next: add(root.next, node)
            else:
                root.next = node
                self.tail = root.next
        if self.root: add(self.root, LLNode(val))
        else: self.root = self.tail = LLNode(val)
        self.length += 1

    def insert(self, index, val):
        if index == 0: self.root = LLNode(val, self.root)
        else:
            position = self.root
            for i in range(index-1):
                if position.next: position = position.next
                else: raise IndexError("Invalid index")
            position.next = LLNode(val, next=position.next)
        if index == self.length: self.tail = position.next
        self.length += 1

    def remove(self, index=-1):
        if index < 0: index += self.length
        position = self.root
        if position:
            if index == 0:
                tmp = self.root
                if tmp == self.tail: self.tail = None
                self.root, tmp.next = self.root.next, None

            else:
                for i in range(index-1):
                    if position.next: position = position.next
                    else: raise IndexError("Invalid index")
                if position.next:
                    tmp = position.next
                    if tmp == self.tail: self.tail = position
                    position.next, tmp.next = position.next.next, None
                else: raise IndexError("Invalid index")
            self.length -= 1
            return tmp.val
        else: raise IndexError("Invalid index")

a = LinkedList(45)
print(a, a.root, a.tail)
a.append(44)
print(a, a.root, a.tail)
a.insert(2, 43)
print(a, a.root, a.tail)
a.remove()
print(a, a.root, a.tail)
