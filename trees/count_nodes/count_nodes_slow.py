class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root):
    count = [0]
   
    def dfs(node):
        if not node:
            return 
        count[0] +=1
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return count[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

print(count_nodes(root))
