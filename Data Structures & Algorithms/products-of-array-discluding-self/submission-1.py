class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [nums[0]] * n, [nums[-1]] * n

        for i in range(n - 1):
            left[i + 1] = left[i] * nums[i + 1]
        for i in range(n - 1, 0, -1):
            right[i - 1] = right[i] * nums[i - 1]
        
        res = [right[1]] + [0] * (n - 2) + [left[n - 2]]
        for i in range(1, n - 1):
            res[i] = left[i - 1] * right[i + 1]
        return res