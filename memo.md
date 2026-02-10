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

# Step2

* 自分ではStep1で書いたコードで読みやすいと思っている.
* LeetCodeの提出結果によると実行速度が52msで上位51%なので, どこか遅くなっているかも？？
    * `pos = n - 2 (nはリストの要素数)`の時, fastはslowが追いついてくるまで `n-2`と`n-1`の要素を行き来するが, slowは`n-2`回で到着するのでボトルネックではなさそう.
    * これ以上早くする方法がわからなかったので回答を確認した.
        * 結局わからず. pythonだから遅いだけ？
    
## 最初に書いたコード(最終的なコード)

Step1との変更点はなし.

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

# Step3

* Step2で実行時間に関しての懸念を示したが, 何回も提出していたら上位92%の実行時間になったこともあったのでサーバーの計算リソースの占有状況的な揺れの可能性がある.
* `fast is not None`は`fast`と同値なので置き換えた.

## 最終的なコード

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```