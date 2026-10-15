from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        l, best = 0, (0, float("inf"))
        for r, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            while missing == 0:
                if r - l < best[1] - best[0]:
                    best = (l, r)
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        return "" if best[1] == float("inf") else s[best[0]:best[1] + 1]