class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self):
        self.root = None

    def same_tree(self, p, q):

        if p is None and q is None:
            return True
        if p is None or q is None or p.val!=q.val:
            return False
        if p.val == q.val:
            return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)
        return False

    def is_same_tree(self, tree1, tree2):
        return self.same_tree(tree1.root, tree2.root)

tree1 = BinaryTree()
tree1.root = TreeNode(1)
tree1.root.left = TreeNode(2)
tree1.root.right = TreeNode(3)
tree1.root.right.right=TreeNode(5)

tree2 = BinaryTree()
tree2.root = TreeNode(1)
tree2.root.left = TreeNode(2)
tree2.root.right = TreeNode(3)
tree2.root.right.right=TreeNode(5)

tree3 = BinaryTree()
tree3.root = TreeNode(1)
tree3.root.left = TreeNode(2)
tree3.root.right = TreeNode(4)
tree3.root.right.right=TreeNode(5)


print(tree1.is_same_tree(tree1, tree2))
print(tree1.is_same_tree(tree1, tree3))  