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

# Step6 (LL(1)を実装中だが, バグとりに苦戦中)

```python
class Parser:
    def __init__(self):
        self.V = ["S", "C"]
        self.T = ["(", ")", "{", "}", "[", "]", ""]
        self.P = {
            "S" : ["CS",""],
            "C" : ["(S)", "{S}","[S]"]
        }
        self.S = "S"
        self.first_map = {}
        self.follow_map = {}
        self.parsing_table = {}
        self._construct_follow_map()
        self._construct_parsing_table()
    
    def first(self, alpha):
        if alpha in self.first_map:
            return self.first_map[alpha]
        if alpha == "":
            return set([""])
        result = set()
        for i in range(len(alpha)):
            symbol = alpha[i]
            if symbol in self.T:
                result.add(symbol)
                self.first_map[alpha] = result
                return result
            if symbol not in self.V:
                raise ValueError(f"the input word [{alpha}] begins with the character not defined in this language.")
            if symbol in self.V:
                ith_first_result = set()
                for produced in self.P[symbol]:
                    ith_first_result = ith_first_result.union(self.first(produced))
                if "" not in ith_first_result:
                    result = result.union(ith_first_result)
                    self.first_map[alpha] = result
                    return result
                ith_first_result.remove("")
                result = result.union(ith_first_result)
        result.add("")
        self.first_map[alpha] = result
        return result

    def _construct_follow_map(self):
        self.follow_map[self.S] = set(["$"])
        for production_head, produced_list in self.P.items():
            for produced in produced_list:
                for processing_idx, symbol in enumerate(produced):
                    if symbol in self.T:
                        continue
                    if symbol in self.V:
                        if symbol not in self.follow_map:
                            self.follow_map[symbol] = set()
                        remaining_string = produced[processing_idx+1:]
                        remaining_string_first_result = self.first(remaining_string)
                        if remaining_string == "" or "" in remaining_string_first_result:
                            self.follow_map[symbol] = self.follow_map[symbol].union(self.follow_map[production_head])
                        if "" in remaining_string_first_result:
                            remaining_string_first_result.remove("")
                        self.follow_map[symbol] = self.follow_map[symbol].union(remaining_string_first_result)
        return

    def follow(self, A):
        if A not in self.V:
            raise ValueError(f"the input variable [{A}] is not a variable used in this language")
        return self.follow_map[A]
        
    def _construct_parsing_table(self):
        for non_terminal in self.V:
            self.parsing_table[non_terminal] = {}
            for terminal in self.T + ["$"]:
                self.parsing_table[non_terminal][terminal] = []
        for production_head, produced_list in self.P.items():
            for produced in produced_list:
                produced_first_result = self.first(produced)
                for terminal in produced_first_result:
                    self.parsing_table[production_head][terminal].append({production_head : produced})
                if "" in produced_first_result:
                    head_follow_result = self.follow(production_head)
                    for terminal in head_follow_result:
                        self.parsing_table[production_head][terminal].append({production_head : produced})
        print(self.parsing_table)
        return
    
    def parse(self, input):
        for word in input:
            if word not in self.T:
                # print(f"word [{word}] is not the terminal used in this language")
                return False
        input = input + "$"
        stack = ["$", self.S]
        processing_idx = 0
        while stack[-1] != "$":
            symbol = stack.pop()
            word = input[processing_idx]
            if symbol == word:
                processing_idx += 1
                continue
            if symbol in self.T:
                # print(f"The given input is not this language")
                return False
            if not self.parsing_table[symbol][word]:
                # print(f"There is no way to parse the symbol [{symbol}] with preceeding word [{word}]")
                return False
            production_rules = self.parsing_table[symbol][word]
            if len(production_rules) >= 2:
                # print(f"There are multiple rules to convert {symbol} with one word prediction of {word}")
                return False
            production_rule = production_rules[0]
            produced = production_rule[symbol]
            if produced != "":
                for produced_word in produced[::-1]:
                    stack.append(produced_word)
        return True
    
class Solution:
    def isValid(self, s: str) -> bool:
        parser = Parser()
        return parser.parse(s)

```