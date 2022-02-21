class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math
def validate_tree(root):
    if not root:
        return False
    
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
       
        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
       
    return validate(root, -math.inf, math.inf) 

root = TreeNode(2)
root.right = TreeNode(3)
root.left = TreeNode(1)

print(validate_tree(root))
