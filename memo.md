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

# Step3

* Leetcodeの解説を見ていると, `prev`ではなく, `head`を基準にその一つ先をみるアプローチがあった. 再帰を使うものもあった.
* それぞれのアプローチについて詳しく考えてみる.
* `head`を基準に一つ先をみるアプローチ
    * 本質的には`prev`を見ているものと変わらない気がする.
    * 実装レベルでは, `head`を基準に先をみる場合は, `head.next`が`not None`である必要があるため`while`の条件式が変わる.
    * `head`を基準に見た場合は, 別の変数を作らなくていい文メモリ的に効率的？？でも一つの参照の値を保持するかどうかだから誤差な気がした.
        * 一つの参照って何bitなんだろうか. => 32bitくらい？？
            * アドレス空間中から一意に特定できる表現幅ってことだよな.
            * そもそもオブジェクトや変数ってどこに保存されるんだっけ.
                * 使う時にレジスタに持ってきて, レジスタが埋まっていたら, ldやstでメモリに退避させてたよな
                    * st %r1 0(%a1)だっけ
                * じゃあレジスタに保存され得る大きさしかアドレスって存在しない？？
                    * いや、複数のレジスタ組み合わせれば無限に表現できるか
                * メインメモリだっけ. でキャッシュヒットするならldは早いけど, ヒットしなかったら遅いってこと？？？
                    * ヒットした時は2クロック？
                    * ヒットしなかったら次のキャッシュを見て(L2), それも無理だったらその次を見て...
                        * 最後までヒットしなかったらメインメモリを見る？？
                        * ここら辺は調べたい
* 再帰呼び出しによるアプローチ
    * 先頭を消すかどうか判断して, 消したなら先頭.nextを引数に再帰呼び出しした結果をreturn. 消さなかったら`先頭.next = 再帰呼び出し(先頭.next)`とした上で先頭をreturn.
    * 関数呼び出しはリストの小数分呼ばれそう.
    * 関数呼び出しのオーバーヘッドはどのくらいか
        * その関数内で使われている変数をstackに退避して, stack pointer動かす.
        * stackに退避/復帰する時に, ldやstを使っていたから2clockはかかりそう??
    * 実行時間の差分が関数のオーバーヘッドということになりそう
    * 関数呼び出しが多すぎたら, stackの一番上まで到達しちゃう？？？ stackの上の方って何かと競合してたはず. グローバル変数置いてたっけ？そこがオーバーしたらエラーになりそう. どのくらいまで呼び出せるのか. もしエラーにならなかったらどんな影響があるのか. pythonやc++はstackがオーバーすることをどうやって検知するのか.

* 関数呼び出しのオーバーヘッドが十分に無視できるか. 関数呼び出しによるstackの上限はあるのか.
    * おそらくどちらも大規模計算では考慮する必要があるため再帰呼び出しは良くなさそう.

## Code3-1(prevを使用)
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

## Code3-2(headの先をみる)
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res
```

## Code3-3(再帰呼び出し)
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None and head.next is not None:
            if head.val == head.next.val:
                return self.deleteDuplicates(head.next)
            else:
                head.next = self.deleteDuplicates(head.next)
                return head
        return head
```

* ３行目`if head is not None and head.next is not None:`としているが, `if head is None or head.next is None`の時に`return head`で先に処理を終了してもいい気がしてきた.
    * `head is None`だった時に, 4行目以降のif文が間に挟まって, その後に処理が来ている. if文の中が長いとスクロールに時間がかかりそう.


# 調べたいこと
* ガベージコレクションの動作タイミング
* pythonのdelの仕組み
* pythonの変数のスコープ
* ld/stの仕組み
* キャッシュヒット/ミス時の振る舞い
* 参照のbit数
* 関数呼び出しのオーバーヘッド
* stackの上限
* stackの上限に達した時の振る舞い