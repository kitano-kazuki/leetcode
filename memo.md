# Step1

## アプローチ

* 数字を順番に見ていってリストに内容を保存. リストの後ろを見ながら新しいノードを作成していく
* 前から順番に繋ぎ変えていく.
    * in-placeでも, 別のノードリストを用意してもできる.
* 再帰で実装もできるけど本質的にはやること一緒.

## Code1-1 (別のリストに数字を保存)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        reversed_head_dummy = ListNode()
        reversed_tail = reversed_head_dummy
        for i in range(len(values) - 1, -1, -1):
            node = ListNode(values[i])
            reversed_tail.next = node
            reversed_tail = reversed_tail.next
        return reversed_head_dummy.next
```

## Code1-2 (別のメモリ使用. one path)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        reversed_head = None
        node = head
        while node is not None:
            new_node = ListNode(node.val)
            new_node.next = reversed_head
            reversed_head = new_node
            node = node.next
        return reversed_head
```

## Code1-3 (in-place, one path)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        reversed_head = None
        node = head
        while node is not None:
            next_node = node.next
            node.next = reversed_head
            reversed_head = node
            node = next_node
        return reversed_head
```

# Step2

変更なし

# Step3

## Code1-1 (別のリストに数字を保存)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        values = []
        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        dummy_reverse_head = ListNode()
        reverse_tail = dummy_reverse_head
        for value in values[::-1]:
            new_node = ListNode(value)
            reverse_tail.next = new_node
            reverse_tail = reverse_tail.next
        return dummy_reverse_head.next
```

## Code1-2 (別のメモリ使用. one path)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        reversed_head = None
        node = head
        while node is not None:
            new_node = ListNode(node.val)
            new_node.next = reversed_head
            reversed_head = new_node
            node = node.next
        return reversed_head
```

## Code1-3 (in-place, one path)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        reversed_head = None
        node = head
        while node is not None:
            next_node = node.next
            node.next = reversed_head
            reversed_head = node
            node = next_node
        return reversed_head
```
