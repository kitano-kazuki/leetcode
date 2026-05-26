# Step1

## Code1-1

* O(N^2)になるので, TLEになった

```python
import functools


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        @functools.cache
        def can_reach_helper(i: int):
            if i == len(s) - 1: 
                return s[i] == "0"
            
            if s[i] == "1":
                return False
            
            for jump in range(minJump, maxJump + 1):
                if i + jump >= len(s):
                    break
                if can_reach_helper(i + jump):
                    return True
            
            return False

        return can_reach_helper(0)
        
```

## Code1-2

* O(N)でやりたい
* 各インデックスごとに, いける範囲を引き継ぐ
* `s = "011010", minJump = 2, maxJump = 3`
    * `01[10]10`
    * `01101[0`
* `s = "010010", minJump = 2, maxJump = 3`
    * `01[00]10`
    * `01[00](10)`
* 範囲の右端にきたら, その範囲はそれ以上残しておく必要はない
* 範囲の寿命は, その範囲の右端にくるまでだから, 範囲の長さ（最大でN）
* 各インデックスごとに, 対象の範囲をみるとすると, 結局最大でO(N^2)になる
* いける範囲に重なりがあるから, それをうまいこと対処できたら嬉しい気がする
* これが常に２区間に抑えられるならいいけど、飛び石上になっていたらめんどう
    * `01110000000000, min=4, max=5`
    * `0111[00]00000000`
    * `0111[00]00(00)0000`
    * `0111[00]00(0{0)0}000`
    * `0111[00]00(0{0)0}0|00|`
    * `0111[00]00(0{0)0}0|0"0|`
* 到達可能かどうかをTrue/Falseで保存しておく
* Trueとなっている0の値に到達するたびに, 配列を更新する
* すでにいけると更新をしたおしりは記録しておく
* `010010`, `TFFFFF`
* `0100|10`, `TFTTFF`
* `010010|`, `TFTTFT`
* ある時点iでいけない点j(s[j]=0)があったとき, i以降のs[k]=0となる点をもってしても, jには到達できない
* AC


```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return True
        if s[0] == "1":
            return False

        reachable = [False] * len(s)
        reachable[0] = True

        updated_tail = 0
        for i in range(len(s)):
            if updated_tail >= len(s):
                break
            if s[i] == "1":
                continue
            if not reachable[i]:
                continue
            for j in range(max(updated_tail + 1, i + minJump), min(len(s), i + maxJump + 1)):
                if s[j] == "0":
                    reachable[j] = True
            
            updated_tail = i + maxJump
        
        return reachable[-1]

```