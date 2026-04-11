# 1st: 1:34
# 2nd: 4:26
# 3rd: 1:02


class Solution:
    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        previous_two_same = k
        previous_two_different = k * (k - 1)
        for _ in range(2, n):
            new_previous_two_same = previous_two_different
            new_previous_two_different = previous_two_same * (k - 1) + previous_two_different * (k - 1)
            previous_two_same = new_previous_two_same
            previous_two_different = new_previous_two_different
        return previous_two_same + previous_two_different

solution = Solution()
print(solution.num_ways(3, 2))
print(solution.num_ways(2, 2))