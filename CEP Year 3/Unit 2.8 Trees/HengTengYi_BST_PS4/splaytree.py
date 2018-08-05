from splaynode import Node
from dyarray import DyArray

class SplayBST:
    '''
Binary splay tree, where a node is splayed to the top of the tree when it is added to the tree or accessed
through a binary search. When a node is deleted, the parent of the deleted node is splayed instead.

Keeping the more frequently accessed nodes near the top of the tree allows for extremely fast access speeds
when accessing the same few nodes over and over, resulting in possibly O(1) search time complexity.

Nodes are created with key-value pairs, the value being returned when a node with the corresponding key is found.
Duplicate keys are handled by making the value an array and appending the new value.

To reduce the memory burden that the linked nodes cause, the class instructs Python to only use a static amount
of memory for our fixed number of variables, reducing RAM usage drastically
    '''

    #allocate static amount of memory to variables instead of a dynamic dictionary
    #this can reduce up to 40% of RAM
    __slots__ = ('root', 'length')

    def __init__(self, key=None, value=None):
        '''
        Initializes root node with the given key and value, and starts the length of the tree at 1
        Time complexity: O(1)

        E.g:
        >>> a = SplayBST(1, 2)
        >>> print(a.root)
        (1, 2)
        >>> print(a.length)
        1
        '''
        if key: self.root,self.length = Node(key, value),1
        else: self.root = self.length = None

    def __len__(self):
        '''
        Returns length of tree when len() is called
        Time complexity: O(1)

        E.g:
        >>> a = SplayBST(1, 2)
        >>> print(len(a))
        1
        '''
        return self.length

    def __str__(self):
        '''
        Returns string of all nodes in ascending order
        Time complexity: O(n)

        E.g:
        >>> a = SplayBST(1, 2)
        >>> a.add(2, 1)
        >>> a.add(1.5, 3)
        >>> print(a)
        [(1.5, 3), (1, 2), (2, 1)]
        '''
        string = ''
        for i in self._inOrderGen(self.root): string += str(i) + ', '
        return '[' + string[:-2] + ']'
    __repr__ = __str__

    def __iter__(self):
        '''
        Iterates through all nodes in ascending order
        Time complexity: O(n)

        E.g:
        >>> a = SplayBST(1, 2)
        >>> a.add(2, 1)
        >>> a.add(1.5, 3)
        >>> for i in a:
        >>>     print(i)
        (1, 2)
        (1.5, 3)
        (2, 1)
        '''
        return iter(self._inOrderGen(self.root))

    def __reversed__(self):
        '''
        Returns a list of all nodes in descending order
        Time complexity: O(n)

        >>> a = SplayBST(1, 2)
        >>> a.add(2, 1)
        >>> a.add(1.5, 3)
        >>> b = reversed(a)
        >>> print(b)
        [(2, 1), (1.5, 3), (1, 2)]
        >>> print(type(b))
        list
        '''
        return self._inOrderReverse(self.root)

    def __contains__(self, key):
        '''
        Returns whether key is present in tree
        Time complexity(Average): O(log n)
        Time complexity(Worst-case): O(n)

        E.g:
        >>> a = SplayBST(1, 2)
        >>> print(1 in a)
        True
        >>> print(2 in a)
        False
        '''
        return self.search(key) is not None

    def __setitem__(key, value):
        '''Same as self.add(key, value):''' + self.add.__doc__
        return self.add(key, value)

    def __getitem__(self, key):
        '''Same as self.search(key, value):''' + self.search.__doc__
        return self.search(key)

    def __delitem__(key):
        '''Same as self.delete(key, value):''' + self.delete.__doc__
        return self.delete(key)

    def add(self, key, value):
        '''
        Adds a node with the given key and value to the tree and splays it to the top of the tree
        Time complexity(Average): O(log n)
        Time complexity(Worst-case): O(n)

        >>> a = SplayBST(1, 2)
        >>> a.add(2, 3)
        >>> print(a)
        [(2, 3), (1, 2)]
        >>> a.add(1.5, 0)
        [(1.5, 0), (1, 2), (2, 3)]
        '''
        assert key is not None, 'Key cannot be None'
        #adds node and splays it if there is a root
        if self.length: self.root = self._splayNode(self.root, self._addNode(self.root, key, value))
        #makes node root if there is not root
        else: self.root,self.length = Node(key, value),1

    def search(self, key):
        '''
        Searches for the node with the given key and returns its corresponding value
        If the node does not exist, None is returned
        If it does exist, it is splayed to the top of the tree

        Time complexity(Average): O(log n)
        Time complexity(Worst-case): O(n)

        >>> a = SplayBST(1, 2)
        >>> print(a.search(1))
        2
        >>> print(a.search(2))
        None
        '''
        assert key is not None, 'Key cannot be None'
        #searches node
        node = self._searchNode(self.root, key)
        #splays node
        self.root = self._splayNode(self.root, node)
        #returns value
        return node.val if node else None

    def delete(self, key, pop=False):
        '''
        Searches for the node and removes it from the tree. If pop is set as True, the value of the node is also returned.
        If the node is not present in the tree and pop is True however, None is returned.
        Then, the parent of the deleted node is splayed to the top of the tree.

        Time complexity(Average): O(log n)
        Time complexity(Worst-case): O(n)

        >>> a = SplayBST(1, 2)
        >>> a.add(2, 3)
        >>> a.add(1.5, 0)
        >>> print(a)
        [(1.5, 0), (1, 2), (2, 3)]
        >>> a.delete(1.5)
        >>> print(a)
        [(2, 3), (1, 2)]
        >>> print(a.delete(1, pop=True), a)
        2 [(2, 3)]
        '''
        #splays node to be deleted
        self.root = self._splayNode(self.root, self._searchNode(self.root, key))
        #stores value if pop
        if pop: value = self.root.val
        #deletes node and replaces it
        self.root = self._delNode(self.root, key)
        #return value if pop
        if pop: return value

    def inOrder(self):
        '''Returns inorder list of all nodes'''
        return list(self._inOrderGen(self.root))

    def inOrderReverse(self):
        '''Returns reverse inorder list of all nodes'''
        return list(self._inOrderReverseGen(self.root))

    def preOrder(self):
        '''Returns preorder list of all nodes'''
        return list(self._preOrderGen(self.root))

    def postOrder(self):
        '''Returns postorder list of all nodes'''
        return list(self._postOrderGen(self.root))

    def levelOrder(self):
        '''Returns levelorder list of all nodes'''
        return list(self._levelOrderGen(self.root))

    def layer(self):
        '''Returns number of layers the tree has (mostly for debugging)'''
        return self.levelOrder()[-1][2]

    def _addNode(self, root, key, value):
        '''
        Function that inserts a new node into the tree if a new key is specified, and appends value to an array if an existing key is given
        The position is determined by the key (left if it is less than a node, right if it is more than a node)
        '''
        def _insert(root, node):
            #appends value if duplicate key is given
            if root.key == node.key:
                #makes new array if needed
                if type(root.val) != DyArray:
                    temp = root.val
                    root.val = DyArray(1)
                    root.val[0] = temp
                #appends value
                root.val.append(node.val)
                return root
            #when key is more than node's key
            if root.key < node.key:
                #moves right if root.right is taken
                if root.right: return _insert(root.right, node)
                #inserts node if root.right is empty
                else: root.right = node
            #when key is less than node's key
            else:
                #moves left if root.left is taken
                if root.left: return _insert(root.left, node)
                #inserts node if root.left is empty
                else: root.left = node
            #updates length
            self.length += 1
            #return newly inserted node to be splayed later on
            return node
        return _insert(root, Node(key, value))

    def _searchNode(self, root, key):
        '''
        Function that binary searches for the node with the given key based on the key's value
        If the key cannot be found, None is returned
        '''
        def _search(root, key):
            if root:
                #if node's key matches given key, the node is found and returned
                if root.key == key: return root
                #if they do not match, search continues right if the key is more than node's key (left if less than)
                if root.key < key: return _search(root.right, key)
                if root.key > key: return _search(root.left, key)
            #if the search cannot proceed left/right, it is assumed the node does not exist, and nothing(or None) is returned
        return _search(root, key)

    def _delNode(self, root, key):
        '''
        Function that finds a new root after the node to be deleted to splayed as root
        Then it removes any references to the node to be deleted, and frees it from memory
        If the key cannot be found, there is no splaying performed
        '''
        def _findMinNode(node):
            #keeps moving left until it finds the leftmost node
            return _findMinNode(node.left) if node.left else node
        def _delete(root, key):
            #if keys do not match, it shows the splay in self.delete() was unsuccessful, meaning the key was not found
            if key != root.key: return root
            #if the root has no right node, the left node can replace it as the new root
            if root.right is None:
                temp = root
                root = root.left
                temp.left = None
            #if it does have a right node, the minimum of its right node is splayed and replaces the root
            else:
                temp = root
                root = self._splayNode(root, _findMinNode(root.right))
                root.left = temp.left
                temp.left = temp.right = None
            #nodes not referenced are freed from memory
            del temp
            #updates length
            self.length -= 1
            #returns new root
            return root
        if root: return _delete(root, key)

    def _splayNode(self, root, node):
        '''
        Function that splays the node up the tree until it becomes root
        while maintaining the priority and order of previously splayed nodes
        '''

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
        #aborts mission if node is not found in tree
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
        '''
        Returns parent of node with given key
        If parent is not found, None is returned
        '''
        if root:
            if root.left:
                #returns root(parent) if its child has the key
                if root.left.key == key: return root
                #moves left if the key is less than root
                elif root.key > key: return self._parent(root.left, key)
            if root.right:
                #returns root(parent) if its child has the key
                if root.right.key == key: return root
                #moves right if the key is more than root
                elif root.key < key: return self._parent(root.right, key)

    def _inOrderGen(self, root):
        '''Returns inorder generator of all nodes'''
        if root:
            for node in self._inOrderGen(root.left): yield node
            yield (root.key, root.val)
            for node in self._inOrderGen(root.right): yield node

    def _inOrderReverseGen(self, root):
        '''Returns reverse inorder generator of all nodes'''
        if root:
            for node in self._inOrderReverseGen(root.right): yield node
            yield (root.key, root.val)
            for node in self._inOrderReverseGen(root.left): yield node

    def _preOrderGen(self, root):
        '''Returns preorder generator of all nodes'''
        if root:
            yield (root.key, root.val)
            for node in self._inOrderReverseGen(root.right): yield node
            for node in self._inOrderReverseGen(root.left): yield node

    def _postOrderGen(self, root):
        '''Returns postorder generator of all nodes'''
        if root:
            for node in self._inOrderReverseGen(root.right): yield node
            for node in self._inOrderReverseGen(root.left): yield node
            yield (root.key, root.val)

    def _levelOrderGen(self, root):
        '''Returns levelorder generator of all nodes'''
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
