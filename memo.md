# Step1

## アプローチ

* highed-balancedかどうかを判定する
* 左の高さと右の高さがわかれば少なくとも今注目しているノードに対してはhighed-balancedかどうかを判定できる
* 全てのノードでそれをやればいい
* 再帰でやる
* 右と左の高さを計算したいから, 各再帰での役割は高さを出すことにしたい
* O(N)
* 2:17

## Code1-1

* AC: 10:13

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_balanced_helper(root: TreeNode) -> tuple[int, bool]:
            left_height = 0
            left_balanced = True
            if root.left is not None:
                left_height, left_balanced = is_balanced_helper(root.left)
            
            right_height = 0
            right_balanced = True
            if root.right is not None:
                right_height, right_balanced = is_balanced_helper(root.right)

            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            return max(left_height, right_height) + 1, balanced

        return is_balanced_helper(root)[1]
        
```

# Step2

## Code2-1

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_balanced_helper(root: TreeNode) -> tuple[int, bool]:
            left_height = 0
            left_balanced = True
            if root.left is not None:
                left_height, left_balanced = is_balanced_helper(root.left)
            
            right_height = 0
            right_balanced = True
            if root.right is not None:
                right_height, right_balanced = is_balanced_helper(root.right)

            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            return max(left_height, right_height) + 1, balanced

        return is_balanced_helper(root)[1]
        
```

# Step3

## Code3-1

* 2:44
* 1:29
* 1:00

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced_helper(root: TreeNode | None) -> tuple[int, bool]:
            if root is None:
                return 1, True
            
            left_height, left_balanced = is_balanced_helper(root.left)
            right_height, right_balanced = is_balanced_helper(root.right)

            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return max(left_height, right_height) + 1, balanced
        
        return is_balanced_helper(root)[1]
        
```
