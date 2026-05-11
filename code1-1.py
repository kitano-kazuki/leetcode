import copy
import collections
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:

        # vより大きい二分探索木
        copied_root1 = copy.deepcopy(root)
        larger_tree = self._delete_less_than_or_equal(copied_root1, v)

        # v以下の二分探索木
        copied_root2 = copy.deepcopy(root)
        smaller_tree = self._delete_more_than(copied_root2, v)

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

        


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values:
        return None

    if values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = collections.deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def print_tree(root: TreeNode | None, indent: str = "", is_left: bool = True) -> None:
    if root is None:
        return

    print_tree(root.right, indent + ("│   " if is_left else "    "), False)
    print(indent + ("└── " if is_left else "┌── ") + str(root.val))
    print_tree(root.left, indent + ("    " if is_left else "│   "), True)

if __name__ == "__main__":
    input_array = list(map(int, sys.argv[1].split(" ")))
    v = int(sys.argv[2])
    root = build_tree(input_array)
    solution = Solution()
    print_tree(solution.split_b_s_t(root, v))

    