# Step1
## アプローチ

* 与えられるリストが整列されているということは, 同じ数字は必ず連続で出現する.
* 一個前の数字を保持しておいて, 今見ている数字が一個前の数字と同じだったら削除する.
* 削除をした場合は, 一個前のノードのnextを今のノードのnextにする必要がある.
    * 一個前の数字を保持するのではなくてオブジェクトを保持したい.
* その後, 次に見るノードとして今見ているノードの次のノードを採用.
* 削除にあたっては, ただ繋ぎかえるだけだとメモリに残り続けるのかな？？
    * ガベージコレクションがいつ働くかだけど, どのオブジェクトもnextとして指していない, かつ, その値がどこにも使われていなくなった瞬間にガベージコレクションが働くのかな？？？
    * 関数呼び出しが終わった後にガベージコレクションが働きそう???. 毎回チェックしていたらオーバーヘッドかかかる？ でも, 各オブジェクトが参照されている数を変数として持っておけば, それが0になった時に削除するだけか. C++とかそういう実装だったような気がするが, あまり自信がないな.
    * 明示的にdelを読んだ方が親切な気がする.
* 計算時間は, リストの長さ文.
* 外部メモリは, 一個前のノードの参照を保持する分だけ使用.
* 終わり際の処理を考えたい. .nextがNoneの時.
    * 今見ているオブジェクトが前のオブジェクトと値が違う場合
        * 次に見るオブジェクトがNoneになるので, 処理をそこで終了すればいい
    * 今見ているオブジェクトが前のオブジェクトと値が一緒の場合
        * 前のオブジェクトのnextを今のオブジェクトのnext(=None)にする
        * 次に見るオブジェクトを今見ているオブジェクトのnext(=None)に更新する
    * どちらも問題がなさそう. 今見ているオブジェクトがNoneの時に処理を終了する.

## Code1

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
            if prev is not None and prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head
```

# Step2

* ガベージコレクションが働いているかわからないので,delを明示的に呼ぶ.

## Code2-1

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
            if prev is not None and prev.val == cur.val:
                prev.next = cur.next
                del cur
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head
```
* コードとしては動いたが以下の不安があった.
    * `del cur`をした時点で4行目に宣言したcurという変数自体が消えちゃわない？？
        * その場合は, `cur = prev.next`でcurという局所変数が定義されることになるが, while文のこのループが終わって次のループに行く時には消えてしまうのでは？？
        * pythonだからガバガバな可能性がある？？？
        * `del`がそもそも, 変数を消すものではなくて, 変数が参照だった時にその中身を解放するものだったとしたら。。。？
            * curが一時的にNoneになるだけでコードとしては問題がなくなる
        * 上記は後で検証するとして, 懸念を払拭したコードを作ろう.

## Code2-2
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
            if prev is not None and prev.val == cur.val:
                to_delete = cur
                prev.next = cur.next
                cur = prev.next
                del to_delete
            else:
                prev = cur
                cur = cur.next
        return head
```

