# Step1

## アプローチ
* remove duplicates from sorted listとの違いは, かぶっているノードは全て消すこと.
* 二つのポインタを用意したらできそう
    * 一つ目のポインタは, これまでに処理し終えたリストの終点
    * 二つ目のポインタはこれから被りがあるかみる部分.
    * もう少し詳しく考える.
    * 一つ目のポインタの一個先と二個先が一緒じゃない(あるいはどちらかがNone)なら削除は不要.
    * 一つ目のポインタの一個先と二個先が一緒なら削除処理に移る.
        * 一つ目のポインタの一個先を基準点
        * 基準点の一個先（一つ目のポインタの二個先）が基準点と同じ値である限り前に進める.
        * 基準点と違う値になった場所(あるいはNoneになった場所)が, 一つ目のポインタのnextが指すノード(=A)になる.
    * 仕事の引き継ぎ
        * 一つ目のポインタをAに移す.
* 再帰呼び出しの解法もあるか考える.
    * 先頭の要素と次の要素が違うのならば, 先頭の要素のnextを先頭の要素のnextを引数として再帰呼び出しした返り値にする.
    * 先頭の要素と次の要素が一緒なら, 先頭の要素と異なる要素が出てくるまでノードをたどる. 先頭の要素と異なるノードを引数として渡した再帰関数の返り値を返す.
* 再帰とtwo pointerのどちらが良いか.
    * 再帰はpythonでは関数呼び出しのオーバヘッドが大きい.
        * 20nsが一回の呼び出しにかかるとして, 最大の場合でリストの長さ * 20nsかかる.
        * リストの長さが 1 * 10^9 / 20 = 5 * 10^7程度の時, オーバヘッドが1sになるため無視できない.
    * 今回はtwo pointerの方が適切そう.

## Code1-1 (two poitner)

* 汚いのでstep2で修正する.
    * is not Noneの判定が多すぎる.
        * processed_end is not Noneっていらなくねとは書いてて思ったからstep2で吟味.
    * .nextが基準になっているのをずらせないか検討したい.

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_start = ListNode()
        dummy_start.next = head
        processed_end = dummy_start
        while processed_end is not None and processed_end.next is not None and processed_end.next.next is not None:
            if processed_end.next.val != processed_end.next.next.val:
                processed_end = processed_end.next
                continue
            delete_start = processed_end.next
            delete_end = processed_end.next.next
            while delete_end is not None and delete_start.val == delete_end.val:
                delete_end = delete_end.next
            processed_end.next = delete_end
        return dummy_start.next
```

## Code1-2 (recursion)

* two poiterに比べて見やすいコードになった.
    * self.deleteDuplicates(None) -> Noneだが, 読む人からするとこのケースが考慮されているかわかりにくいかも？？

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        delete_start = head
        delete_end = head.next
        while delete_end is not None and delete_end.val == delete_start.val:
            delete_end = delete_end.next
        return self.deleteDuplicates(delete_end)
```

# Step2

## Code2-1

* `processed_end`を`unique`にした.
* 他の人を見る限り`dummy`は結局使わないと難しそう.
* `unique_candidate = unique.next`とすることで, 注目している基準を`unique`の次のノードにした.
    * `.next.next`が出現しなくて良くなった.
* `unique`が更新されるのは, `unique = unique.next`だけだが, `while`文の条件より, `unqiue.next`は`None`でないことが保証されている. `while`の条件式に`unique is not None`は不要になるが, 読み手からはわかりづらい？？？でもいい書き方がわからなかったので保留.

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_start = ListNode()
        dummy_start.next = head
        unique = dummy_start
        while unique.next is not None:
            unique_candidate = unique.next
            if unique_candidate.next is None or unique_candidate.val != unique_candidate.next.val:
                unique = unique.next
            else:
                duplication_val = unique_candidate.val
                while unique_candidate is not None and unique_candidate.val == duplication_val:
                    unique_candidate = unique_candidate.next
                unique.next = unique_candidate
        return dummy_start.next
```

## Code2-2

* Code1-2から変更なし

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        delete_start = head
        delete_end = head.next
        while delete_end is not None and delete_end.val == delete_start.val:
            delete_end = delete_end.next
        return self.deleteDuplicates(delete_end)
```

# Step3

* ３回実装する中でこうしたらわかりやすいかもという風に少しずつコードが変わっていった.

## １回目

* `unique_candidate`は, `unique`の一個先と二個先が等しい場合に考えたいもの. 
* そうではない場合は, `unique.next`がユニークなことが確定するので, 早めに処理を切り上げる.

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_start = ListNode()
        dummy_start.next = head
        unique = dummy_start
        while unique.next is not None:
            if unique.next.next is None:
                return dummy_start.next
            if unique.next.val != unique.next.next.val:
                unique = unique.next
                continue
            unique_candidate = unique.next
            duplication_val = unique_candidate.val
            while unique_candidate is not None and unique_candidate.val == duplication_val:
                unique_candidate = unique_candidate.next
            unique.next = unique_candidate
        return dummy_start.next
```

## ２回目

* `duplication_val`を`unique_candidate.val`にするのは直感に反していた.
    * ユニークな候補なはずなのに, その数字がかぶっている数字とするのは変.
    * `duplication_val = unique.next.val`とした.
        * `unique.next`は必ず重複するノードであることが`if`文の条件からわかるのでこっちの方が直感的.

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_start = ListNode()
        dummy_start.next = head
        unique = dummy_start
        while unique.next is not None:
            if unique.next.next is None:
                return dummy_start.next
            if unique.next.val != unique.next.next.val:
                unique = unique.next
                continue
            duplication_val = unique.next.val
            unique_candidate = unique.next.next
            while unique_candidate is not None and unique_candidate.val == duplication_val:
                unique_candidate = unique_candidate.next
            unique.next = unique_candidate
        return dummy_start.next
```

## ３回目

* `unique_candidate`文字通りユニークになり得るのは, `unique.next.next.next`から.
    * `.next`が複数続くのは少し違和感があったが, こっちの方が変数の意味に合致している

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        unique = dummy_head
        while unique.next:
            if unique.next.next is None:
                return dummy_head.next
            if unique.next.val != unique.next.next.val:
                unique = unique.next
                continue
            duplicated_val = unique.next.val
            unique_candidate = unique.next.next.next
            while unique_candidate is not None and unique_candidate.val == duplicated_val:
                unique_candidate = unique_candidate.next
            unique.next = unique_candidate
        return dummy_head.next
```