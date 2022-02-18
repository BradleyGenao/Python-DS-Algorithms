class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(2)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

def min_depth(node):
    if not node:
        return 0
    if not node.right:
        return min_depth(node.left) + 1
    if not node.left:
        return min_depth(node.right) + 1
    return min(min_depth(node.left), min_depth(node.right)) + 1
print(min_depth(root))
