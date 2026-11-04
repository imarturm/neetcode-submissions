class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        cache = {}
        def dfs(i1, i2):
            if i1 == n or i2 == m:
                return 0
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            if text1[i1] == text2[i2]:
                cache[(i1, i2)] = 1 + dfs(i1 + 1, i2 + 1)
            else:
                cache[(i1, i2)] = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))
            return cache[(i1, i2)]
        return dfs(0, 0)