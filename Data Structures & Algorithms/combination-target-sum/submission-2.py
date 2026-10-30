class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(current_sum, number_to_add):
            new_sum = current_sum + number_to_add
            if new_sum > target:
                return
            path.append(number_to_add)
            
            if new_sum == target:
                res.append(path.copy())
                path.pop()
                return
            
            for n in (n for n in nums if n >= number_to_add):
                backtrack(new_sum, n)
            path.pop()
        
        for n in nums:
            backtrack(0, n)
        return res