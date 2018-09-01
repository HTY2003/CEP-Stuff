from splaytree import SplayBST, Node
from dyarray import DyArray
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
        '''Edited to have O(log n) completion time'''
        def boloop(root, max, count=0):
            if root:
                if root.key < max: count = boloop(root.right, max, (count + 1)if type(root.val)!=DyArray else(count+len(root.val)))
                count = boloop(root.left, max, count)
            return count
        return boloop(self.root, max)

    def boprint(self, min, max):
        '''Edited to have O(log n) completion time'''
        def boloop(root, min, max):
            if root:
                mincheck = root.key > min
                maxcheck = root.key < max
                if mincheck and maxcheck:
                    yield from boloop(root.left, min, max)
                    yield (root.key, root.val)
                    yield from boloop(root.right, min, max)
                elif not maxcheck: yield from boloop(root.left, min, max)
                elif not mincheck: yield from boloop(root.right, min, max)
        for node in boloop(self.root, min, max): print(node) #note: min and max are included in the printed list

    def highestboprint(self):
        def findRightMost(root):
            return findRightMost(root.right) if root.right else root
        print(findRightMost(self.root))

class ScoreBST(SplayBST):
    '''
Splay tree with print by score function added for task 7 & 8.
Not added to the splay tree ADT to maintain versatility of the original ADT.
    '''
    def scoreprint(self, min=-1, max=101):
        '''Edited to have O(log n) completion time'''
        def scoreloop(root, min, max):
            if root:
                mincheck = root.key > min
                maxcheck = root.key < max
                if mincheck and maxcheck:
                    yield from scoreloop(root.left, min, max)
                    yield (root.key, root.val)
                    yield from scoreloop(root.right, min, max)
                elif not maxcheck: yield from scoreloop(root.left, min, max)
                elif not mincheck: yield from scoreloop(root.right, min, max)
        for node in scoreloop(self.root, min, max): print(node) #note: min and max are not included in the printed list
