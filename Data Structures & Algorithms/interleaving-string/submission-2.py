class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False

        cache = {(m, n): True}
        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = (i < m and s1[i] == s3[i + j] and dp(i + 1, j)) or (j < n and s2[j] == s3[i + j] and dp(i, j + 1))
            return cache[(i, j)]
        return dp(0, 0)