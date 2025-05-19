from typing import List

def parse_digit_list(s: str, sequence: List[int]) -> List[str]:
    results = []
    for num in sequence:
        result = ""
        for i in range(len(s)):
            is_one = num >> i & 1
            if is_one:
                result += s[i]
        results.append(result)
    return results


def extract_subsequence(s: str) -> List[str]:
    n = len(s)
    subsequence_int = [i for i in range(1, 2 ** n)]
    for i in range(n):
        one_digit_num = 1 << i
        subsequence_int.remove(one_digit_num)
        for j in range(i + 1,n):
           one_digit_num2 = 1 << j
           to_remove = one_digit_num | one_digit_num2
           subsequence_int.remove(to_remove)
    print(subsequence_int)
    subsequence = parse_digit_list(s, subsequence_int)
    return subsequence


def is_all_special(s: str, st: List[str]) -> bool:
    subsequences = extract_subsequence(s)
    for subseq in subsequences:
        if subseq in st:
            continue
        return False
    return True


s="good"
st = ["goo" , "god", "ood", "great", "good"]
print(is_all_special(s, st))
