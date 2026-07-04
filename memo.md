# Step1

## アプローチ

* 一回に1段か2段あがるとして, n段上がる方法はどのくらいあるか
* n段目に上がる方法は, n - 1段目にあがる方法とn-2段目にあがる方法の和
* 再帰でとくことができる
* あるいは, n = 1のときから順番に見て行ってもいい
    * 配るdpでもできるし, もらうdpでもできる
        * 配るdpでは, k段目までの上り方がl通りあったとすると, k + 1段目, k + 2段目への上り方もそれぞれl通りはあるとする
* ここまで3:39

## Code1-1 (再帰)

* AC: 2:09
* メモ化をしなかった場合の計算量を考える
* 各nごとに, 2回の呼び出しがある
* O(2^n)かな？？

```python
import functools


class Solution:
    @functools.cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
```

## Code1-2 (もらうDP)

* AC: 1:08

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        num_steps = [None] * (n + 1)
        num_steps[0] = 1
        num_steps[1] = 1
        for i in range(2, n + 1):
            num_steps[i] = num_steps[i - 1] + num_steps[i - 2]
        
        return num_steps[n]
        
```

## Code1-3（配るDP）

* AC: 2:16

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        num_steps = [0] * (n + 1)
        num_steps[0] = 1
        for i in range(n + 1):
            if i + 1 <= n:
                num_steps[i + 1] += num_steps[i]
            if i + 2 <= n:
                num_steps[i + 2] += num_steps[i]
        return num_steps[n]

```

# Step2

## Code2-1(再帰関数)

* `n == 0`と`n == 1`を一つにまとめた

```python
import functools


class Solution:
    @functools.cache
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
```

## Code2-2(もらうDP)

* 変更なし

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        num_steps = [None] * (n + 1)
        num_steps[0] = 1
        num_steps[1] = 1
        for i in range(2, n + 1):
            num_steps[i] = num_steps[i - 1] + num_steps[i - 2]
        
        return num_steps[n]
        
```

## Code2-3(配るDP)

* 変更なし

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        num_steps = [0] * (n + 1)
        num_steps[0] = 1
        for i in range(n + 1):
            if i + 1 <= n:
                num_steps[i + 1] += num_steps[i]
            if i + 2 <= n:
                num_steps[i + 2] += num_steps[i]
        return num_steps[n]

```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/16
    * DPの解法は二つだけ値を保存しておけばいいので, 空間計算量をO(1)にできる
    * > これ、もうちょっと良い評価で、フィボナッチ数になります。だいたい O(1.6^n) ですね。
        * https://github.com/irohafternoon/LeetCode/pull/33#discussion_r2071628078

    * 再帰の方法では、メモ化を使わなくても, タプルで返すことで線形時間にすることもできる
        * https://discord.com/channels/1084280443945353267/1201211204547383386/1247145320098566144
            ```
            いや、私の良くするたとえ話としてね、木の全ノードに部下を立たせるんですよ。

            そうすると、nonlocal って、部下たちのいる部屋に共通の看板を立てておいて、全部下がその看板に書いたり消したりするんですよね。

            それだったら、部下同士のやり取り(関数呼び出し)の中で、自分より下の部分の max_sum の情報も報告するようにしたほうがスマートじゃないでしょうか、ということです。

            たとえば、こっちの方がスレッド増やしたくなったときに並列性が良さそうです。
            ```
* https://github.com/rihib/leetcode/pull/35
    * > メモ化再帰はトップダウンな順序で計算し、動的計画法はボトムダウンな順序で計算するイメージがあります。計算結果自体はほとんどの場合において一致します。

## Code2-4 (タプルを返す再帰関数)

* 下記２点を問い合わせ
    * あなた自身はどのくらいのステップでいけるのですか
    * あなたの一つ下の段はどのくらいのステップでいけるのですか


```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb_stairs_helper(n: int) -> tuple[int, int]:
            if n == 1:
                return (1, 1)
            
            one_lower, two_lower = climb_stairs_helper(n - 1)
            return one_lower + two_lower, one_lower
        
        return climb_stairs_helper(n)[0]

```

## Code2-5 (空間計算量をO(1)にしたDP)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        one_lower = 1
        two_lower = 1
        for _ in range(2, n + 1):
            one_lower, two_lower = one_lower + two_lower, one_lower
        return one_lower

```

# Step3

## Code3-4 (タプルを返す再帰関数)

* 1st: 0:48
* 2nd: 0:35
* 3rd: 0:31

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb_stairs_helper(n: int) -> tuple[int, int]:
            if n == 1:
                return (1, 1)
            
            one_lower, two_lower = climb_stairs_helper(n - 1)
            return one_lower + two_lower, one_lower
        
        return climb_stairs_helper(n)[0]

```
