class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_height(node):
    if not node:
        return 0
    return get_height(node.left) + 1

def count(node):
    height = get_height(node)
    if height == 0:
        return 0
    if (height -1) == get_height(node.right):
        return 2 ** (height-1) + count(node.right)
    else:
        return 2 ** (height-2) + count(node.left)


def count_nodes(root):
    if not root:
        return 0
    return count(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

print(count_nodes(root))
