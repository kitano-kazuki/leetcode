import copy
import sys
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:

        def split_bst_helper(root: TreeNode | None) -> tuple[TreeNode | None, TreeNode | None]:
            if root is None:
                return None, None
            
            if root.val <= v:
                sub_smaller_root, sub_larger_root = split_bst_helper(root.right)
                root.right = sub_smaller_root
                return [root, sub_larger_root]
            else:
                sub_smaller_root, sub_larger_root = split_bst_helper(root.left)
                root.left = sub_larger_root
                return [sub_smaller_root, root]
        
        return split_bst_helper(copy.deepcopy(root))


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
    solution = Solution() 
    tree_values = list(map(int, sys.argv[1].split(" ")))
    v = int(sys.argv[2])
    root = build_tree(tree_values)
    smaller_root, larger_root = solution.split_b_s_t(root, v)
    print_tree(smaller_root)
    print_tree(larger_root)
