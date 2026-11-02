class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        maximum = -float("inf")
        for n in nums:
            prefix = max(prefix + n, n)
            maximum = max(maximum, prefix)
        return maximum