class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def paths(root):
    if not root:
        return []
    paths = []
    
    def get_path(node, str_path):
        if not node:
            return 
        str_path += str(node.val)
        if node.left:
            get_path(node.left, str_path + '->')
        if node.right:
            get_path(node.right, str_path + '->')
        if not node.left and not node.right:
            paths.append(str_path)
    get_path(root, '')
    return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5) 
root.right = TreeNode(3)
print("Tree Paths for tree [1,2,3,null,5] = {}".format(paths(root))) 
