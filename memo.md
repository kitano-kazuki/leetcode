# Step1

## アプローチ

* 末尾の要素にすぐアクセスしたいし, 先頭にすぐ持っていきたい
* LinkedListとして保存
* 双方向にlinkを作っておく
* キーに対応するLinkedListNodeを作っておく
* 2:37

## Code1-1

* AC: 16:30

```python

class Node:
    def __init__(self, value = None, key = None, next_node = None, previous_node = None):
        self.value = value
        self.key = key
        self.next_node = next_node
        self.previous_node = previous_node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.key_to_node = {}

        self.head = Node()
        self.tail =  Node()
        self.head.next_node = self.tail
        self.tail.previous_node = self.head


    def _delete_relation(self, node) -> None:
        previous_node = node.previous_node
        next_node = node.next_node

        previous_node.next_node = next_node
        next_node.previous_node = previous_node
        return

    def _add_head_relation(self, node) -> None:
        original_first_node = self.head.next_node

        self.head.next_node = node
        node.previous_node = self.head

        node.next_node = original_first_node
        original_first_node.previous_node = node

        return

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._delete_relation(node)
        self._add_head_relation(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.get(key)
            return

        if len(self.key_to_node) >= self.capacity:
            tail_node = self.tail.previous_node
            self._delete_relation(tail_node)
            del self.key_to_node[tail_node.key]

        node = Node(value, key)
        self.key_to_node[key] = node
        self._add_head_relation(node)
        return

```

# Step2

## Code2-1

* listの管理を別のクラスで行うことにした

```python
class Node:
    def __init__(self, value = None, key = None, next_node = None, previous_node = None):
        self.value = value
        self.key = key
        self.next_node = next_node
        self.previous_node = previous_node


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail =  Node()
        self.head.next_node = self.tail
        self.tail.previous_node = self.head

    def insert_between(self, node, previous_node, next_node):
        previous_node.next_node = node
        node.next_node = next_node
        next_node.previous_node = node
        node.previous_node = previous_node
        return

    def delete(self, node):
        previous_node = node.previous_node
        next_node = node.next_node
        previous_node.next_node = next_node
        next_node.previous_node = previous_node
        return

    def pop_tail(self):
        node_to_delete = self.tail.previous_node
        self.delete(node_to_delete)
        return node_to_delete

    def append_front(self, node):
        self.insert_between(node, self.head, self.head.next_node)

    def move_to_front(self, node):
        self.delete(node)
        self.append_front(node)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.nodes = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.nodes.move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.nodes.move_to_front(node)
            return

        if len(self.key_to_node) >= self.capacity:
            node = self.nodes.pop_tail()
            del self.key_to_node[node.key]

        node = Node(value, key)
        self.key_to_node[key] = node
        self.nodes.append_front(node)
        return

```

## 他の人のPRを見る

* https://github.com/tom4649/Coding/pull/72
    * OrderedDictを使うとシンプルに描ける
    * > 将来拡張するときにバグが出にくくなりそうだなと思うので、一応自分ならnode.nextとnode.prevにNoneを入れておくかなと思いました。
* https://github.com/t0hsumi/leetcode/pull/16
    * 自分と同じように別でデータ構造(このPRではDeque)をクラスで定義している
* https://github.com/Mike0121/LeetCode/pull/49
    * > 仮に、これがインタビューで聞かれて OrderedDict で書けますが返事だとしたら、中を教えて下さいになると思います。

# Step3

## Code3-1

```python
class Node:
    def __init__(self, key = -1, value = -1, next = None, previous = None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head


    def insert_in_front(self, node):
        front_node = self.head.next

        node.previous = self.head
        node.next = front_node

        self.head.next = node

        front_node.previous = node

        return
    
    def delete(self, node):
        if node.next is None or node.previous is None:
            return
        
        previous_node = node.previous
        next_node = node.next

        previous_node.next = next_node
        next_node.previous = previous_node

        node.next = None
        node.previous = None

        return node

    def delete_last(self):
        return self.delete(self.tail.previous)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.nodes = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self.nodes.delete(node)
        self.nodes.insert_in_front(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.nodes.delete(node)
            self.nodes.insert_in_front(node)
            return
        
        if len(self.key_to_node) >= self.capacity:
            last_node = self.nodes.delete_last()
            del self.key_to_node[last_node.key]
        
        node = Node(key, value)
        self.key_to_node[key] = node
        self.nodes.insert_in_front(node)
        return

```