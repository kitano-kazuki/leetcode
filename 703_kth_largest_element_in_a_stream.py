from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)
        result = self.nums[self.k - 1]
        return result



# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
param = obj.add(3)
print(param)
param = obj.add(5)
print(param)
param = obj.add(10)
print(param)
param = obj.add(9)
print(param)
param = obj.add(4)
print(param)
