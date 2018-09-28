from ds_treenode import AVLNode
from ds_dyarray import DyArray

class AVLBST:
    '''
    AVL Tree ADT for CEP Final Project
    ----------------------------------
    This class was used for the attribute trees in the Contact Book ADT, and
    was chosen for its constant O(log n) access. With and and or searches, many
    values may be specified for searching, so it's essential that all values can
    be accessed quickly regardless of recent access (which is why the splay tree wasn't used)

    The Node class from ds_treenode.py was used for this implementation.
    '''
    __slots__ = ('root', 'length')

    #---BUILT-IN FUNCTIONS---
    def __init__(self, key=None, value=None):
        '''Initializes root and length attributes'''
        if key and value: self.root,self.length=AVLNode(key,value),1
        else: self.root,self.length=None,0

    def __str__(self):
        '''
        Returns an inorder string of key-value pairs in the tree
        Time complexity: O(n)

        E.g:
        >> a = AVLBST()
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
        >> a = AVLBST()
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
        >> a = AVLBST()
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
        Time complexity: O(log n)

        E.g:
        >> a = AVLBST()
        >> a.add(1, 2)
        >> print(a)
        [(1, 2)]
        >> print(1 in a)
        True
        >> print(2 in a)
        False
        '''
        return self.search(key) is not None

    def __setitem__(key, value):
        ''' Same as AVLBST.add(key, value) '''
        return self.add(key, value)

    def __getitem__(self, key):
        ''' Same as AVLBST.search(key) '''
        return self.search(key)

    def __delitem__(key):
        ''' Same as AVLBST.delete(key) '''
        return self.delete(key)

    __repr__ = __str__

    #---TREE FUNCTIONS---
    def add(self, key, value):
        '''
        Adds node with given key and value into the tree
        Time complexity: O(log n)

        E.g:
        >> a = AVLBST()
        >> a.add(1, 2)
        >> print(a)
        [(1, 2)]
        '''
        if self.root: self.root = self._addNode(self.root,AVLNode(key, value))
        else: self.root, self.length = AVLNode(key, value), 1

    def search(self,key):
        '''
        Returns the value of the node with the given key in the tree
        Time complexity: O(log n)

        E.g:
        >> a = AVLBST()
        >> a.add(1, 2)
        >> print(a)
        [(1, 2)]
        >> print(a.search(1))
        2
        '''
        return self._searchNode(key,self.root)

    def delete(self,key):
        '''
        Removes node with given key from the tree and returns its value
        Time complexity: O(log n)

        E.g:
        >> a = AVLBST()
        >> a.add(1, 2)
        >> print(a)
        [(1, 2)]
        >> print(a.delete(1))
        2
        >> print(a)
        []
        '''
        newroot, val = self._delNode(key, self.root)
        if newroot != 0: self.root = newroot
        return val

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
    def _addNode(self, root, node):
        '''
        Moves node down the tree and adds node in empty slot for AVLBST.add()
        Then it balances the tree to ensure constant O(log n access)'''
        #Standard BST insertion
        if root.key == node.key:
            if type(root.val) != DyArray:
                tmp = root.val
                root.val = DyArray(1)
                root.val[0] = tmp
            root.val.append(node.val)
        elif root.key > node.key:
            if root.left: root.left = self._addNode(root.left, node)
            else: root.left = node
        elif root.key < node.key:
            if root.right: root.right = self._addNode(root.right, node)
            else: root.right = node

        #updates height of each root
        root = self._heightupdate(root)
        #calculates balance of each sides
        balance = self._balancecal(root)
        #rotates accordingly
        if balance > 1 and node.key < root.left.key: return self._rightRotate(root)
        if balance < -1 and node.key > root.right.key: return self._leftRotate(root)
        if balance > 1 and node.key > root.left.key:
            root.left = self._leftRotate(root.left)
            return self._rightRotate(root)
        if balance < -1 and node.key < root.right.key:
            root.right = self._rightRotate(root.right)
            return self._leftRotate(root)
        #updates length
        self.length += 1
        return root

    def _searchNode(self,key,root):
        ''' Moves down the tree finding node with given key for SplayBST.search() '''
        if root:
            #return value
            if root.key == key: return root.val
            #move left
            elif root.key > key: return self._searchNode(key,root.left)
            #move right
            elif root.key < key: return self._searchNode(key,root.right)

    def _delNode(self,key,root,succnode=False):
        if root:
            #standard BST deletion
            if root.key > key: root.left, val = self._delNode(key, root.left)
            elif root.key < key: root.right, val = self._delNode(key, root.right)
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
                    root.right = self._delNode(succ.key, succ.right, True)

            #updates height of each root
            root = self._heightupdate(root)
            #calculates balance of each sides
            balance = self._balancecal(root)
            #rotates accordingly
            if balance > 1 and self._balancecal(root.left) >= 0: return self._rightRotate(root), val
            if balance < -1 and self._balancecal(root.right) <= 0: return self._leftRotate(root), val
            if balance > 1 and self._balancecal(root.left) < 0:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root), val
            if balance < -1 and self._balancecal(root.right) > 0:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root), val
            #updates length
            self.length -= 1
            return root, val
        return None if succnode else (0, None)

    def _leftRotate(self, node):
        '''Rotate nodes left for AVLBST._addNode() and AVLBST._delNode()'''
        #shift positions
        child = node.right
        tmp = child.left
        child.left = node
        node.right = tmp
        #update heights of all changed nodes
        node = self._heightupdate(node)
        child = self._heightupdate(child)
        return child

    def _rightRotate(self, node):
        '''Rotate nodes right for AVLBST._addNode() and AVLBST._delNode()'''
        #shift positions
        child = node.left
        tmp = child.right
        child.right = node
        node.left = tmp
        #update heights of all changed nodes
        node = self._heightupdate(node)
        child = self._heightupdate(child)
        return child

    def _heightcal(self, node):
        '''Return height of a node for AVLBST._balancecal() and AVLBST._heightupdate()'''
        return node.height if node else 0

    def _balancecal(self, node):
        '''Return balance of a node for AVLBST._addNode() and AVLBST._delNode()'''
        return self._heightcal(node.left) - self._heightcal(node.right) if node else 0

    def _heightupdate(self, node):
        '''Return balance of a node for AVLBST._addNode() and AVLBST._delNode()'''
        node.height = 1 + max(self._heightcal(node.left), self._heightcal(node.right))
        return node

    def _inOrderGen(self, root):
        '''Generates generator of all key-value pairs for AVLBST.inOrder()'''
        if root:
            yield from self._inOrderGen(root.left)
            yield (root.key, root.val)
            yield from self._inOrderGen(root.right)

    def _inOrderReverseGen(self, root):
        '''Generates generator of all key-value pairs for AVLBST.inOrderReverse()'''
        if root:
            yield from self._inOrderReverseGen(root.right)
            yield (root.key, root.val)
            yield from self._inOrderReverseGen(root.left)

    def _preOrderGen(self, root):
        '''Generates generator of all key-value pairs for AVLBST.preOrder()'''
        if root:
            yield (root.key, root.val)
            yield from self._preOrderReverseGen(root.right)
            yield from self._preOrderReverseGen(root.left)

    def _postOrderGen(self, root):
        '''Generates generator of all key-value pairs for AVLBST.postOrder()'''
        if root:
            yield from self._postOrderReverseGen(root.right)
            yield from self._postOrderReverseGen(root.left)
            yield (root.key, root.val)

    def _levelOrderGen(self, root):
        '''Generates generator of all key-value pairs for AVLBST.levelOrder()'''
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
