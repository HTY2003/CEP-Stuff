from splaytree import SplayBST, Node

class TitleBST(SplayBST):
    '''
Functionally the same as the SplayBST, except that duplicate keys are not handled by appending new values to a list,
but overwrite the existing values instead. This is because the keys used are unique, specific movie titles, so it would be
more logical and useful for duplicates to update values, not append them.
    '''
    def search(self, key):
        node = self._searchNode(self.root, key)
        self.root = self._splayNode(self.root, node)
        categorizer = lambda x, k: [k] + list(zip(['score', 'rating', 'genre', 'box office', 'running time'], x))
        return categorizer(node.val, key)

    def _addNode(self, root, key, value):
        '''
        Function that inserts a new node into the tree if a new key is specified, and updates value if an existing key is given
        The position is determined by the key (left if it is less than a node, right if it is more than a node)

        NOTE: This differs from the SplayBST in that duplicate keys overwrite existing values.
        '''
        def _insert(root, node):
            #updates value if new value is given
            if root.key == node.key:
                root.val = node.val
                return root
            #when key is more than node's key, inserts node if right of node is empty, continues moving right otherwise
            if root.key < node.key:
                if root.right is None: root.right = node
                else: return _insert(root.right, node)
                #when key is less than node's key, inserts node if left of node is empty, continues moving left otherwise
            else:
                if root.left is None: root.left = node
                else: return _insert(root.left, node)
            self.length += 1
            #return newly inserted node to be splayed later on
            return node
        return _insert(root, Node(key, value))

class BoxOfficeBST(SplayBST):
    '''
Splay tree with print by score function added for task 4, 5 & 6.
Not added to the splay tree ADT to maintain versatility of the original ADT.
    '''
    def bocount(self, max):
        count = 0
        for node in self._inOrderGen(self.root):
            if node.key < max: count += 1
        return count

    def boprint(self, min, max):
        for node in self._inOrderGen(self.root):
            if node.key > min and node.key < max: print(node) #note: min and max are included in the printed list

    def highestboprint(self):
        def findRightMost(root):
            if root.right is not None: return findRightMost(root.right)
            else: return root
        print(findRightMost(self.root))

class ScoreBST(SplayBST):
    '''
Splay tree with print by score function added for task 7 & 8.
Not added to the splay tree ADT to maintain versatility of the original ADT.
    '''
    def scoreprint(self, min=-1, max=101):
        for node in self._inOrderGen(self.root):
            if node.key > min and node.key < max: print(node) #note: min and max are not included in the printed list
