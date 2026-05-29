# Step1

## アプローチ

* 二つのstackを使ってqueueを再現する
* 1つ目のstackに積んでいく
* 取り出す時は, 一つ目のstackの要素をすべて二つ目のstackに移動
    * 一番古い要素が一番上に来るようになる
* 新しい要素は（現在空空なっている）１つ目のstackに入れる
* 二つ目のstackが空になったら, 再び1つ目のstackから2つ目のstackに全てを移動させる
* アクセスの最初はO(N)
* 以降は取り出した後に追加された要素数をMとするとN個の要素を取り出した後の最初の取り出しでO(M)かかる

## Code1-1

* AC: 9:35
* follow-upの要件`amortized O(1) time complexity`も自然と満たしていた

```python
class MyQueue:

    def __init__(self):
        self.store = []
        self.retrievable = []

    def _fill_retrievable(self):
        while self.store:
            self.retrievable.append(self.store.pop())
        return

    def push(self, x: int) -> None:
        self.store.append(x)
        return

    def pop(self) -> int:
        if self.retrievable:
            return self.retrievable.pop()
        self._fill_retrievable()
        return self.retrievable.pop()

    def peek(self) -> int:
        if self.retrievable:
            return self.retrievable[-1]
        self._fill_retrievable()
        return self.retrievable[-1]

    def empty(self) -> bool:
        return (not self.store) and (not self.retrievable)

```

# Step2

## Code2-1

* 変更なし

```python
class MyQueue:

    def __init__(self):
        self.store = []
        self.retrievable = []

    def _fill_retrievable(self):
        while self.store:
            self.retrievable.append(self.store.pop())
        return

    def push(self, x: int) -> None:
        self.store.append(x)
        return

    def pop(self) -> int:
        if self.retrievable:
            return self.retrievable.pop()
        self._fill_retrievable()
        return self.retrievable.pop()

    def peek(self) -> int:
        if self.retrievable:
            return self.retrievable[-1]
        self._fill_retrievable()
        return self.retrievable[-1]

    def empty(self) -> bool:
        return (not self.store) and (not self.retrievable)

```

# Step3

## Code3-1

* 2:14
* 1:29
* 1:16

```python
class MyQueue:

    def __init__(self):
        self.store = []
        self.retrievable = []


    def _fill_retrievable(self):
        if self.retrievable:
            return
        while self.store:
            self.retrievable.append(self.store.pop())
        return
        

    def push(self, x: int) -> None:
        self.store.append(x)
        return
        

    def pop(self) -> int:
        self._fill_retrievable()
        return self.retrievable.pop()
        

    def peek(self) -> int:
        self._fill_retrievable()
        return self.retrievable[-1]
        

    def empty(self) -> bool:
        return (not self.store) and (not self.retrievable)
        

```
