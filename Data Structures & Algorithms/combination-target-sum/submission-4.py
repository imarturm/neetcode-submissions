class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] > remaining:
                    break
                path.append(nums[j])
                backtrack(j, remaining - nums[j])
                path.pop()
        
        backtrack(0, target)
        return res