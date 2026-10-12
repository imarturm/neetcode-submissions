class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in s:
                cur = 0
                while n in s:
                    n += 1
                    cur += 1
                    longest = max(cur, longest)

        return longest