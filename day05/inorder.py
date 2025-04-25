class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    helper(root)
    return result

# Build the tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)
root = TreeNode(1, node2, node3)

print("Inorder traversal:", inorder_traversal(root))
# Output: [4, 2, 5, 1, 3]
