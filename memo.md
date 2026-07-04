# Step1

## アプローチ

* linkedlistの真ん中のノードをしりたい
* 一番単純な方法は,最初にサイズを確認して
* 次に, 半分のサイズのところまで先頭から辿り直す
* fast, slowのポインタを用意してやることもできそう
* fastが到達した時にslowはだいたい真ん中にあるはずだ
* 今回は真ん中に該当するのが二つあるときには, 二つ目の要素を返したい
* fastは1, 3, 5, 7...のノードに到達する
* fast.next is Noneのときは, ノードの個数は奇数
* slowの今いる位置が真ん中
* fast.next is not Noneだけど, fast.next.next is Noneのとき
* ノードの終わりが, 偶数個めのノード

## Code1-1 (fast and slow)

* AC: 1:05

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next is not None:
            slow = slow.next
        
        return slow
        
```

## Code1-2 (count nodes)

* AC: 3:21

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_nodes = 0
        node = head
        while node is not None:
            num_nodes += 1
            node = node.next

        target = num_nodes // 2  + 1

        node_count = 0
        node = head
        while node is not None:
            node_count += 1
            if node_count == target:
                return node
            node = node.next
        
```

# Step2

## Code2-1 (fast and slow)

* 変更なし

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next is not None:
            slow = slow.next
        
        return slow
        
```

## Code1-2 (count nodes)

* 制約的に大丈夫だが, head is Noneのときに想定外の挙動をするので, ifを追加

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        num_nodes = 0
        node = head
        while node is not None:
            num_nodes += 1
            node = node.next

        half = num_nodes // 2  + 1

        node_count = 0
        node = head
        while node is not None:
            node_count += 1
            if node_count == half:
                return node
            node = node.next
        
        raise ValueError("something went wrong")
        
```

## 他の人のPRをみる

* https://github.com/tom4649/Coding/pull/68
    * whileの条件は`fast is not None`と`fast.next is not None`の方が主役が`fast`であるから自然だな
    * hashmapで`position`から`node`を得られるようにする方法は思いつかなかった
* https://github.com/huyfififi/coding-challenges/pull/22
    * 自分の`Code*-2`で, move_count分`for`を回してnodeを動かす方法の方が読みやすそう

# Step3

## Code3-1

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
       
```
