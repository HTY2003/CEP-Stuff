from ds_treenode import AVLNode
from ds_dyarray import DyArray

class AVLBST:
    __slots__ = ('root', 'length')
    def __init__(self, key=None, value=None):
        if key and value: self.root,self.length=AVLNode(key,value),1
        else: self.root,self.length=None,0

    def __str__(self):
        string = ''
        for i in self._inOrderGen(self.root): string += str(i) + ', '
        return '[' + string[:-2] + ']'

    def __len__(self): return self.length
    def __iter__(self): return iter(self._inOrderGen(self.root))
    def __reversed__(self): return self._inOrderReverse(self.root)
    def __contains__(self, key): return self.search(key) is not None
    def __setitem__(self, key, value): return self.add(key, value)
    def __getitem__(self, key): return self.search(key)
    def __delitem__(key): return self.delete(key)
    __repr__ = __str__

    def add(self, key, value):
        if self.root: self.root = self.addNode(self.root,AVLNode(key, value))
        else: self.root, self.length = AVLNode(key, value), 1

    def addNode(self, root, node):
        if root.key == node.key:
            if type(root.val) != DyArray:
                tmp = root.val
                root.val = DyArray(1)
                root.val[0] = tmp
            root.val.append(node.val)
        elif root.key > node.key:
            if root.left: root.left = self.addNode(root.left, node)
            else: root.left = node
        elif root.key < node.key:
            if root.right: root.right = self.addNode(root.right, node)
            else: root.right = node
        root = self._heightupdate(root)
        balance = self._balancecal(root)
        if balance > 1 and node.key < root.left.key: return self._rightRotate(root)
        if balance < -1 and node.key > root.right.key: return self._leftRotate(root)
        if balance > 1 and node.key > root.left.key:
            root.left = self._leftRotate(root.left)
            return self._rightRotate(root)
        if balance < -1 and node.key < root.right.key:
            root.right = self._rightRotate(root.right)
            return self._leftRotate(root)
        self.length += 1
        return root

    def search(self,key): return self.searchNode(key,self.root)

    def searchNode(self,key,root):
        if root:
            if root.key == key: return root.val
            elif root.key > key: return self.searchNode(key,root.left)
            elif root.key < key: return self.searchNode(key,root.right)

    def delete(self,key):
        newroot, val = self.delNode(key, self.root)
        if newroot != 0: self.root = newroot
        return val

    def delNode(self,key,root):
        if root:
            if root.key > key: root.left, val = self.delNode(key, root.left)
            elif root.key < key: root.right, val = self.delNode(key, root.right)
            else:
                if root.left is None:
                    tmp, val = root.left, root.val
                    root = None
                    return tmp, val
                elif root.right is None:
                    tmp, val = root.right, root.val
                    root = None
                    return tmp, val
                else:
                    succ, val = root.right, root.val
                    while succ.left: succ = succ.left
                    root.key, root.val = succ.key, succ.val
                    self.length += 1
                    root.right = self.delNode(succ.key, succ.right)
            if root is None: return root
            root = self._heightupdate(root)
            balance = self._balancecal(root)
            if balance > 1 and self._balancecal(root.left) >= 0: return self._rightRotate(root), val
            if balance < -1 and self._balancecal(root.right) <= 0: return self._leftRotate(root), val
            if balance > 1 and self._balancecal(root.left) < 0:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root), val
            if balance < -1 and self._balancecal(root.right) > 0:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root), val
            self.length -= 1
            return root, val
        return 0, None

    def _leftRotate(self, node):
        child = node.right
        tmp = child.left
        child.left = node
        node.right = tmp
        node = self._heightupdate(node)
        child = self._heightupdate(child)
        return child

    def _rightRotate(self, node):
        child = node.left
        tmp = child.right
        child.right = node
        node.left = tmp
        node = self._heightupdate(node)
        child = self._heightupdate(child)
        return child

    def _heightcal(self, node): return node.height if node else 0
    def _balancecal(self, node): return self._heightcal(node.left) - self._heightcal(node.right) if node else 0
    def _heightupdate(self, node):
        node.height = 1 + max(self._heightcal(node.left), self._heightcal(node.right))
        return node

    def _inOrderGen(self, root):
        if root:
            yield from self._inOrderGen(root.left)
            yield (root.key, root.val)
            yield from self._inOrderGen(root.right)

    def _inOrderReverseGen(self, root):
        if root:
            yield from self._inOrderReverseGen(root.right)
            yield (root.key, root.val)
            yield from self._inOrderReverseGen(root.left)

    def _preOrderGen(self, root):
        if root:
            yield (root.key, root.val)
            yield from self._preOrderReverseGen(root.right)
            yield from self._preOrderReverseGen(root.left)

    def _postOrderGen(self, root):
        if root:
            yield from self._postOrderReverseGen(root.right)
            yield from self._postOrderReverseGen(root.left)
            yield (root.key, root.val)

    def _levelOrderGen(self, root):
        if root:
            base = 0
            queue = [(root, base)]
            while len(queue) > 0:
                yield (queue[0][0].key, queue[0][0].val, queue[0][1])
                node, base = queue.pop(0)
                if node.left: queue.append((node.left,base+1))
                if node.right: queue.append((node.right,base+1))
