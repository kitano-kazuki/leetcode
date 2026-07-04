# Step1

## アプローチ

* 2回目に出てくるものがあったら、True, 全部uniqueだったらFalse
* set()に保存しておけばいい

## Code1-1

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        
```

# Step2

## Code2-1

* 変更なし

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        
```

# Step3

## Code3-1

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

```
