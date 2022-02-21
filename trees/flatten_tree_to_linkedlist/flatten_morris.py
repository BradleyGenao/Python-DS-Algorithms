class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten_tree(root):
    if not root:
        return None
    node = root
    while node:
        if node.left:
            right_most = node.left
            while right_most.right:
                right_most = right_most.right
            right_most.right = node.right
            node.right = node.left
            node.left = None
        node = node.right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)

root.right.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
flatten_tree(root)

while root:
    print(root.val)
    root = root.right
