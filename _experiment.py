import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
node = TreeNode()
print(sys.getsizeof(node))  # 48
print(sys.getsizeof(node.__dict__)) # 296