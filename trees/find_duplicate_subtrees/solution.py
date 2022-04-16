from collections import defaultdict

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_duplicate_subtrees(root):
    tree_hash = defaultdict(list)

    def hash_tree(node):
         if not node:
              return 'None'
         
         key = "{} {} {}".format(node.value, hash_tree(node.left), hash_tree(node.right))
         tree_hash[key].append(node)
         return key
    dups = []
    hash_tree(root)
    for tree in tree_hash.values():
        if len(tree) > 1:
            dups.append(tree[0])
    return dups
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left =TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)

print(find_duplicate_subtrees(root))
