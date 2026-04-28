# Step1

## アプローチ

* 左より値が下がるところがminimumになる
* 前から順番に見ていけばO(N)で探せる
* n = 5000なので, 5 * 10^3 / 10^6 = 0.005 sec程度で終わる
* 二分探索を使う場合はどうするか
    * 今観に行った場所の右に最小があるのか左に最小があるのか次の人に伝えたい
    * 今観に行った場所より右に最小がある
        * 左端 <= 今の場所 and 今の場所 > 右端
    * 今観に行った場所かそれより左に最小がある
        * 今の場所 <= 右端 or 左端 > 今の場所

## Code1-1 (Iterative)

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        
        return nums[0]

```

## Code1-2 (Binary Search)

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")
        if len(nums) == 1:
            return nums[0]

        left_exclusive = -1
        right_inclusive = len(nums) - 1
        while left_exclusive + 1 != right_inclusive:
            mid = left_exclusive + (right_inclusive - left_exclusive) // 2
            if nums[0] <= nums[mid] and nums[mid] > nums[-1]:
                left_exclusive = mid
            else:
                right_inclusive = mid

        return nums[right_inclusive]

```

# Step2

## Code2-1 (Iterative)

* 「直前の要素」が「今の要素」よりも大きいならば
* という自然言語をif文で表すなら, `if nums[i - 1] > nums[i]`の方が自然な気がした

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i]
        
        return nums[0]

```

## Code2-2 (Binary Search)

* `mid = -1`の時に想定しない動作をする可能性がある
    * `len(nums) == 1`のときはそもそも`while`が実行されない
        * でもそれを確認するのが若干パズルなので、アーリーリターンで返した
    * `len(nums) >= 2`のときは常に`mid != -1`となるが, 読み手が確認する手間を省くためにコメントを追加

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")
        if len(nums) == 1:
            return nums[0]

        # len(nums)>=2よりmidは-1にならない
        left_exclusive = -1
        right_inclusive = len(nums) - 1
        while left_exclusive + 1 != right_inclusive:
            mid = left_exclusive + (right_inclusive - left_exclusive) // 2
            if nums[0] <= nums[mid] and nums[mid] > nums[-1]:
                left_exclusive = mid
            else:
                right_inclusive = mid

        return nums[right_inclusive]

```

# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/42
    * 細かく検討している項目
        * left, rightの取り方（閉区間or開区間）
        * 切り上げや切り下げ
* https://github.com/naoto-iwase/leetcode/pull/25
* https://github.com/mamo3gr/arai60/pull/40

## 他の人のコメントを見る

### 二分探索の理解を深める質問

https://github.com/seal-azarashi/leetcode/pull/39#discussion_r1849419449

```
どのあたりに違和感を感じているのか、なんですが、まず

「2で割る処理がありますがこれは切り捨てでも切り上げでも構わないのでしょうか。」
「nums[middle] <= nums[right] とありますが、これは < でもいいですか。」
「nums[right] は、nums[nums.length - 1] でもいいですか。」
「right の初期値は nums.length でもいいですか。」

これ、組み合わせて16通りのソースコードが生成できますが、どれが動いてどれが動かないか答えられますか。
```

今回、自分が書いたソースコード Step2-2 (Binary Search)を元に考える

=> 結論全部動作としては問題ない.

#### 切り上げで問題が生じるか

Q. 「2で割る処理がありますがこれは切り捨てでも切り上げでも構わないのでしょうか。」

A. 問題がない

詳しく検討する.

切り上げにすることで変わるのはmidの取り方.
midは区間を狭める役割を果たしているから基本的にはどこをとってもいいはず.
気にするべきは、無限ループにならないかと条件式がそのままでも大丈夫か

このままだと、nums[mid] = nums[-1]のとき、
最小値はmidまたはそれより左側に存在する
という条件に移動する
これは正しそう.

ただ、毎回midが右端で選ばれていると
right_inclusive = mid
で範囲が狭まっていないので無限ループになる??

繰り上げが起こるのは要素数が偶数の時
真ん中の要素のうち左寄りでとるか右寄りでとるかが変わる

nums[mid] = nums[-1]になるのは,
要素数が2で繰り上げをした時
しかし、今回の取り方ではそれは起こらない

leftの初期値 -1 かつ, `left + 1 == right`でwhileを抜けるので
要素数が２になることはない

よって今回のコードでは問題がなさそう
=> 実行して問題ないことを確認


#### 等合をつけるかつけないか

Q. 「nums[middle] <= nums[right] とありますが、これは < でもいいですか。」
(自分のコードが`nums[mid] > nums[-1]`なので`nums[mid] >= nums[-1]`として問題ないか)

A. 問題ない

前述の通り, `nums[mid] = nums[-1]`となることがあり得ないのでどっちでもいい
=> 実行して問題ないことを確認


#### midとの比較対象の変更

Q. 「nums[right] は、nums[nums.length - 1] でもいいですか。」
(自分のコードが`nums[mid] > nums[-1]`なので`nums[mid] > nums[right]`として問題ないか)

A. 問題ない

前項の検討より、切り上げでも切り下げでもmidがrightになることはないので`=`の有無は関係ない

`-1`を`right`に変更してもロジック的には問題ない
部分問題の解決的な発想になるだけ
=> 実行して問題ないことを確認

#### rightの初期値の変更

Q. 「right の初期値は nums.length でもいいですか。」

A. 問題ないが非推奨.

前項の検討より, midがrightになることはない.
終了条件よりrightが更新されないままnums.lengthで終わることはない.

でもright_inclusiveとしているので, nums.lengthから始めるのは違和感しかない
=> 実行して問題ないことを確認

# Step4

## Code4-2 (Binary Search)

どっちもinclusiveの方が描きやすかった

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")
        
        if len(nums) == 1:
            return nums[0]
        
        left_inclusive = 0
        right_inclusive = len(nums) - 1
        while left_inclusive < right_inclusive:
            mid = left_inclusive + (right_inclusive - left_inclusive) // 2
            if nums[mid] > nums[-1]:
                left_inclusive = mid + 1
            else:
                right_inclusive = mid
        
        return nums[left_inclusive]


```