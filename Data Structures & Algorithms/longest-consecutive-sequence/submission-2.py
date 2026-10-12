class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in s:
            if n - 1 not in s:
                end = n
                while end + 1 in s:
                    end += 1
                longest = max(longest, end - n + 1)
        return longest