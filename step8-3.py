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
