# Step1

## アプローチ (14:22)

* rootとなる値がわかれば, それより左側と右側で再帰を呼ぶことで解ける
    * rootとなる値は中央値?
    * height-balancedではある
    * rootの左側と右側の個数が等しくなるようにすればbalancedにはなるよな
* 日本語で仕事を考えてみる
    * 与えられた数字の列からrootになる値を決める(自分の仕事)
    * 決めた数字の左側と右側の配列を部下に渡して, 自分が繋ぐべきrootをもらう
    * rootを返す
* 計算量を考える
    * 計算量をT(N)とする
    * T(N) = T(N/2) + T(N/2) = T(N / 2^2) + ... + T(N / 2^2)
    * T(N) = T(1) * 2 * 2^(log2_N)
    * O(N)
        * 追記: slicingを使っていた場合はO(NlogN)になる
* 空間計算量
    * 再帰の最大回数 ... logN
    * 結果として使う分 ... size(TreeNode) * N
    * O(N)

## Code1-1 (Recursion) - 1:49

```python
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        mid_idx = len(nums) // 2
        root_node = TreeNode(nums[mid_idx])
        left_nums = nums[:mid_idx]
        right_nums = nums[mid_idx + 1:]
        root_node.left = self.sortedArrayToBST(left_nums)
        root_node.right = self.sortedArrayToBST(right_nums)
        return root_node

```

# Step2

## 他の人のコード

* https://github.com/mamo3gr/arai60/pull/23/files
    * whileを使用した再帰
    * 区間を指定した再帰関数を作った実装もある

## Code2-1 (Recursion)

```python
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sortedArrayToBST_with_range(nums, left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(nums[left])
            
            mid_idx = (left + right) // 2
            return TreeNode(
                    val=nums[mid_idx], 
                    left=sortedArrayToBST_with_range(nums, left, mid_idx - 1),
                    right=sortedArrayToBST_with_range(nums, mid_idx + 1, right)
                )
            
        return sortedArrayToBST_with_range(nums, 0, len(nums) - 1)


```

## Code2-2 (DFS)

```python
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        frontier = [(0, len(nums) - 1, root)]
        while frontier:
            left, right, node = frontier.pop()
            mid = (left + right) // 2
            node.val = nums[mid]
            if left <= mid - 1:
                node.left = TreeNode()
                frontier.append((left, mid - 1, node.left))
            if mid + 1 <= right:
                node.right = TreeNode()
                frontier.append((mid + 1, right, node.right))
        return root

```

# Step3

## Code3-1 (Recursion)

```python
# 1st: 1:41
# 1st: 1:19
# 1st: 1:12


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def sortedArrayToBST_with_range(nums, left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(nums[left])
            
            mid = (left + right) // 2
            return TreeNode(
                val=nums[mid],
                left=sortedArrayToBST_with_range(nums, left, mid - 1),
                right=sortedArrayToBST_with_range(nums, mid + 1, right)
            )
        return sortedArrayToBST_with_range(nums, 0, len(nums) - 1)

```

## Code3-2 (DFS)

```python
# 1st: 1:55
# 1st: 1:41
# 1st: 1:25

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        root = TreeNode()
        frontier = [(0, len(nums) - 1, root)]
        while frontier:
            left, right, node = frontier.pop()
            mid = (left + right) // 2
            node.val = nums[mid]
            if left <= mid - 1:
                node.left = TreeNode()
                frontier.append((left, mid - 1, node.left))
            if mid + 1 <= right:
                node.right = TreeNode()
                frontier.append((mid + 1, right, node.right))
            
        return root

```