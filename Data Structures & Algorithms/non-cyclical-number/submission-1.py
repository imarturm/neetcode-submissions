class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            s = 0
            for c in str(n):
                s += int(c) ** 2
            n = s
        return n == 1