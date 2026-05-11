import copy

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:

        larger_tree = self._delete_less_than_or_equal(copy.deepcopy(root), v)
        smaller_tree = self._delete_more_than(copy.deepcopy(root), v)

        if self._count_num_nodes(larger_tree) >= self._count_num_nodes(smaller_tree):
            return larger_tree
        else:
            return smaller_tree

    def _delete_less_than_or_equal(self, root: TreeNode | None, v: int) -> TreeNode | None:
        if root is None:
            return None

        if root.val > v:
            root.left = self._delete_less_than_or_equal(root.left, v)
            return root
        
        return self._delete_less_than_or_equal(root.right, v)

    def _delete_more_than(self, root: TreeNode | None, v: int) -> TreeNode | None:
        if root is None:
            return None

        if root.val <= v:
            root.right = self._delete_more_than(root.right, v)
            return root
        
        return self._delete_more_than(root.left, v)
        
    def _count_num_nodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        return 1 + self._count_num_nodes(root.left) + self._count_num_nodes(root.right)

