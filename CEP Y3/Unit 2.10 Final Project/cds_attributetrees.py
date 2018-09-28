import re
from ds_avltree import AVLBST
from ds_splaytree import SplayBST
from ds_treenode import AVLNode
from ds_dyarray import DyArray
from ds_set import Set
from cds_date import Date

#This file contains custom versions of the trees (AVL and Splay) with modifications and specific functions to the contact book

class Attribute_AVL(AVLBST):
    def __setitem__(self, key, value):
        ''' Same as Attribute_AVL.add(), but with the replace set to True '''
        return self.add(key, value, True)

    def add(self, key, value, replace = False):
        ''' Same as AVLBST.add(), but with a new replace toggle'''
        if self.root: self.root = self._addNode(self.root,AVLNode(key, value), replace)
        else: self.root, self.length = AVLNode(key, value), 1

    def _addNode(self, root, node, replace):
        '''Same as AVLBST.add(), but with duplicate keys being handled using Set.union() unless replace is True'''
        #---MAIN AREA OF CHANGE---
        if root.key == node.key:
            #replaces if replace is True
            if replace: root.val = node.val
            #does Set.union() otherwise
            else: root.val = root.val.union(node.val)
        elif root.key > node.key:
            if root.left: root.left = self._addNode(root.left, node, replace)
            else:
                root.left = node
        elif root.key < node.key:
            if root.right: root.right = self._addNode(root.right, node, replace)
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
        '''Returns leftmost node's key and value aka the minimum value'''
        node = self.root
        while node.left: node = node.left
        return node

    def max(self):
        '''Returns rightmost node's key and value aka the maximum value'''
        node = self.root
        while node.right: node = node.right
        return node

    def avg(self):
        '''Returns average of all nodes' keys (The ContactBook class makes sure this only happens on the phone and sex trees)'''
        value = 0
        count = 0
        for i in self._inOrderGen(self.root):
            for x in i[1]:
                value += i[0]
                count += 1
        return value/count

    def simsearch(self, string):
        '''
        Simple similarity search for attribute trees
        Time complexity: O(n)
        '''
        for i in self._inOrderGen(self.root):
            if re.match(str(string), str(i[0])): yield i[1]

    def treestr(self):
        '''Returns string of nested lists that can be used to build the tree'''
        def generate(root):
            if root:
                yield list(generate(root.left))
                yield (root.key, root.val, root.height)
                yield list(generate(root.right))
        return str(list(generate(self.root))) if self.root else '[]'

    def treebuild(self, lyststr):
        '''Builds tree from nested lists (converts list of values back into Sets)'''
        def createnode(lyst, root=None):
            if lyst:
                if root:
                    if root.key > lyst[1][0]:
                        root.left = AVLNode(lyst[1][0], Set(lyst[1][1]), lyst[1][2])
                        self.length += 1
                        root.left = createnode(lyst[0], root.left)
                        root.left = createnode(lyst[2], root.left)
                    else:
                        root.right = AVLNode(lyst[1][0], Set(lyst[1][1]), lyst[1][2])
                        self.length += 1
                        root.right = createnode(lyst[0], root.right)
                        root.right = createnode(lyst[2], root.right)
                else:
                    root = AVLNode(lyst[1][0], Set(lyst[1][1]), lyst[1][2])
                    self.length += 1
                    root = createnode(lyst[0], root)
                    root = createnode(lyst[2], root)
            return root
        if eval(lyststr, {'__builtins__':{}}): self.root = createnode(eval(lyststr, {'__builtins__':{}}))

class Attribute_Date_AVL(Attribute_AVL):
    def simsearch(self, string):
        '''
        Simple similarity search for Date tree
        Time complexity: O(n)
        '''
        for i in self._inOrderGen(self.root):
            if re.match(str(string), i[0].treestr()): yield i[1]

    def treestr(self):
        '''Returns string of nested lists(with custom Date treestr) that can be used to build the tree'''
        def generate(root):
            if root:
                yield list(generate(root.left))
                yield (root.key.treestr(), root.val, root.height)
                yield list(generate(root.right))
        return str(list(generate(self.root))) if self.root else '[]'

    def treebuild(self, lyststr):
        '''Builds tree from nested lists (converts treestr into Date and values back into Sets)'''
        def createnode(lyst, root=None):
            if lyst:
                if root:
                    if root.key > Date(lyst[1][0]):
                        root.left = AVLNode(Date(lyst[1][0]), Set(lyst[1][1]), lyst[1][2])
                        self.length += 1
                        root.left = createnode(lyst[0], root.left)
                        root.left = createnode(lyst[2], root.left)
                    else:
                        root.right = AVLNode(Date(lyst[1][0]), Set(lyst[1][1]), lyst[1][2])
                        self.length += 1
                        root.right = createnode(lyst[0], root.right)
                        root.right = createnode(lyst[2], root.right)
                else:
                    root = AVLNode(Date(lyst[1][0]), Set(lyst[1][1]), lyst[1][2])
                    self.length += 1
                    root = createnode(lyst[0], root)
                    root = createnode(lyst[2], root)
            return root
        if eval(lyststr, {'__builtins__':{}}): self.root = createnode(eval(lyststr, {'__builtins__':{}}))

class User_BST(SplayBST):
    def simsearch(self, string):
        '''
        Simple similarity search for user tree
        Time complexity: O(n)
        '''
        for i in self._inOrderGen(self.root):
            if re.match(str(string), str(i[0])): yield i[0]

    def treestr(self):
        '''Returns string of nested lists that can be used to build the tree (using the Date treestr)'''
        def generate(root):
            if root:
                yield list(generate(root.left))
                val = root.val[:5]
                val.append(root.val[5].treestr())
                val.append(root.val[6].treestr())
                yield (root.key, val)
                yield list(generate(root.right))
        return str(list(generate(self.root))) if self.root else '[]'

    def treebuild(self, lyststr):
        '''Builds tree from nested lists (converts treestr back into Date and converts values back into DyArray)'''
        def createnode(lyst, root=None):
            if lyst:
                if root:
                    if root.key > lyst[1][0]:
                        lyst[1][1][5] = Date(lyst[1][1][5])
                        lyst[1][1][6] = Date(lyst[1][1][6])
                        root.left = AVLNode(lyst[1][0], DyArray(0, iterator = lyst[1][1]))
                        self.length += 1
                        root.left = createnode(lyst[0], root.left)
                        root.left = createnode(lyst[2], root.left)
                    else:
                        lyst[1][1][5] = Date(lyst[1][1][5])
                        lyst[1][1][6] = Date(lyst[1][1][6])
                        root.right = AVLNode(lyst[1][0], DyArray(0, iterator = lyst[1][1]))
                        self.length += 1
                        root.right = createnode(lyst[0], root.right)
                        root.right = createnode(lyst[2], root.right)
                else:
                    lyst[1][1][5] = Date(lyst[1][1][5])
                    lyst[1][1][6] = Date(lyst[1][1][6])
                    root = AVLNode(lyst[1][0], DyArray(0, iterator = lyst[1][1]))
                    self.length += 1
                    root = createnode(lyst[0], root)
                    root = createnode(lyst[2], root)
            return root
        if eval(lyststr, {'__builtins__':{}}): self.root = createnode(eval(lyststr, {'__builtins__':{}}))
