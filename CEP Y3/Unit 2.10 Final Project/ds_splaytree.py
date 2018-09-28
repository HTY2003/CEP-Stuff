from ds_treenode import Node

class SplayBST:
    '''
    Binary Splay Tree ADT for CEP Final Project
    ---------------------------------------------
    For the user tree in the Contact Book ADT, the splay tree was used
    This type of tree has the advantage of maintaining recently accessed order,
    so the user can list users in recently-accessed order, and see the data
    of those he edited or searched most recently quickly,
    providing both convenience for the user and speed in the back-end.

    The Node class from ds_treenode.py was used for this implementation.
    '''
    __slots__ = ('root', 'length')

    #---BUILT-IN FUNCTIONS---
    def __init__(self, key=None, value=None):
        '''Initializes root and length attributes'''
        if key: self.root,self.length = Node(key, value),1
        else: self.root = self.length = 0

    def __str__(self):
        '''
        Returns an inorder string of key-value pairs in the tree
        Time complexity: O(n)

        E.g:
        >> a = SplayBST()
        >> a.add(1, 2)
        >> a.add(2, 3)
        >> print(a)
        [(1, 2), (2, 3)]
        '''
        string = ''
        for i in self._inOrderGen(self.root): string += str(i) + ', '
        return '[' + string[:-2] + ']'

    def __len__(self):
        '''
        Returns the number of nodes in the tree
        Time complexity: O(1)

        E.g:
        >> a = SplayBST()
        >> a.add(1, 2)
        >> a.add(2, 3)
        >> print(len(a))
        2
        '''
        return self.length

    def __iter__(self):
        '''
        Iterates through the key-value pair(tuple) of every node in the tree sorted inorder
        Time complexity: O(n)

        E.g:
        >> a = SplayBST()
        >> a.add(1, 2)
        >> a.add(2, 3)
        >> for i in a:
        >>     print(i)
        (1, 2)
        (2, 3)
        '''
        return iter(self._inOrderGen(self.root))

    def __contains__(self, key):
        '''
        Returns whether a node with the given key is in the tree
        Time complexity (Average): O(log n)
        Time complexity (Worst case): O(n)

        E.g:
        >> a = SplayBST()
        >> a.add(1, 2)
        >> print(a)
        [(1, 2)]
        >> print(1 in a)
        True
        >> print(2 in a)
        False
        '''
        return self.search(key) != None

    def __setitem__(key, value):
        ''' Same as SplayBST.add(key, value) '''
        return self.add(key, value)

    def __getitem__(self, key):
        ''' Same as SplayBST.search(key) '''
        return self.search(key)

    def __delitem__(key):
        ''' Same as SplayBST.delete(key) '''
        return self.delete(key)

    __repr__ = __str__

    #---TREE FUNCTIONS---
    def add(self, key, value):
        '''
        Adds node with given key and value into the tree
        Time complexity (Average): O(log n)
        Time complexity (Worst case): O(n)

        E.g:
        >> a = SplayBST()
        >> a.add(1, 2)
        >> print(a)
        [(1, 2)]
        '''
        assert key is not None, 'Key cannot be None'
        if self.length:
            #add node, then splay it to root
            self.root = self._splayNode(self.root, self._addNode(self.root, key, value))
        else:
            #set node as new root
            self.root,self.length = Node(key, value),1

    def search(self, key):
        '''
        Returns the value of the node with the given key in the tree
        Time complexity (Average): O(log n)
        Time complexity (Worst case): O(n)

        E.g:
        >> a = SplayBST()
        >> a.add(1, 2)
        >> print(a)
        [(1, 2)]
        >> print(a.search(1))
        2
        '''
        assert key is not None, 'Key cannot be None'
        #search for node
        node = self._searchNode(self.root, key)
        #splay node to root
        self.root = self._splayNode(self.root, node)
        return node.val if node else None

    def delete(self, key, pop=False):
        '''
        Removes node with given key from the tree and returns its value
        Time complexity (Average): O(log n)
        Time complexity (Worst case): O(n)

        E.g:
        >> a = SplayBST()
        >> a.add(1, 2)
        >> print(a)
        [(1, 2)]
        >> print(a.delete(1))
        2
        >> print(a)
        []
        '''
        #search node, then splay it to root
        self.root = self._splayNode(self.root, self._searchNode(self.root, key))
        #store node value
        value = self.root.val
        #delete node
        self.root = self._delNode(self.root, key)
        return value

    #---SORTING FUNCTIONS---
    def inOrder(self):
        '''
        Returns list containing all key-value pairs(tuples) of all nodes sorted inorder
        Time complexity: O(n)
        '''
        return list(self._inOrderGen(self.root))
    def inOrderReverse(self):
        '''
        Returns list containing all key-value pairs(tuples) of all nodes sorted inorder in reverse
        Time complexity: O(n)
        '''
        return list(self._inOrderReverseGen(self.root))
    def preOrder(self):
        '''
        Returns list containing all key-value pairs(tuples) of all nodes sorted preorder
        Time complexity: O(n)
        '''
        return list(self._preOrderGen(self.root))
    def postOrder(self):
        '''
        Returns list containing all key-value pairs(tuples) of all nodes sorted postorder
        Time complexity: O(n)
        '''
        return list(self._postOrderGen(self.root))
    def levelOrder(self):
        '''
        Returns list containing all key-value pairs(tuples) of all nodes sorted level order
        Time complexity: O(n)
        '''
        return list(self._levelOrderGen(self.root))

    #---HIDDEN FUNCTIONS---
    def _addNode(self, root, key, value):
        ''' Moves node down the tree and adds node in empty slot for SplayBST.add() '''
        def _insert(root, node):
            if root.key == node.key:
                root.val = node.val
                return root
            if root.key < node.key:
                #move right if key is larger than root's key
                if root.right:
                    return _insert(root.right, node)
                #add node if slot is empty
                else:
                    self.length += 1
                    root.right = node
            else:
                #move left if key is smaller than root's key
                if root.left:
                    return _insert(root.left, node)
                #add node if slot is empty
                else:
                    root.left = node
                    self.length += 1
            return node
        return _insert(root, Node(key, value))

    def _searchNode(self, root, key):
        ''' Moves down the tree finding node with given key for SplayBST.search() '''
        def _search(root, key):
            if root:
                #return value
                if root.key == key: return root
                #move right
                if root.key < key: return _search(root.right, key)
                #move left
                if root.key > key: return _search(root.left, key)
        return _search(root, key)

    def _delNode(self, root, key):
        ''' Removes node to be deleted (already in root position) and replaces it with a successor for SplayBST.delete() '''
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
                temp.left = None
                temp.right = None
            del temp
            self.length -= 1
            return root
        if root: return _delete(root, key)

    def _splayNode(self, root, node):
        '''Splays node to become the new root of the tree for all functions: SplayBST.add(), SplayBST.delete(), SplayBST.search()'''

        '''
        Main steps Zig and Zag (Credit: GeeksforGeeks)
                y                                     x
               / \     Zig (Right Rotation)          /  \
              x   T3   – - – - – - – - - ->         T1   y
             / \       < - - - - - - - - -              / \
            T1  T2     Zag (Left Rotation)            T2   T3
        '''
        #Right Rotation(Zig)
        def _zig(node, parent, grandnode=None):
            parent.left = node.right
            node.right = parent
            if grandnode:
                if grandnode.left == parent: grandnode.left = node
                if grandnode.right == parent: grandnode.right = node
        #Left Rotation(Zag)
        def _zag(node, parent, grandnode=None):
            parent.right = node.left
            node.left = parent
            if grandnode:
                if grandnode.left == parent: grandnode.left = node
                if grandnode.right == parent: grandnode.right = node
        #No need to rotate if node is already root
        if root == node or node is None or root is None: return root
        #if node is left child of root, a right rotation (or zig) is performed
        if root.left == node:
            _zig(node, root)
            return node
        #if node is right child of root, a left rotation (or zag) is performed
        if root.right == node:
            _zag(node, root)
            return node
        '''
        When the node is a left-left or right-right grandchild of root, simply
        rotating the node up 2 levels will destroy the recently-accessed order
        of the tree. Hence, the parent must be rotated up before the node.
        These two steps are known as Zig-Zig and Zag-Zag.

        For left-right and right-left grandchild situations, rotating the node
        up will not destroy the order, so the node is simply rotated up twice.
        These steps are known as Zig-Zag and Zag-Zig.
        '''
        if root.left:
        #Zig-Zig
            if root.left.left == node:
                temp = root.left
                #rotates parent to root
                _zig(root.left, root)
                #rotates node to root
                _zig(node, temp)
                return node
        #Zig-Zag
            elif root.left.right == node:
                #rotates node to parent
                _zag(node, root.left, grandnode=root)
                #rotates node to root
                _zig(node, root)
                return node
        #Zag-Zag
        if root.right:
            if root.right.right == node:
                temp = root.right
                #rotates parent to root
                _zag(root.right, root)
                #rotates node to root
                _zag(node, temp)
                return node
        #Zag-Zig
            elif root.right.left == node:
                #rotates node to parent
                _zig(node, root.right, grandnode=root)
                #rotates node to root
                _zag(node, root)
                return node

        '''
        If the node is not a child or grandchild of root, it means that the node
        does not exist, or is more than two levels down from the root. Hence, we have
        to keep rotating the node upwards until the node is a child or grandchild.

        So, we find the parent and grandparent of the node before making the node
        zig-zig, zig-zag, zag-zig, or zag-zag upwards based on its position. Then,
        the node is run through the function once again to check if it is a child
        or grandchild of root.
        '''
        #finds parent
        p = self._parent(root, node.key)
        #find grandparent
        if p: gp = self._parent(root, p.key)
        else: return root
        #finds great-grandparent
        if gp: gpp = self._parent(root, gp.key)
        else: return root
        #moves the node up by two levels based on our 4 cases
        if gp.left:
        #Zig-Zig
            if gp.left.left == node:
                temp = gp.left
                _zig(gp.left, gp, grandnode=gpp)
                _zig(node, temp, grandnode=gpp)
        #Zig-Zag
            elif gp.left.right == node:
                _zag(node, gp.left, grandnode=gp)
                _zig(node, gp, grandnode=gpp)
        #Zag-Zag
        if gp.right:
            if gp.right.right == node:
                temp = gp.right
                _zag(gp.right, gp, grandnode=gpp)
                _zag(node, temp, grandnode=gpp)
        #Zag-Zig
            elif gp.right.left == node:
                _zig(node, gp.right, grandnode=gp)
                _zag(node, gp, grandnode=gpp)
        #Repeats splay operation until node is root
        return self._splayNode(root, node)

    def _parent(self, root, key):
        '''Returns parent node of any node in the tree'''
        if root:
            if root.left:
                if root.left.key == key: return root
                elif root.key > key: return self._parent(root.left, key)
            if root.right:
                if root.right.key == key: return root
                elif root.key < key: return self._parent(root.right, key)

    def _inOrderGen(self, root):
        '''Generates generator of all key-value pairs for SplayBST.inOrder()'''
        if root:
            yield from self._inOrderGen(root.left)
            yield (root.key, root.val)
            yield from self._inOrderGen(root.right)

    def _inOrderReverseGen(self, root):
        '''Generates generator of all key-value pairs for SplayBST.inOrderReverse()'''
        if root:
            yield from self._inOrderReverseGen(root.right)
            yield (root.key, root.val)
            yield from self._inOrderReverseGen(root.left)

    def _preOrderGen(self, root):
        '''Generates generator of all key-value pairs for SplayBST.preOrder()'''
        if root:
            yield (root.key, root.val)
            yield from self._preOrderReverseGen(root.right)
            yield from self._preOrderReverseGen(root.left)

    def _postOrderGen(self, root):
        '''Generates generator of all key-value pairs for SplayBST.postOrder()'''
        if root:
            yield from self._postOrderReverseGen(root.right)
            yield from self._postOrderReverseGen(root.left)
            yield (root.key, root.val)

    def _levelOrderGen(self, root):
        '''Generates generator of all key-value pairs for SplayBST.levelOrder()'''
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
