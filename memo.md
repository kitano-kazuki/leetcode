# Step1

## アプローチ

* すでにソート済みの二つのリストを結合したい
* 先頭から順番に見ていって, 新しいHeadに加えていく
* あるいは, 一つ目のリストを基準にして二つ目のリストを付け加えていく
* 空間計算量がO(1)になるが, inputが破壊されるのがどうかという観観
* 時間計算量は, O(N + M)
* 実行時間は, 100 / 10^6 ~= 10^-4sec程度

## Code1-1 

* AC: 7:41
* 実装中に思ったけど, これは与えられたノードを再利用している
* mergedリストの中身の値を書き換えたら, list1の中身も書き変わる
* それが嫌ならcopyして, 末尾に追加するとかの方がいい

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        merged_tail = dummy_head

        head1 = list1
        head2 = list2

        while head1 is not None or head2 is not None:

            if head1 is None:
                merged_tail.next = head2
                merged_tail = merged_tail.next
                head2 = head2.next
                continue
            
            if head2 is None:
                merged_tail.next = head1
                merged_tail = merged_tail.next
                head1 = head1.next
                continue
            
            if head1.val <= head2.val:
                merged_tail.next = head1
                merged_tail = merged_tail.next
                head1 = head1.next
                continue
            else:
                merged_tail.next = head2
                merged_tail = merged_tail.next
                head2 = head2.next
                continue
        
        return dummy_head.next

```

# Step2

## Code2-1

* 変更なし

## 他の人のPRを見る

* https://github.com/naoto-iwase/leetcode/pull/62
    * bigger, smallerを使って, head1, head2に行っていた対照的な処理を簡潔にまとめている
* https://github.com/ryosuketc/leetcode_grind75/pull/3
    * > 別言語で解いてみる取り組みいいなと思いました。触発されて数問Pythonで解いて見ております。
    * たしかに, C++で解くようにするのもありやな
* https://github.com/huyfififi/coding-challenges/pull/3
    * > 私の言語感覚では、これは「マージ済みの最後尾」なんですがいかがですか。例えば、merged_tail あたりです。
    * これが一緒の感覚でよかった
* https://github.com/rihib/leetcode/pull/1

# Step3

* 1st: 2:42
* 2nd: 2:48
* 3rd: 1:45

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        dummy_head = ListNode()
        merged_tail = dummy_head
        node1 = list1
        node2 = list2
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                merged_tail.next = node1
                merged_tail = merged_tail.next
                node1 = node1.next
                continue
            else:
                merged_tail.next = node2
                merged_tail = merged_tail.next
                node2 = node2.next
                continue
        
        if node1 is None:
            merged_tail.next = node2
        if node2 is None:
            merged_tail.next = node1

        return dummy_head.next
```