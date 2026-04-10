import dataclasses


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


@dataclasses.dataclass
class Range:
    left_index_inclusive: int
    right_index_inclusive: int

    def contains_in_range(self, index: int) -> bool:
        return self.left_index_inclusive <= index <= self.right_index_inclusive

    def get_range_right(self) -> int:
        return self.right_index_inclusive
    
    def get_range_left(self) -> int:
        return self.left_index_inclusive


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        if len(preorder) != len(inorder):
            return None

        node_value_to_inorder_index = {}
        for i in range(len(inorder)):
            node_value_to_inorder_index[inorder[i]] = i

        dummy = TreeNode()

        # stores 
        # 1.nodes which may have child nodes, 
        # 2.index ranges in inorder-array where left child value exist, 
        # 3.index ranges in inorder-array where right child value exist
        INVALID_RANGE = Range(-1, -1)
        stack = [(dummy, Range(0, len(inorder) - 1), INVALID_RANGE)]

        preorder_index = 0
        while preorder_index < len(preorder):
            node_value = preorder[preorder_index]
            parent_node, left_child_range, right_child_range = stack[-1]
            node_value_index_in_inorder = node_value_to_inorder_index[node_value]
            is_left_child = left_child_range.contains_in_range(node_value_index_in_inorder)
            is_right_child = right_child_range.contains_in_range(node_value_index_in_inorder)
            if not is_left_child and not is_right_child:
                stack.pop()
                continue
            node = TreeNode(node_value)
            if is_left_child:
                parent_node.left = node
                stack.append((node, 
                             Range(left_child_range.get_range_left(), node_value_index_in_inorder - 1),
                             Range(node_value_index_in_inorder + 1, left_child_range.get_range_right())))
                preorder_index += 1
                continue
            if is_right_child:
                parent_node.right = node
                stack.append((node, 
                             Range(right_child_range.get_range_left(), node_value_index_in_inorder - 1),
                             Range(node_value_index_in_inorder + 1, right_child_range.get_range_right())))
                preorder_index += 1
                continue

        return dummy.left