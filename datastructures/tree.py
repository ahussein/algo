class Tree(object):
    """
    Tree Structure
    """
    def __init__(self, root=None):
        self._root = None
        self._size = 0
        if root is not None:
            self.add(root)

    def add(self, node):
        """
        Adds new node to the tree
        """
        if self._root is None:
            self._root = node
            self._size += 1
        else:
            self._add(self._root, node)

    def _add(self, root, node):
        if node.data < root.data:
            if root._left is None:
                root._left = node
                self._size += 1
            else:
                self._add(root._left, node)
        elif node.data > root.data:
            if root._right is None:
                root._right = node
                self._size += 1
            else:
                self._add(root._right, node)

    def dfs(self):
        """
        Traverse tree in depth first matter
        """
        self._dfs(self._root)

    def _dfs(self, node):
        if node is None:
            return
        self._dfs(node._left)
        node.visit()
        self._dfs(node._right)

    def get_height(self):
        """
        Calculate the height of the tree
        """
        return self._get_height(self._root)

    def _get_height(self, node):
        # import pdb; pdb.set_trace()
        if node is None:
            return 0
        if node.is_leaf():
            return 1
        left_height = self._get_height(node._left)
        right_height = self._get_height(node._right)
        return max(left_height, right_height) + 1


    @property
    def root(self):
        return self._root



class BinaryNode(object):
    """
    Binary Tree Node
    """
    def __init__(self, data):
        self.data = data
        self._left = None
        self._right = None

    def visit(self):
        """
        Visit node
        """
        print(self.data)


    def is_leaf(self):
        """
        Check if a node is a leaf node or not
        """
        return False if (self._right or self._left) else True


    def get_childrens(self):
        """
        Return list of children of this node
        """
        return [self._left, self._right]


"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
"""
def create_min_tree(data):
    # import pdb; pdb.set_trace()
    size = len(data)
    mid = size / 2
    i = mid - 1
    j = mid + 1
    tree = Tree()
    root = BinaryNode(data[mid])
    tree.add(root)
    while i >= 0:
        tree.add(BinaryNode(data[i]))
        i -= 1
    while j < size:
        tree.add(BinaryNode(data[j]))
        j += 1
    return tree


"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).
"""
def get_depth_list(root):
    from Queue import Queue
    result = []
    queue = Queue()
    result.append([root.data ])
    sublist = []
    queue.put(root)
    height_map = {root: 0}
    current_level = 1
    while not queue.empty():
        item = queue.get()
        if height_map[item] != current_level and item.data != root.data:
            result.append(sublist)
            sublist = [item.data]
            current_level += 1
        elif item.data != root.data:
            sublist.append(item.data)

        for child in item.get_childrens():
            if child is not None:
                queue.put(child)
                height_map[child] = height_map[item] + 1

    result.append(sublist)
    return result


"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""
def check_balanced(root):
    # import pdb; pdb.set_trace()
    if root is None or root.is_leaf():
        return 0
    left_height = check_balanced(root._left)
    right_height = check_balanced(root._right)
    # import pdb; pdb.set_trace()
    if left_height is False or  right_height is False:
        return False
    if abs(left_height - right_height) > 1:
        return False

    return max(left_height, right_height) + 1


"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""
def validate_bst(root):
    if root is None or root.is_leaf():
        return True

    left_result = validate_bst(root._left)
    right_result = validate_bst(root._right)
    if left_result is False or right_result is False:
        return False
    if root._left is None and root._right.data < root.data:
        return False
    elif root._right.data > root.data:
        return True
    if root._right is None and root._left.data > root.data:
        return False
    elif root._left.data < root.data:
        return True
    if root._left.data < root.data and root._right.data > root.data:
        return True



if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        data = open(sys.argv[1], 'r').read()
    else:
        data = 'hello aa man test ally'
        data = 'd a b c d e f  g h'
    tree = Tree()
    for item in data.split(' '):
        node = BinaryNode(item)
        tree.add(node)

    tree.dfs()
    print('Tree Height is: %s and Tree size is: %s' % (tree.get_height(), tree._size))

    # test for min tree
    data = range(10)
    tree = create_min_tree(data)
    tree.dfs()
    tree2 = Tree()
    for item in data:
        tree2.add(BinaryNode(item))
    print('Min height tree has height: %s while normal tree has height: %s' %(tree.get_height(), tree2.get_height()))

    # test for depth list
    data = range(10)
    tree = create_min_tree(data)
    print(get_depth_list(tree.root))

    # test for balanced check
    data = [100, 80, 200, 20, 90]
    tree = Tree()
    for item in data:
        tree.add(BinaryNode(item))
    print('Tree tree is %s' % ('balanced' if check_balanced(tree.root) is not False else 'not balanced'))
    print('Tree tree2 is %s' % ('balanced' if check_balanced(tree2.root) is not False else 'not balanced'))

    # test check BST
    print('Tree tree is %sBST' % ('' if validate_bst(tree.root) else 'not '))
