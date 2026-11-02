class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        rob1 = rob2 = 0
        for n in nums[1:]:
            rob1, rob2 = rob2, max(rob2, rob1 + n)
        skip_first = rob2

        rob1 = rob2 = 0
        for n in nums[:-1]:
            rob1, rob2 = rob2, max(rob2, rob1 + n)
        skip_last = rob2
    
        return max(skip_first, skip_last)