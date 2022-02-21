class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def subtree(root, sub_root):
    if not root:
        return False
    
    def compare(node, sub_node):
        if not node and not sub_node:
            return True
        if not node or not sub_node:
            return False
        return node.val == sub_node.val and compare(node.left, sub_node.left) and compare(node.right, sub_node.right)



    left = subtree(root.left, sub_root)
    right = subtree(root.right, sub_root)
    return left or right or compare(root, sub_root)


root = TreeNode(3)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(5)

root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(2)
root2.left.right.left = TreeNode(0)
root2.right = TreeNode(5)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print("Is the Subtree [4,1,2] in Tree [3,4,5,1,2]:    {}".format(subtree(root, subRoot)))
print("Is the Subtree [4,1,2] in Tree [3,4,5,1,2, null, null, null, null, 0]:    {}".format(subtree(root2, subRoot)))
