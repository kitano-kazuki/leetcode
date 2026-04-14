from dataclasses import dataclass

# 1st: 1:05:01
# 2nd: 0:53:00


@dataclass
class TreeVertex:
    tree_index: int
    left: int
    right: int

    def get_children(self):
        if self.left == self.right:
            return None
        mid = (self.left + self.right) // 2
        return TreeVertex(2 * self.tree_index, self.left, mid), TreeVertex(2 * self.tree_index + 1, mid + 1, self.right)

    def contains(self, index) -> bool:
        return self.left <= index <= self.right


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n * 4)

    
    def update(self, target_index: int, new_value: int):

        def update_helper(vertex: TreeVertex, target_index: int, new_value: int):
            children = vertex.get_children()

            if children is None:
                if vertex.left != target_index:
                    assert False, "unreachable"
                self.data[vertex.tree_index] = new_value
                return

            left_child, right_child = children
            if left_child.contains(target_index):
                update_helper(left_child, target_index, new_value)
            else:
                update_helper(right_child, target_index, new_value)
            self.data[vertex.tree_index] = max(self.data[left_child.tree_index], self.data[right_child.tree_index])
            return
        
        update_helper(TreeVertex(1, 0, self.n - 1), target_index, new_value)
        return


    def get_max(self, left: int, right: int) -> int:

        def get_max_helper(vertex: TreeVertex, left: int, right: int) -> int:
            if left > right:
                return float("-inf")

            children = vertex.get_children()
            if children is None:
                if vertex.left != left:
                    assert False, "unreachable"
                return self.data[vertex.tree_index]
            
            left_child, right_child = children
            left_max = get_max_helper(left_child, left, min(left_child.right, right))
            right_max = get_max_helper(right_child, max(right_child.left, left), right)
            return max(left_max, right_max)

        return get_max_helper(TreeVertex(1, 0, self.n - 1), left, right)
            


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        num_to_rank = {num : i + 1 for i, num in enumerate(sorted(set(nums)))}
        ranks = list(map(lambda num: num_to_rank[num], nums))

        segment_tree = SegmentTree(len(ranks) + 1)
        length_of_LIS = float("-inf")
        for rank in ranks:
            maximum_length = segment_tree.get_max(0, rank - 1)
            segment_tree.update(rank, maximum_length + 1)
            length_of_LIS = max(length_of_LIS, maximum_length + 1)
        
        return length_of_LIS

solution = Solution()
print(solution.lengthOfLIS([-10000]))