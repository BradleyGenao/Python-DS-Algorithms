class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert(array):
    if not array:
        return None
    
    mid = len(array) // 2
    root = TreeNode(array[mid])
    root.left = convert(array[:mid])
    root.right = convert(array[mid+1:])
    return root
def print_inorder(node):
    if not node:
        return 
    print_inorder(node.left)
    print(node.val)
    print_inorder(node.right)
arr = [-10,-3,0,5,9]
root = convert(arr)
print_inorder(root)

