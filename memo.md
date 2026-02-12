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