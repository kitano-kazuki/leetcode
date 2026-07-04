# Step1

## アプローチ

* 最初にbad versionとなった地点を探す
* 二分探索

## Code1-1

* 6:17
* 不変条件を意識した
* 指しているポインタとその外側は必ずBad or Good
* お隣に来た時点で境界ができあがる

```
G [G] | U U | [B]
```

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if not isBadVersion(n):
            return -1
        if isBadVersion(1):
            return 1
        
        good_left = 1
        bad_right = n

        while bad_right - good_left > 1:
            mid = (good_left + bad_right) // 2
            if isBadVersion(mid):
                bad_right = mid
            else:
                good_left = mid
        
        return bad_right

```                

# Step2

## 他の人のコードを見る

* https://github.com/naoto-iwase/leetcode/pull/68
* https://github.com/huyfififi/coding-challenges/pull/14
* https://github.com/rihib/leetcode/pull/33
    * > isBadVersion 次第ですが、これだとループ一回で最大3回呼ばれるのが少し気になりますね。場合によっては10分くらいかかるとても重い処理かもしれません
    * 最初の判定で２回呼んでいるのが無駄かも？？
        * でも結局最初や最後にbad versionがあると, 最初に判定しない限り工数が増えすぎちゃうよな

## Code2-1

* 変更なし

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if not isBadVersion(n):
            return -1
        if isBadVersion(1):
            return 1
        
        good_left = 1
        bad_right = n

        while bad_right - good_left > 1:
            mid = (good_left + bad_right) // 2
            if isBadVersion(mid):
                bad_right = mid
            else:
                good_left = mid
        
        return bad_right

```                


# Step3

## Code3-1

* 領域外(0やn+1)をGoodやBadとして行う方法
* good_most_rightの左側（数字と数字の間）が境界
* bad_most_leftの右側（数字と数字の間）が境界
* でも, leftやrightが普段の二分探索のleftやrightと違うからややこしいかも

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        good_most_right = 1
        bad_most_left = n

        while good_most_right < bad_most_left:
            mid = (good_most_right + bad_most_left) // 2
            if isBadVersion(mid):
                bad_most_left = mid - 1
            else:
                good_most_right = mid + 1
        
        if isBadVersion(good_most_right):
            return good_most_right
        else:
            return good_most_right + 1

```

## Code3-2

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if not isBadVersion(n):
            return -1
        if isBadVersion(1):
            return 1
        
        left = 1
        right = n
        while right - left > 1:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        
        return right
        
```
