class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        node = root
        frontier = [(node, 1)]
        maximum_depth = 0
        while frontier:
            node, depth = frontier.pop()
            maximum_depth = max(maximum_depth, depth)
            if node.left is not None:
                frontier.append((node.left, depth + 1))
            if node.right is not None:
                frontier.append((node.right, depth + 1))
        
        return maximum_depth
            
