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

# Step6/7/8 (LL(1))

* LL(1)の実装をした.
* アルゴリズムとかは[ブログ](https://kazuki.jp.net/archives/456)にまとめた.
* `follow`で循環が起きているとバグりそうだけど, うまいこと対照する方法が思いつかなかった.
    * A -> aBC
        * first(C)が"#"を含む時, follow(A)を計算して, follow(B)に追加する
    * B -> aAC
        * follow(B)を計算して, follow(A)に追加する
    * このような生成規則が与えられるとバグりそう  

```python
class Parser:
    def __init__(self, terminals, nonterminals, rules, start_symbol):
        self.terminals = terminals
        self.nonterminals = nonterminals
        self.rules = rules
        self.start_symbol = start_symbol
        self.follow_memo = {}
        self.parsing_table = {}
        self._construct_parsing_table()
    
    def first(self, string):
        if len(string) == 1:
            if string == "#":
                return set(["#"])
            if string in self.terminals:
                return set([string])
            result = set()
            for produced_string in self.rules[string]:
                result = result | self.first(produced_string)
            return result
                    
        result = set()
        for symbol in string:
            symbol_first_result = self.first(symbol)
            if "#" not in symbol_first_result:
                result = result | symbol_first_result
                return result
            symbol_first_result.remove("#")
            result = result | symbol_first_result
        result.add("#")
        return result

    def follow(self, nonterminal):
        if nonterminal not in self.nonterminals:
            raise ValueError(f"{nonterminal} is not non-terminal")
        if nonterminal in self.follow_memo:
            return self.follow_memo[nonterminal]
        result = set() if nonterminal != self.start_symbol else set(["$"])
        for production_head, produced_strings in self.rules.items():
            for produced_string in produced_strings:
                nonterminal_idx = produced_string.find(nonterminal)
                if nonterminal_idx == -1:
                    continue
                while nonterminal_idx != -1:
                    remaining_string = produced_string[nonterminal_idx + 1:]
                    if remaining_string:
                        remaining_string_first_res = self.first(remaining_string)
                        if "#" not in remaining_string_first_res:
                            result = result | remaining_string_first_res
                        else:
                            production_head_follow_result = self.follow(production_head) if production_head != nonterminal else set()
                            result = result | production_head_follow_result | (remaining_string_first_res - set(["#"]))
                    else:
                        production_head_follow_result = self.follow(production_head) if production_head != nonterminal else set()
                        result = result | production_head_follow_result
                    nonterminal_idx = produced_string.find(nonterminal, nonterminal_idx + 1)
        self.follow_memo[nonterminal] = result
        return result
            
    def _construct_parsing_table(self):
        for nonterminal in self.nonterminals:
            self.parsing_table[nonterminal] = {}
            for terminal in self.terminals + ["$"]:
                self.parsing_table[nonterminal][terminal] = []
        for production_head, produced_strings in self.rules.items():
            for produced_string in produced_strings:
                produced_string_first_result = self.first(produced_string)
                if "#" in produced_string_first_result:
                    head_follow_result = self.follow(production_head)
                    for terminal in head_follow_result:
                        self.parsing_table[production_head][terminal].append({production_head : produced_string})
                    produced_string_first_result.remove("#")
                for terminal in produced_string_first_result:
                    self.parsing_table[production_head][terminal].append({production_head : produced_string})
        # print(self.parsing_table)
        return
    
    def parse(self, input):
        end_idx = len(input)
        input = input + "$"
        stack = ["$", self.start_symbol]
        processing_idx = 0
        while stack[-1] != "$":
            symbol = stack.pop()
            input_char = input[processing_idx]
            if symbol == input_char:
                processing_idx += 1
                continue
            if symbol in self.terminals:
                return False
            if not self.parsing_table[symbol][input_char]:
                return False
            production_rules = self.parsing_table[symbol][input_char]
            if len(production_rules) >= 2:
                return False
            production_rule = production_rules[0]
            produced_string = production_rule[symbol]
            if produced_string != "#":
                for produced_char in produced_string[::-1]:
                    stack.append(produced_char)
        return processing_idx == end_idx
    
class Solution:
    def isValid(self, s: str) -> bool:

        nonterminals = ["S", "C"]
        terminals = ["(", ")", "{", "}", "[", "]", "e"]
        rules = {
            "S" : ["CS","#"],
            "C" : ["(S)", "{S}","[S]"]
        }
        start_symbol = "S"
        parser = Parser(terminals, nonterminals, rules, start_symbol)
        return parser.parse(s)

```