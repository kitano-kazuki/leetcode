from dataclasses import dataclass


@dataclass
class IncreasingSequence:
    tail_value: int
    length: int


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        increasing_subsequences = []

        for num in nums:
            longest_tail_length = 1
            for increasing_subsequence in increasing_subsequences:
                if increasing_subsequence.tail_value < num:
                    longest_tail_length = max(longest_tail_length, increasing_subsequence.length + 1)
            increasing_subsequences.append(IncreasingSequence(num, longest_tail_length))

        return max([sequence.length for sequence in increasing_subsequences])