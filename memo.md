# Step1

## アプローチ
* 各ノードの値がユニークなら, 先頭から順番に見ていくと同時に値をsetに保存. setに保存されている値に遭遇したらcycleがあるというアルゴリズムでいける.
    * ノードの参照をsetに保存できるなら値がユニークではなくても同じアルゴリズムで解けそう.
    * この場合はメモリをリストの要素数分使う可能数がある.
* ユニークじゃないなら, slowポインタとfastポインタを使って, それぞれ１つ,２つずつ進めるようにする. サイクルがあるならslowが到着するまでにfastが追いつくかな.
    * slowが一番後ろにつくまでにfastはリストを２周できるから必ず追いつく. 
    * 線形時間で終わる. メモリもfastとslowの二つのポインタ分だけ使う.  
* メモリの効率性を考えると後者のアプローチ(fastとslowのポインタを使用)が良さそう.

## 最初に書いたコード

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None or fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
```

```bash
AttributeError: 'NoneType' object has no attribute 'next'
           ^^^^^^^^^^^^^^
    fast = fast.next.next
Line 7 in hasCycle (Solution.py)
    ret = Solution().hasCycle(param_1)
Line 34 in _driver (Solution.py)
    ~~~~~~~^^
    _driver()
Line 47 in <module> (Solution.py)
```

* fast.nextがNoneでエラーが出たっぽい.
* while文の条件を詳しく確認して, orじゃなくてandが正しそう
    * fastがnot Noneだけど, fast.nextがNoneでもwhileの処理が行われてしまう.
    *  fastがNone　あるいは, fast.nextがNoneの時に処理を終了するのは問題なさそう. nextにNoneがある時点でcycleはないと断定できるから.
* and演算子の評価順が不安だったので, 一応andの両側は()で処理順を明確にした.

## ２回目に書いたコード(最終的なコード)
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
```