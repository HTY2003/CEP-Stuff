class PyListQueue1:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue"
        return self.items.pop()
    def size(self):
        return len(self.items)


class PyListQueue2:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue"
        return self.items.pop(0)
    def size(self):
        return len(self.items)



if __name__ == "__main__":
    q1 = PyListQueue2()

    for i in range(5):
        q1.enqueue(i)

    for i in range(5):
        print(q1.dequeue())


