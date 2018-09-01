from ds_avltree import AVLBST
from ds_treenode import AVLNode
from ds_dyarray import DyArray

class Attribute_AVL(AVLBST):
    def __setitem__(self, key, value): return self.add(key, value, True)

    def add(self, key, value, replace = False):
        if self.root: self.root = self.addNode(self.root,AVLNode(key, value), replace)
        else: self.root, self.length = AVLNode(key, value), 1

    def addNode(self, root, node, replace):
        if root.key == node.key:
            if replace: root.val = node.val
            else: root.val = root.val.union(node.val)
        elif root.key > node.key:
            if root.left: root.left = self.addNode(root.left, node, replace)
            else:
                root.left = node
        elif root.key < node.key:
            if root.right: root.right = self.addNode(root.right, node, replace)
            else:
                root.right = node
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

    def min(self):
        node = self.root
        while node.left: node = node.left
        return node.value

    def max(self):
        node = self.root
        while node.right: node = node.right
        return node.value

    def sorted(self):
        lyst = DyArray(capacity=(self.length + 1))
        for i in self._inOrderGen:
            if type(i[1]) is DyArray:
                for x in i[1]:
                    lyst.append(i[0], x)
            else: lyst.append(i[0], i[1])
        return lyst

    def simsearch(self, string):
        for i in self._inOrderGen(self.root):
            if str(string) in str(i[0]): yield i[1]

#    def treebuild(self):
