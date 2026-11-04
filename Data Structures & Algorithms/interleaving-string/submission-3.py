class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        cache = defaultdict(bool)
        cache[(m, n)] = True
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    continue
                cache[(i, j)] = ((i < m and s1[i] == s3[i + j] and cache[(i + 1, j)]) or
                                (j < n and s2[j] == s3[i + j] and cache[(i, j + 1)]))
        return cache[(0, 0)]