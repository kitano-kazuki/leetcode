# Step1

## アプローチ

* 最小の要素がO(1)でわかるようなstackを実装する
* 各要素を積む時に,最小値もタプルとして含めておくようにする

## Code1-1

* AC: 4:02

```python
import dataclasses


@dataclasses.dataclass
class MinStackElement:
    value: int
    min_value: int

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, value: int) -> None:
        min_value = self.stack[-1].min_value if self.stack else float("inf")
        self.stack.append(MinStackElement(value, min(min_value, value)))


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1].value
        

    def getMin(self) -> int:
        return self.stack[-1].min_value
        
```

# Step2

## Code2-1

* 変更なし

```python
import dataclasses


@dataclasses.dataclass
class MinStackElement:
    value: int
    min_value: int

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, value: int) -> None:
        min_value = self.stack[-1].min_value if self.stack else float("inf")
        self.stack.append(MinStackElement(value, min(min_value, value)))


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1].value
        

    def getMin(self) -> int:
        return self.stack[-1].min_value
        
```

## 他の人のPRを見る

* https://github.com/TaisukeFujise/leetcode_tafujise/pull/21
    * 自前でstack自体も実装
* https://github.com/tom4649/Coding/pull/74
* https://github.com/huyfififi/coding-challenges/pull/38

# Step3

## Code3-1

```python
import dataclasses


@dataclasses.dataclass
class MinStackElement:
    value: int
    min_value: int


class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, value: int) -> None:
        min_value = self.stack[-1].min_value if self.stack else float("inf")
        self.stack.append(MinStackElement(value, min(min_value, value)))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1].value
        

    def getMin(self) -> int:
        return self.stack[-1].min_value
        

```
