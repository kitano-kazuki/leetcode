# Step1

## アプローチ

* 141の問題と違って, サイクルの開始点を出す必要がある
    * fastとslowポインタを使っていても, fastとslowが一致した場所がサイクルの開始点ではないため一工夫が必要そう.
        *　その工夫が思いつかないのでこのアプローチは取らないことにした.
    * setを使って一度訪れたノードを入れる方法では, ふたたび遭遇した時にサイクルの開始点がわかる.
        * ただ, 外部メモリの使用量がノード数分になる可能性がある.
        * pythonの実装でsetにオブジェクトを入れられるのか不明.
            * 無理だったらそれぞれにユニークなidをつけて, idとオブジェクトのマッピングを別で保持しておく.

## Code 1

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None
```

# Step2

* Step1との変更点はなし.
* pythonでsetにオブジェクトを追加することができた.