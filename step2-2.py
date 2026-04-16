import functools


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @functools.cache
        def unique_paths_helper(m, n) -> int:
            if m == 1 or n == 1:
                return 1
            return unique_paths_helper(m - 1, n) + unique_paths_helper(m, n - 1)

        return unique_paths_helper(m, n)
