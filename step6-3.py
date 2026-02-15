# バグありコード. Step7で修正
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

solution = Solution()
print(solution.isValid("}"))