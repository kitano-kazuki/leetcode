# 1st: 1:05:01

from dataclasses import dataclass

@dataclass
class SegmentTreeVertex:
    index: int
    left: int
    right: int

    def get_left_child(self):
        if self.left == self.right:
            return None
        return SegmentTreeVertex(self.index * 2, self.left, (self.left + self.right) // 2)
    
    def get_right_child(self):
        if self.left == self.right:
            return None
        return SegmentTreeVertex(self.index * 2 + 1, (self.left + self.right) // 2 + 1, self.right)

    def contains(self, position):
        return self.left <= position <= self.right

class SegmentTreeMax:
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size * 4)
    

    def update(self, position: int, new_value: int) -> None:

        def update_helper(vertex: SegmentTreeVertex, position: int, new_value: int) -> None:
            if vertex.left == position and vertex.right == position:
                self.data[vertex.index] = new_value
                return
            left_vertex = vertex.get_left_child()
            right_vertex = vertex.get_right_child()
            if left_vertex.contains(position):
                update_helper(left_vertex, position, new_value)
            elif right_vertex.contains(position):
                update_helper(right_vertex, position, new_value)
            else:
                raise ValueError()
            self.data[vertex.index] = max(self.data[left_vertex.index], self.data[right_vertex.index])
            return

        update_helper(SegmentTreeVertex(1, 0, self.size - 1), position, new_value)
        return

        
    def get_max(self, left: int, right: int) -> int:

        def get_max_helper(vertex: SegmentTreeVertex, left, right) -> int:
            if vertex.right < left or right < vertex.left:
                return float("-inf")
            if vertex.left == left and vertex.right == right:
                return self.data[vertex.index]

            left_vertex = vertex.get_left_child()
            right_vertex = vertex.get_right_child()
            return max(get_max_helper(left_vertex, left, min(left_vertex.right, right)), get_max_helper(right_vertex, max(right_vertex.left, left), right))

        return get_max_helper(SegmentTreeVertex(1, 0, self.size - 1), left, right)



class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        num_to_rank = {num : i + 1 for i, num in enumerate(sorted(set(nums)))}
        num_ranks = list(map(lambda num : num_to_rank[num], nums))

        segment_tree = SegmentTreeMax(len(num_ranks) + 1)

        length_of_LIS = float("-inf")
        for rank in num_ranks:
            # maximum length of increasing subsequence ending with x (< rank)
            max_length = segment_tree.get_max(0, rank - 1)
            segment_tree.update(rank, max_length + 1)
            length_of_LIS = max(length_of_LIS, max_length + 1)
        
        return length_of_LIS
            
            
nums = [10,9,2,5,3,7,101,18]
solution = Solution()
solution.lengthOfLIS(nums)