class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      sorted_nums = sorted(nums, reverse=True)
      self.topk_nums = sorted_nums[:k]
      self.k = k
        

    def add(self, val: int) -> int:
      if len(self.topk_nums) < self.k - 1:
        raise ValueError("missing number of elements during initialization")
      if len(self.topk_nums) == self.k and val <= self.topk_nums[-1]:
        return self.topk_nums[-1]
      should_check_mte = 0
      should_check_lte =  len(self.topk_nums) - 1
      while should_check_mte <= should_check_lte:
        check_idx = should_check_lte + (should_check_mte - should_check_lte) // 2
        if self.topk_nums[check_idx] >= val:
          should_check_mte = check_idx + 1
        else:
          should_check_lte = check_idx - 1
      insert_idx = should_check_mte
      self.topk_nums.insert(insert_idx, val)
      if len(self.topk_nums) > self.k:
        self.topk_nums.pop()
      return self.topk_nums[-1]
