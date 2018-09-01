from ds_treenode import Node

class SplayBST:
    __slots__ = ('root', 'length')
    def __init__(self, key=None, value=None):
        if key: self.root,self.length = Node(key, value),1
        else: self.root = self.length = None

    def __str__(self):
        string = ''
        for i in self._inOrderGen(self.root): string += str(i) + ', '
        return '[' + string[:-2] + ']'

    def __len__(self): return self.length
    def __iter__(self): return iter(self._inOrderGen(self.root))
    def __reversed__(self): return self._inOrderReverse(self.root)
    def __contains__(self, key): return self.search(key) is not None
    def __setitem__(key, value): return self.add(key, value)
    def __getitem__(self, key): return self.search(key)
    def __delitem__(key): return self.delete(key)
    __repr__ = __str__

    def add(self, key, value):
        assert key is not None, 'Key cannot be None'
        if self.length: self.root = self._splayNode(self.root, self._addNode(self.root, key, value))
        else: self.root,self.length = Node(key, value),1

    def search(self, key):
        assert key is not None, 'Key cannot be None'
        node = self._searchNode(self.root, key)
        self.root = self._splayNode(self.root, node)
        return node.val if node else None

    def delete(self, key, pop=False):
        self.root = self._splayNode(self.root, self._searchNode(self.root, key))
        if pop: value = self.root.val
        self.root = self._delNode(self.root, key)
        if pop: return value

    def inOrder(self): return list(self._inOrderGen(self.root))
    def inOrderReverse(self): return list(self._inOrderReverseGen(self.root))
    def preOrder(self): return list(self._preOrderGen(self.root))
    def postOrder(self): return list(self._postOrderGen(self.root))
    def levelOrder(self): return list(self._levelOrderGen(self.root))
    def layer(self): return self.levelOrder()[-1][2]

    def _addNode(self, root, key, value):
        def _insert(root, node):
            if root.key == node.key:
                root.val = node.val
                return root
            if root.key < node.key:
                if root.right: return _insert(root.right, node)
                else: root.right = node
            else:
                if root.left: return _insert(root.left, node)
                else: root.left = node
            self.length += 1
            return node
        return _insert(root, Node(key, value))

    def _searchNode(self, root, key):
        def _search(root, key):
            if root:
                if root.key == key: return root
                if root.key < key: return _search(root.right, key)
                if root.key > key: return _search(root.left, key)
        return _search(root, key)

    def _delNode(self, root, key):
        def _findMinNode(node):
            return _findMinNode(node.left) if node.left else node
        def _delete(root, key):
            if key != root.key: return root
            if root.right is None:
                temp = root
                root = root.left
                temp.left = None
            else:
                temp = root
                root = self._splayNode(root, _findMinNode(root.right))
                root.left = temp.left
                temp.left = temp.right = None
            del temp
            self.length -= 1
            return root
        if root: return _delete(root, key)

    def _splayNode(self, root, node):
        def _zig(node, parent, grandnode=None):
            parent.left = node.right
            node.right = parent
            if grandnode:
                if grandnode.left == parent: grandnode.left = node
                if grandnode.right == parent: grandnode.right = node
        def _zag(node, parent, grandnode=None):
            parent.right = node.left
            node.left = parent
            if grandnode:
                if grandnode.left == parent: grandnode.left = node
                if grandnode.right == parent: grandnode.right = node
        if root == node or node is None or root is None: return root
        if root.left == node:
            _zig(node, root)
            return node
        if root.right == node:
            _zag(node, root)
            return node
        if root.left:
            if root.left.left == node:
                temp = root.left
                _zig(root.left, root)
                _zig(node, temp)
                return node
            elif root.left.right == node:
                _zag(node, root.left, grandnode=root)
                _zig(node, root)
                return node
        if root.right:
            if root.right.right == node:
                temp = root.right
                _zag(root.right, root)
                _zag(node, temp)
                return node
            elif root.right.left == node:
                _zig(node, root.right, grandnode=root)
                _zag(node, root)
                return node
        p = self._parent(root, node.key)
        if p: gp = self._parent(root, p.key)
        else: return root
        if gp: gpp = self._parent(root, gp.key)
        else: return root
        if gp.left:
            if gp.left.left == node:
                temp = gp.left
                _zig(gp.left, gp, grandnode=gpp)
                _zig(node, temp, grandnode=gpp)
            elif gp.left.right == node:
                _zag(node, gp.left, grandnode=gp)
                _zig(node, gp, grandnode=gpp)
        if gp.right:
            if gp.right.right == node:
                temp = gp.right
                _zag(gp.right, gp, grandnode=gpp)
                _zag(node, temp, grandnode=gpp)
            elif gp.right.left == node:
                _zig(node, gp.right, grandnode=gp)
                _zag(node, gp, grandnode=gpp)
        return self._splayNode(root, node)

    def _parent(self, root, key):
        if root:
            if root.left:
                if root.left.key == key: return root
                elif root.key > key: return self._parent(root.left, key)
            if root.right:
                if root.right.key == key: return root
                elif root.key < key: return self._parent(root.right, key)

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
                node = queue.pop(0)[0]
                if node.left is not None:
                    queue.append((node.left, base+1))
                if node.right is not None:
                    queue.append((node.right, base+1))
                base += 1
