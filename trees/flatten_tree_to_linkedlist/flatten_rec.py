class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten_tree(root):
    if not root:
        return None
    prev = [None]
    def flatten(node):
        if not node:
            return 
        flatten(node.right)
        flatten(node.left)
   
        node.right = prev[0] 
        node.left = None
        prev[0] = node
       
    flatten(root)


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
