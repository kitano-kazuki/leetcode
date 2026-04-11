# solved: 6:47

class Solution:
    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        previous_two_same = k
        previous_two_different = k * (k - 1)
        for _ in range(2, n):
            temporary = previous_two_same
            previous_two_same = previous_two_different
            previous_two_different = temporary * (k - 1) + previous_two_different * (k - 1)
        
        return previous_two_same + previous_two_different

# solution = Solution()
# print(solution.num_ways(3, 2))
# print(solution.num_ways(2, 2))