# Step1

## アプローチ

* n行k番目のシンボルは, n-1行{(k+1)//2}番目をもとに決まる
    * kが奇数の時は, n-1行目のシンボルと一緒
    * kが偶数の時は, n-1行目のシンボルと反対
* top-down的に求めたい答えから遡って探していく
    * loopでも再帰でも解けそう
    * 今回はloopでやってみる
* 計算量
    * 段数分処理を行う
    * O(N) : 30 / 10^6 ~= 10^-5 sec = 10 ns

## Code1-1

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n <= 0:
            raise ValueError("n must be > 0")
        
        if k > 2 ** (n - 1):
            raise ValueError("k must be less than the number of symbols in the row")

        is_reverse = False
        row = n
        col = k
        while row > 1:
            if col % 2 == 0:
                is_reverse = not is_reverse
            row = row - 1
            col = (col + 1) // 2
        
        if is_reverse:
            return 1
        else:
            return 0
                
```
