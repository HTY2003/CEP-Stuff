class Node:
    __slots__=('key', 'val', 'left', 'right')
    def __init__(self, key, value):
        self.key,self.val,self.left,self.right = key,value,None,None
    def __str__(self):return str((self.key, self.val))
    __repr__=__str__
class BST:
    __slots__=('root', 'length')
    def __init__(self,key=None,value=None):
        if key and value:self.root,self.length=Node(key,value),1
        else:self.root,self.length=None,0
    def __str__(self):return str(self.inOrder())
    def __len__(self):return self.length
    __repr__ = __str__
    def add(self,key,value):
        if self.root:self.root,self.length=self.addNode(key,value,self.root),self.length+1
        else:self.length,self.root=1,Node(key,value)
    def addNode(self,key,value,root):
        if root.key>key:
            if root.left:self.addNode(key,value,root.left)
            else:root.left=Node(key,value)
        elif root.key<key:
            if root.right:self.addNode(key,value,root.right)
            else:root.right=Node(key,value)
        return root
    def search(self,key):return self.searchNode(key,self.root)
    def searchNode(self,key,root):
        if root.key==key:return root.val
        elif root.key>key:return self.searchNode(key,root.left)
        elif root.key<key:return self.searchNode(key,root.right)
    def delete(self,key):
        newroot,val=self.delNode(key,self.root)
        if newroot is not 0:self.length,self.root=self.length-1,newroot
        return val
    def delNode(self,key,root):
        if root:
            if root.key>key:self.left,val=self.delNode(key,root.left)
            elif root.key<key:self.right,val=self.delNode(key,root.right)
            else:
                if root.left is None:return root.left,root.val
                elif root.right is None:return None,root.val
                else:
                    succ=root.right
                    while succ.left: succ=succ.left
                    root.key,root.val=succ.key,succ.val
                    self.delNode(succ.key,succ.right)
                    return root,root.val
            return root,val
        return 0,None
    def inOrder(self):
        def _inOrderGen(root):
            if root.left: yield from _inOrderGen(root.left)
            yield root
            if root.right: yield from _inOrderGen(root.right)
        return list(_inOrderGen(self.root)) if self.root else None
