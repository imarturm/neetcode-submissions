class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best = (0, 0)
        for i in range(n - 1):
            # odd case
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > best[1] - best[0]:
                    best = (l, r)
                l -= 1
                r += 1
            # even case
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > best[1] - best[0]:
                    best = (l, r)
                l -= 1
                r += 1
        return s[best[0]:best[1] + 1]