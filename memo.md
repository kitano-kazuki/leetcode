# Step1

## アプローチ

* nペアのかっこであり得るパターンを全部出す
* 再帰的にやるとわかりやすそう
    * () + 残りのかっこ
    * ( + 残りのかっこ + )
    *  残りのかっこ + ()
    * これ以外にはないよね
    * 被りこみだと 3^N個できる
    * 作ったそれぞれを最後にまとめる(あるいはコピーする)
        * カッコの長さは2 * N
    * 計算量は O(N * 3^N)?
    * 実行ステップでは8 * 3^8 ~= 6 * 10^3
    * 実行時間は, 6 * 10^-3 sec

## Code1-1(Wrong Answer)

* ( + 残りのかっこ + ) + ( + 残りのかっこ + )のパターンができてなかった
* n = 4のときに, `(())(())`が生成されていない

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        parentheses = set()

        def generate_parenthesis_helper(n: int, parts: str) -> None:
            if n == 0:
                parentheses.add(parts)
                return
            
            generate_parenthesis_helper(n - 1, "()" + parts       )
            generate_parenthesis_helper(n - 1, "("  + parts + ")" )
            generate_parenthesis_helper(n - 1,        parts + "()")
        
        generate_parenthesis_helper(n, "")
        
        return list(sorted(parentheses))

```

## Code1-1(AC)

* 開きカッコは必ず閉じカッコよりも先に多く置かれている必要があるという条件のもとで, 先頭から配置

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        parentheses = set()

        def generate_parenthesis_helper(num_open_brackets: int, num_close_brackets: int, parts: list[str]) -> None:
            if num_open_brackets == 0 and num_close_brackets == 0:
                parentheses.add("".join(parts))
                return

            if num_open_brackets > num_close_brackets:
                return
            
            if num_open_brackets > 0:
                parts.append("(")
                generate_parenthesis_helper(num_open_brackets - 1, num_close_brackets, parts)
                parts.pop()

            if num_close_brackets > 0:
                parts.append(")")
                generate_parenthesis_helper(num_open_brackets, num_close_brackets - 1, parts)
                parts.pop()

            return

        generate_parenthesis_helper(n, n, [])
        return list(sorted(parentheses))
            
```

# Step2

## Code2-1

* 注目する対象を置いたカッコにしたほうがわかりやすい

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        parentheses = []

        def generate_parenthesis_helper(num_placed_open: int, num_placed_close: int, parts: list[str]) -> None:
            if num_placed_open == n and num_placed_close == n:
                parentheses.append("".join(parts))

            if num_placed_open < num_placed_close:
                return
            
            if num_placed_open < n:
                parts.append("(")
                generate_parenthesis_helper(num_placed_open + 1, num_placed_close, parts)
                parts.pop()

            if num_placed_close < n:
                parts.append(")")
                generate_parenthesis_helper(num_placed_open, num_placed_close + 1, parts)
                parts.pop()

            return

        generate_parenthesis_helper(0, 0, [])
        return parentheses
            

```

# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/54
    * 自分のACしたコードと同様に, 今までに置いたかっこの数に基づいてbacktrack
* https://github.com/naoto-iwase/leetcode/pull/54
    * 自分のWAとなったコードと同様のアプローチにも至っていた

# Step4

## Code4-1

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        all_parentheses = []

        def generate_parenthesis_patterns(num_open: int, num_close: int, parts: list[str]) -> None:
            if num_open == n and num_close == n:
                all_parentheses.append("".join(parts))
                return
            
            if num_open < num_close:
                return

            if num_open < n:
                parts.append("(")
                generate_parenthesis_patterns(num_open + 1, num_close, parts)
                parts.pop()
            
            if num_close < n:
                parts.append(")")
                generate_parenthesis_patterns(num_open, num_close + 1, parts)
                parts.pop()
            
            return
        
        generate_parenthesis_patterns(0, 0, [])
        return all_parentheses


```