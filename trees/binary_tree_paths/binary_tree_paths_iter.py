class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def paths(root):
    if not root:
        return []
    paths = []
    stack = [(root, '')]
    while stack:
        node, str_path = stack.pop() 
        if node:
            str_path += str(node.val)
            if node.left:
                stack.append((node.left, str_path + '->'))
            if node.right:
                stack.append((node.right, str_path + '->'))
            if not node.left and not node.right:   
                paths.append(str_path)
      

    return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5) 
root.right = TreeNode(3)
print("Tree Paths for tree [1,2,3,null,5] = {}".format(paths(root))) 
