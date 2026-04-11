from dataclasses import dataclass


@dataclass
class SegmentTreeVertex:
    index: int
    left_inclusive: int
    right_inclusive: int



# SegmentTree for getting maximum value between given left and right.
class SegmentTreeMax:
    def __init__(self, size):
        self.size = size
        self.tree = [None] * (size * 4) # 1-indexed
    
    def build(self, array):
        self._build(array, SegmentTreeVertex(1, 0, self.size - 1))

    def _build(self, array, vertex: SegmentTreeVertex):
        if vertex.left_inclusive == vertex.right_inclusive:
            self.tree[vertex.index] = array[vertex.left_inclusive]
            return

        mid = (vertex.left_inclusive + vertex.right_inclusive) // 2
        left_child = SegmentTreeVertex(vertex.index * 2, vertex.left_inclusive, mid)
        self._build(array, left_child)
        right_child = SegmentTreeVertex(vertex.index * 2 + 1, mid + 1, vertex.right_inclusive)
        self._build(array, right_child)
        self.tree[vertex.index] = max(self.tree[left_child.index], self.tree[right_child.index])
        return

    def get_max(self, query_left_inclusive: int, query_right_inclusive: int) -> int:
        return self._get_max(SegmentTreeVertex(1, 0, self.size - 1), query_left_inclusive, query_right_inclusive)
    
    def _get_max(self, queried_vertex: SegmentTreeVertex, query_left_inclusive: int, query_right_inclusive: int) -> int:
        if query_left_inclusive > query_right_inclusive:
            return 0
        if query_left_inclusive == queried_vertex.left_inclusive and query_right_inclusive == queried_vertex.right_inclusive:
            return self.tree[queried_vertex.index]
        mid = (queried_vertex.left_inclusive + queried_vertex.right_inclusive) // 2
        left_child = SegmentTreeVertex(queried_vertex.index * 2, queried_vertex.left_inclusive, mid)
        right_child = SegmentTreeVertex(queried_vertex.index * 2 + 1, mid + 1, queried_vertex.right_inclusive)
        return max(self._get_max(left_child, query_left_inclusive, min(mid, query_right_inclusive)), self._get_max(right_child, max(query_left_inclusive, mid + 1), query_right_inclusive))

        
    def update(self, position: int, new_value: int) -> None:
        self._update(SegmentTreeVertex(1, 0, self.size - 1), position, new_value)
        return

    def _update(self, vertex: SegmentTreeVertex, position: int, new_value: int):
        if vertex.left_inclusive == vertex.right_inclusive:
            self.tree[vertex.index] = new_value
            return

        mid = (vertex.left_inclusive + vertex.right_inclusive) // 2
        left_child = SegmentTreeVertex(vertex.index * 2, vertex.left_inclusive, mid)
        right_child = SegmentTreeVertex(vertex.index * 2 + 1, mid + 1, vertex.right_inclusive)
        if position <= mid:
            self._update(left_child, position, new_value)
        else:
            self._update(right_child, position, new_value)
        self.tree[vertex.index] = max(self.tree[left_child.index], self.tree[right_child.index])
        return



class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ranks = self._convert_array_to_ranks(nums)

        # ith element represents the maximum LIS length ending at i(rank)
        maximum_LIS_lengthes = [0] * (len(set(ranks)) + 1)
        n = len(maximum_LIS_lengthes)

        segment_tree = SegmentTreeMax(n)
        segment_tree.build(maximum_LIS_lengthes)

        for rank in ranks:
            # the maximum LIS length ending at x(< rank)
            maximum_length_before = segment_tree.get_max(0, rank - 1)
            maximum_LIS_lengthes[rank] = maximum_length_before + 1
            segment_tree.update(rank, maximum_LIS_lengthes[rank])
        
        return max(maximum_LIS_lengthes)



    def _convert_array_to_ranks(self, array: list[int]) -> list[int]:
        unique_numbers = sorted(set(array))
        value_to_rank = {}
        rank = 1
        for unique_number in unique_numbers:
            value_to_rank[unique_number] = rank
            rank += 1
        return [value_to_rank[num] for num in array]