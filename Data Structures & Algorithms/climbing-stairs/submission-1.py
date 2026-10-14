class Solution:
    def climbStairs(self, n: int) -> int:
        prev2, prev1 = 1, 1
        for _ in range(n - 1):
            prev2, prev1 = prev1, prev2 + prev1
        return prev1