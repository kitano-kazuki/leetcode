# Step1

## アプローチ

* 一番単純な方法は, 各リストが示すintegerを数字に変換. 変換した数字同士を足し合わせる. 結果をリストに変換.
    * この方法だと, ３回分リストの長さを捜査する必要がある.
    * 片方のリストの桁数がばかデカくて, もう片方のリストの桁数が１桁だと無駄が多い.
* 繰り上がりを考慮しながら, 全加算機みたいに構成できないか.
    * 各リストごとに, 処理中の桁を示すポインタをそれぞれ用意.
    * 結果を格納するリストを用意.
    * 結果リストのうち,処理し終わった最後のノードを指すポインタを用意.
    * そのポインタが指す値同士を足した一の位を値にもつノードを作成して, 結果リストのポインタの末尾に追加.
    * 仕事の引き継ぎ.
        * 処理中の桁を示すポインタを移動.
        * 結果リストのポインタを先ほど作成したノードに移動.
        * 繰り上がりがない場合は以上.
        * 繰り上がりがある場合は,
            * 繰り上がった値を次に渡す.
* 上記の方法だと, 結果の格納用に新しいメモリ空間を用意している
    * ある一つのリストにもう一つのリストの値を加算していく方法が取れたらメモリ的に新しい領域を確保しなくていいので嬉しい
    * リストの長さがわかっていたら, リストのうち, 長い違法を足される数（基準）にする
    * 今回はリストの長さがわからない, リストの長さが短い方が基準になったらどうなるか.
        * 繰り上がりがない場合は, もう一つのリスト（長い方の値）をひたすらコピーするだけ
        * いや、コピーじゃなくて繋ぎ変えればいいのか

## Code1-1 (外部メモリ不使用, ワンパス)

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        bef_node2 = None
        carry = 0
        while node1 is not None and node2 is not None:
            summed_value = node1.val + node2.val + carry
            node2.val = summed_value % 10
            carry = summed_value // 10
            bef_node2 = node2
            node1 = node1.next
            node2 = node2.next
        if node1 is None:
            while node2 is not None:
                summed_value = node2.val + carry
                node2.val = summed_value % 10
                carry = summed_value // 10
                bef_node2 = node2
                node2 = node2.next
            if carry != 0:
                bef_node2.next = ListNode(carry)
            return l2
        bef_node2.next = node1
        bef_node1 = bef_node2
        while node1 is not None:
            summed_value = node1.val + carry
            node1.val = summed_value % 10
            carry = summed_value // 10
            bef_node1 = node1
            node1 = node1.next
        if carry != 0:
            bef_node1.next = ListNode(carry)
        return l2
```

## Code1-2 (数字に直して足し算⇨リスト生成)
```python
class Solution:
    def parseListAsInteger(self, l):
        node = l
        digits = []
        while node is not None:
            digits.append(node.val)
            node = node.next
        digits = digits[::-1]
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.parseListAsInteger(l1)
        num2 = self.parseListAsInteger(l2)
        summed_num = num1 + num2
        if summed_num == 0:
            return ListNode(0)
        dummy_head = ListNode(0)
        node = dummy_head
        while summed_num > 0:
            digit_node = ListNode(summed_num % 10)
            node.next = digit_node
            node = node.next
            summed_num = summed_num // 10
        return dummy_head.next
```

## Code1-3 (再帰呼び出し)

```python
class Solution:
    def _addTwoNumbers(self, l1, l2, carry):
        if l1 is None and l2 is None:
            if carry == 0:
                return None
            return ListNode(carry)
        if l1 is None:
            summed_value = l2.val + carry
            node = ListNode(summed_value % 10)
            carry = summed_value // 10
            node.next = self._addTwoNumbers(None, l2.next, carry)
            return node
        if l2 is None:
            summed_value = l1.val + carry
            node = ListNode(summed_value % 10)
            carry = summed_value // 10
            node.next = self._addTwoNumbers(l1.next, None, carry)
            return node
        summed_value = l1.val + l2.val + carry
        node = ListNode(summed_value % 10)
        carry = summed_value // 10
        node.next = self._addTwoNumbers(l1.next, l2.next, carry)
        return node
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self._addTwoNumbers(l1, l2, 0)
        
```

# Step2

## Code2-1

* `node2.next is None`の時に, `node2.next`をリスト１の余剰分の開始点に変更することでループを１つで済むようにした.
* `tail`は常に`node2`の一つ前を指すようにしているが, 結局使うのは一番最後の`carry`を元にしたノードの追加の時だけ.
    * 毎回保存しているの勿体無い気がするけど, 最後だけ保存するためにわざわざ`if`文を書くのも読みにくくなる気がした

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        carry = 0
        tail = None
        while node2 is not None:
            node1_value = node1.val if node1 is not None else 0
            summed_value = node1_value + node2.val + carry
            node2.val = summed_value % 10
            carry = summed_value // 10
            node1 = node1.next if node1 is not None else None
            if node2.next is None:
                node2.next = node1
                node1 = None
            tail = node2
            node2 = node2.next
        if carry != 0:
            tail.next = ListNode(carry)
        return l2
```
