# Step1

## アプローチ

* 特定の金額を作るために必要な最小のコイン枚数を出したい
* 自分の手元に財布があったら, なるべく大きい金額から試すかな
* でも全ての種類のお金があるわけではないのが今回の問題。一円玉みたいなのが存在しなかったらうまく表せられないものが存在する
    * [2, 3, 5] で 14をつくりたいとき
        * 5, 5, 3と選ぶと作れなくなってしまう
* 階段を登ることを考えてみる
    * 一度に登れる段数が2, 3, 5
    * 14段目まで登りたい
    * 12段目, 11段目, 10段目が昇れているかを見ればいい
* `amount`までの値それぞれについて, 必要なコインの最小枚数を計算する
* 必要なコインの最小枚数は, `len(coins)`遡ったそれぞれの段数がいけているかを確認する
* coins.length = N, amount = Mとして
* O(M * N)
* 10^4 / 10^6 = 0.01sec程度の実行時間
* メモリは, 各値段(<=amount)での最小コイン枚数を記録するのでO(M)
* 28 byte * 10^4 / 1024 = 280KBくらい


## Code1-1 (DP)

```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        min_coins = [0] + [None] * (amount)
        for target in range(amount + 1):
            if min_coins[target] is None:
                continue
            for coin in coins:
                if target + coin > amount:
                    continue
                if min_coins[target + coin] is None or min_coins[target] + 1 < min_coins[target + coin]:
                    min_coins[target + coin] = min_coins[target] + 1
        
        if min_coins[amount] is None:
            return -1
        return min_coins[amount]

```

# Step2


* [リーダブルコード](https://www.amazon.co.jp/%E3%83%AA%E3%83%BC%E3%83%80%E3%83%96%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89-%E2%80%95%E3%82%88%E3%82%8A%E8%89%AF%E3%81%84%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E6%9B%B8%E3%81%8F%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%A7%E5%AE%9F%E8%B7%B5%E7%9A%84%E3%81%AA%E3%83%86%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF-Theory-practice-Boswell/dp/4873115655)を買ったのでそれに基づいてStep2をやるようにする
* 今までは変更なしが多かったけど、いざ意識してみると書き換えた方がいいところが見つかるようになった
* `for target in range(amount + 1)`の`target`という命名を悩んだがいい名前はおもいつかず
    * リーダブルコードp10「2.1 明確な単語を選ぶ」
        * 空虚な単語は避けるべきだとしている
        * 例えば, 
            * `getPage`よりも`fetchPage`や`downloadPage`
            * `Size`よりも`Height`や`NumNodes`
    * リーダブルコードp12「2.2 tmpやretvalなどの汎用的な名前を避ける」
        * retvalは「これは戻り値です」の情報しかないがそれは当たり前
    * リーダブルコードp23「スコープがちいさければ短い名前でもいい」
        * すべての情報（変数の型・初期値・破棄方法）が見えるので変数の名前は短くていい
    * 今回の`target`という命名は, 明確ではないし汎用的な単語に分類されそう. 一方でスコープがたかだか10行なので`target`のままにした. 同じくらい短くて簡潔に「特定の額」みたいなニュアンスを伝えられたらそれがベストではありそう
* `min_coins`という命名
    * リーダブルコードp30「誤解されない名前」
        * 名前が「他の意味と間違えられることはないだろうか」と何度も自問自答する
    * `min_coins`だと, 「coinの額の最小」と勘違いしてしまいそう
    * 今回は「枚数の」最小だから、きちんと`min_num_coins`にした
* `min_num_coins[target + coin] = min(...)`の整形
    * リーダブルコードp47「縦の線をまっすぐにする」
        * 縦の線をまっすぐにすれば文章に目を通しやすくなる
        * 縦の線が「視覚的なてすり」になれば、流し読みが楽にできるようになる
    * ここまで考えたことがなかった
    * `min`を計算する行が横に長くなってしまったので改行をすることで, `min`を計算する対象を一目で映るようにした
* `# amount以下の金額それぞれで必要な最小コイン枚数を計算`というコメント
    * リーダブルコードp67「要約コメント」
        * 関数の内部でも「全体像」についてコメントするのはいい考えだ。
        * 低レベルのコードをうまく要約したコメントを紹介しよう
        * コメントがないとコードを読んでいる途中で意味がわからなくなる
        * このような要約コメントは関数の内部にある大きな塊につけてもいい
    * リーダブルコードp76「コードの意図を書く」
        * コメントというのはコードを書いている時に考えていたことを読み手に伝えるためのものだ
* 上記コメント前後の改行
    * リーダブルコードp51「コードを「段落」に分割する」
        * 似ている考えをグループにまとめて、他の考えとわける
        * 段落単位で移動できるようになる
* `# float("inf")は特殊な値なので, ==の比較が正しく動作する`というコメント
    * リーダブルコードp63「読み手の立場になって考える」
        * 質問されそうなことを想像する
        * ハマりそうな罠を告知する
    * 今回は自分が読んでいて, 「float同士の比較はinfなら本当に正確に行われるのか？」疑問になった
    * 過去の経験から動くことはわかっていたが、他の人が読んだ時に同じ疑問を持った上で、まあ大丈夫でしょうくらいで読み流すかもしれない
    * 念の為調べてコメントで記載した

## Code2-1 (DP)

```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        # amount以下の金額それぞれで必要な最小コイン枚数を計算
        min_num_coins = [0] + [float("inf")] * amount
        for target in range(amount + 1):
            if min_num_coins[target] == float("inf"):
                continue
            for coin in coins:
                if target + coin > amount:
                    continue
                min_num_coins[target + coin] = min(
                    min_num_coins[target + coin], 
                    min_num_coins[target] + 1
                )
        
        # float("inf")は特殊な値なので, ==の比較が正しく動作する
        # IEEE754 - https://tmytokai.github.io/open-ed/activity/fpoint/text03/page02.html
        if min_num_coins[amount] == float("inf"):
            return -1
        return min_num_coins[amount]

```

## Code2-2 (Recursion)

```python
import functools


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        @functools.cache
        def calc_minimum_num_coins(amount: int) -> int:
            if amount < 0:
                return -1
            if amount == 0:
                return 0

            # 「(総額 - コインの額)を作るのに必要な最小枚数」+ 1 の最小値を計算
            minimum_num_coins = float("inf")
            for coin in coins:
                num_coins = calc_minimum_num_coins(amount - coin)
                if num_coins == -1:
                    continue
                minimum_num_coins = min(minimum_num_coins, num_coins + 1)
            
            # float("inf")は特殊な値なので, ==の比較が正しく動作する
            # IEEE754 - https://tmytokai.github.io/open-ed/activity/fpoint/text03/page02.html
            if minimum_num_coins == float("inf"):
                return -1
            return minimum_num_coins

        return calc_minimum_num_coins(amount)

```