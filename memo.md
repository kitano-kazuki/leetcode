# Step1

## アプローチ

* シフト制でやることを考える
* 自分の元に来る仕事
    * 演算子がわかっている(あるいは単一の数字のみ)
        * その後に出てくる二つの数字の句切れ目を見つける
            * それぞれの区切り目ごとに, それの評価結果を教えてもらう
        * でも, その場合は何度も同じ文字列を見ないといけない
        * O(N^2)になりそう
            * N + N - 1 + N - 2 + N - 3 + ...
* 直前に見た演算子を記録しておく, 数字が2個連続したら、直前に見た演算子を使って計算をする
* ここまで7:22

## Code1-1

* AC: 17分くらい

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = []
        i = len(tokens) - 1
        while not symbols or type(symbols[0]) is str:
            calculatable = len(symbols) >= 3 and type(symbols[-1]) is int and type(symbols[-2]) is int and type(symbols[-3]) is str
            if not calculatable:
                if tokens[i] in ["+", "-", "*", "/"]:
                    symbols.append(tokens[i])
                else:
                    symbols.append(int(tokens[i]))
                i -= 1
                continue
            operand1 = int(symbols.pop())
            operand2 = int(symbols.pop())
            operator = symbols.pop()
            if operator == "+":
                symbols.append(operand1 + operand2)
                continue
            if operator == "-":
                symbols.append(operand1 - operand2)
                continue
            if operator == "*":
                symbols.append(operand1 * operand2)
                continue
            if operator == "/":
                if operand1 * operand2 < 0:
                    symbols.append(-1 * (abs(operand1) // abs(operand2)))
                else:
                    symbols.append(operand1 // operand2)
        
        return symbols[0]
        
```

# Step2

## Code2-1 (reverse order)

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = []
        i = len(tokens) - 1
        while not symbols or type(symbols[0]) is str:
            # 数字2つと演算子1つの並びかどうか
            calculatable = len(symbols) >= 3 and type(symbols[-1]) is int and type(symbols[-2]) is int and type(symbols[-3]) is str

            if not calculatable:
                if tokens[i] in ["+", "-", "*", "/"]:
                    symbols.append(tokens[i])
                else:
                    symbols.append(int(tokens[i]))
                i -= 1
                continue

            operand1 = int(symbols.pop())
            operand2 = int(symbols.pop())
            operator = symbols.pop()
            if operator == "+":
                symbols.append(operand1 + operand2)
                continue
            if operator == "-":
                symbols.append(operand1 - operand2)
                continue
            if operator == "*":
                symbols.append(operand1 * operand2)
                continue
            if operator == "/":
                if operand1 * operand2 < 0:
                    symbols.append(-1 * (abs(operand1) // abs(operand2)))
                else:
                    symbols.append(operand1 // operand2)
        
        return symbols[0]
        
```

## 他の人のPRを見る

* https://github.com/TaisukeFujise/leetcode_tafujise/pull/22
    * 普通にtoken列の先頭から処理をしていける
    * stackには数字だけ積むようにして, operatorに遭遇した時はstackから二つ数字を取り出すこととする
        * validなtoken列なら必ずoperator遭遇時に数字が二つ以上stackに存在している
* https://github.com/tom4649/Coding/pull/73
    * `//`演算子は0方向じゃなくてマイナスの無限方向に丸められる
        * > The result is always rounded towards minus infinity: 1//2 is 0, (-1)//2 is -1, 1//(-2) is -1, and (-1)//(-2) is 0.
    * `int()`は小数部分を消す
        * > Conversion from float to int truncates, discarding the fractional part
    * > 面接のハックとしては、「うわー、整数の割り算は言語ごとに仕様が違ってややこしいとはいえ、普段使い慣れているこの言語でこれが分からなくなっちゃっているなんて失格ですねえ。うわー、どれでしたっけ。普段だったら仕様書か公式マニュアルを調べるんですが、面接の場でこんなことが分からないなんて恥ずかしすぎます。」という顔をしていると、この技を使うのが、1,2回くらいならば、ほぼノーダメージでしょう
    * > Python の `round()` は IEEE 754 偶数丸めに従う。
    * 記号をkey, valueをlambda式にして, 条件分岐を減らしているのが面白い書き方だと思った. わかりやすい
* https://github.com/huyfififi/coding-challenges/pull/33

## Code2-2 (normal order)

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_to_function = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        operands = []
        for token in tokens:
            if token not in operator_to_function:
                operands.append(int(token))
                continue
            right_operand = operands.pop()
            left_operand = operands.pop()
            operands.append(operator_to_function[token](left_operand, right_operand))
        
        return operands[-1]
        
```

# Step3

## Code3-2

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_to_function = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        operands = []
        for token in tokens:
            if token not in operator_to_function:
                operands.append(int(token))
                continue
            right_operand = operands.pop()
            left_operand = operands.pop()
            operands.append(operator_to_function[token](left_operand, right_operand))
        
        return operands[-1]

```
