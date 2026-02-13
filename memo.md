# Step1

## アプローチ

* 括弧の種類ごとにスタックを用意しておく
    * 開始かっこが出てきた時はスタックにappend
    * 閉じ括弧が出てきた時はスタックからpop
    * 最終的にスタックが空になっていたらおk
* 再帰でもループでもできそう
* 括弧の種類ごとに個数をカウントしておくのでもいいか.
    * マイナスになった時点でinvalid

## Code1 (括弧の種類を数える方法, Wrong Answer)

* 問題文の条件`Open brackets must be closed in the correct order`を満たさず.
* 結局一つのstackに入れていくのが良さそう

```python
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses1 = 0
        parentheses2 = 0
        parentheses3 = 0
        for i in range(len(s)):
            if parentheses1 < 0 or parentheses2 < 0 or parentheses3 < 0:
                return False
            if s[i] == "(":
                parentheses1 += 1
            elif s[i] == "{":
                parentheses2 += 1
            elif s[i] == "[":
                parentheses3 += 1
            elif s[i] == ")":
                parentheses1 -= 1
            elif s[i] == "}":
                parentheses2 -= 1
            elif s[i] == "]":
                parentheses3 -= 1
        if parentheses1 == 0 and parentheses2 == 0 and parentheses3 == 0:
            return True
        return False
            
```

## Code2 (stack)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        unclosed_brackets = []
        brackets_pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for i in range(len(s)):
            if s[i] in brackets_pairs.keys():
                unclosed_brackets.append(s[i])
            else:
                if len(unclosed_brackets) == 0:
                    return False
                last_unclosed_bracket = unclosed_brackets.pop(-1)
                if brackets_pairs[last_unclosed_bracket] != s[i]:
                    return False
        if len(unclosed_brackets) == 0:
            return True
        return False
```

## Code3 (再帰)

* `return True`や`return False`が交互に出現するのが気持ち悪かったので, `return True`が最後に登場するようにした.
* 途中計算に使う値を変数に切り出して読みやすくした

```python
BRACKET_PAIRS = {
    "(" : ")",
    "{" : "}",
    "[" : "]"
}
class Solution:
    def _isValid(self, s, idx, stack):
        if idx == len(s):
            if len(stack) == 0:
                return True
            return False
        if s[idx] in BRACKET_PAIRS.keys():
            stack.append(s[idx])
            return self._isValid(s, idx + 1, stack)
        if len(stack) == 0:
            return False
        last_unclosed_bracket = stack.pop(-1)
        if BRACKET_PAIRS[last_unclosed_bracket] != s[idx]:
            return False
        return self._isValid(s, idx + 1, stack)

    def isValid(self, s: str) -> bool:
        return self._isValid(s, 0, [])
```

# Step2

## Code2-2 (stack)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        unclosed_brackets = []
        parentheses_pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        open_brackets = parentheses_pairs.keys()
        for i in range(len(s)):
            if s[i] in open_brackets:
                unclosed_brackets.append(s[i])
                continue
            if len(unclosed_brackets) == 0:
                return False
            last_unclosed_bracket = unclosed_brackets.pop(-1)
            expected_close_bracket = parentheses_pairs[last_unclosed_bracket]
            if s[i] != expected_close_bracket:
                return False
        if len(unclosed_brackets) > 0:
            return False
        return True
```

# Step3

## Code3-2 (stack)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        unclosed_open_brackets = []
        bracket_pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        open_brakets = bracket_pairs.keys()
        for i in range(len(s)):
            if s[i] in open_brakets:
                unclosed_open_brackets.append(s[i])
                continue
            if len(unclosed_open_brackets) == 0:
                return False
            last_open_bracket = unclosed_open_brackets.pop(-1)
            expected_close_bracket = bracket_pairs[last_open_bracket]
            if s[i] != expected_close_bracket:
                return False
        if len(unclosed_open_brackets) > 0:
            return False
        return True

```

# Step4/5

* 再帰降下法の実装をした.
    * [参考](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.5ynll0rwu02h)
* 自然言語で解釈をちゃんとできたらバグなく実装できた.
* ただ, `nonlocal`な変数として処理をしている`idx`を持つのは初見だと思いつかなさそう.
* 自然言語での動作の説明
    * `check_chunk_valid`は, 先頭の開きかっこから始まって対応する閉じ括弧まで(以降はchunkと呼ぶ)が有効かどうかを判定する関数.
    * chunkのなかは, 複数のchunkで構成されることもあるし, 単一のchunkであることもあるし, 何もないこともある
        * それぞれの具体例
            * ( () [] {} )
            * ( {([])} )
            * (  )
    * これら全てに対応する, かつ`check_chunk_valid`を再利用するためには, 対応する閉じかっこが出てくるまでこの関数を呼びたい.
    * `isValid`の入力は, 同じく複数チャンクからなる可能性があるので似た形式のループで`check_chunk_valid`を呼んであげる.
    * 以下の形のコードは２回出現する
        ```python
        while processing_idx < len(s):
            if not check_chunk_valid():
                return False
        ```



```python
class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        open_brackets = open_to_close.keys()
        processing_idx = 0

        def check_chunk_valid():
            nonlocal processing_idx
            if s[processing_idx] not in open_brackets:
                return False
            expected_end_bracket = open_to_close[s[processing_idx]]
            processing_idx += 1
            while processing_idx < len(s) and s[processing_idx] != expected_end_bracket:
                if not check_chunk_valid():
                    return False
            if processing_idx >= len(s):
                return False
            processing_idx += 1
            return True
        
        while processing_idx < len(s):
            if not check_chunk_valid():
                return False
        
        return True
```