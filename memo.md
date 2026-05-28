# Step1

## アプローチ

* 見つからなかったら-1を返すbinary search

## Code1-1

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] == target:
            return left
        else:
            return -1

```

# Step2

## 他の人のPRを見る

* https://github.com/yamashita-ki/codingTest/pull/13
    * > ループを抜けたタイミングで区間には要素が含まれなくなります。これは違和感を感じます。

## コメント集

[二分探索](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0)

### 二分探索の考え方

https://discord.com/channels/1084280443945353267/1192736784354918470/1199018938005213234

```
left = 0
right = len(nums) - 1

と書いたら、left と right の両端を含む、この範囲にある、ということを考えていますね。
言い換えると、「target はあるとすると、left 以上、right 以下に必ずある」ということです。

「target はあるとすると、10以上10以下にあるんだよねー。」といわれたら、10確認しろよ、ってなりますよね。
だから、両端を含む場合は、同じ値でも確認しないといけません。

...

これが頭にあれば、それほど抵抗なく書けませんか?

```

---

https://discord.com/channels/1084280443945353267/1206101582861697046/1235118378793046036

```
うーむ。二分探索ですが、これも仕事の引き継ぎと思いましょう。

調査隊が、ベースキャンプを作っていて、非常に長い川の情報を調べていくんです。キャンプに left right の位置しか情報を置けないとすると、それは何を意味する情報なのか書けますでしょうか。
```

```
leftは常にGoodとなるような位置
rightは常にBadになるような位置
という前提を常に満たすようにすることでコードや解法がだいぶ単純化できるということに気づきました。
```

---

https://github.com/TORUS0818/leetcode/pull/43#discussion_r1970989476

```
二分探索は何をループの不変条件とするかによっていろいろな書き方があるんですが、不変条件を理解せずに書いている人が多いということです。
```

```
まずは「何を探しているのか」「ループごとに今どこまで分かっているのか」「それをどう変数に表現しているのか」というのが意味の部分の話で、あとはループの中で「終了条件」「更新」「必ず終了すること」という形式操作の話くらいです。

だいたい、意味をすっ飛ばして形式だけでやろうとするので、「左」「右」「閉区間」などと唱えたら倒せると思っているんですが、もっと単純に、二分探索の仕事を途中で引き継いだら知りたいことは何なのか「昇順で並んでいる数字の中で一番左の400以上の数を探していて、いくつか確認した。重要な知見として、25番目が288で、51番目が789、その間は開いていない。」くらいですよね。で、この情報を圧縮して変数とコードにするだけです。
```

---

https://nuc.hatenadiary.org/entry/2025/11/29/#%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2%E3%82%92%E8%AA%AD%E3%82%81%E3%82%8B%E3%81%8B

```
何を言っているかというと、二分探索で左だの右だの書いてあることがあるが、それが部隊内でどのような共通理解がなされているのかは必ず問題となるはずなのに、書いた本人もその理解がないまま書かれている場合がよくある。
```

## いろいろなバリエーションで書いてみる

* leftの指す要素より左はtargetより小さい
    * `index=-1`に`-inf`があると仮定
* rightの指す要素より右はtarget以上(区間内にtargetとなる値は残るように調整)
    * `index=len(nums)`に`inf`があると仮定

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] == target:
            return left
        else:
            return -1
        
```

---

以下の想定でやってみる  
`left`, `right`は境界自体を指すこととする  
コードに落とし込む上では, `left`や`right`の値の左側の境界を指していることとする

```
| 1 | 2 | 3 |
↑           ↑
left        right
```

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        if nums[left] == target:
            return left
        else:
            return -1

```

* 今まで, `right`はexclusiveとか思って書いていたバージョンは実は境界を表しているバージョンだったのか

---

上記のシチュエーションを別の捉え方でやる  
コードに落とし込む上で  
`left`はその値の左側の境界を指し  
`right`はその値の右側の境界を指すとする

```
| 1 | 2 | 3 |
↑           ↑
left        right
```

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] == target:
            return left
        else:
            return -1

```

* コードとしては最初に書いたもの(Code1-1)と同じになったが, 考え方は違っているのが面白い

---

ということは、`left`も`right`もその値の右側の境界を指しているとしても解けそう

```python
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums) - 1
        while right - left > 1:
            mid = math.ceil((left + right) / 2)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if nums[right] == target:
            return right
        else:
            return -1
        
```

# Step3

Step2で色々書いたので省略
