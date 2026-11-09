class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        val_pointer = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[val_pointer], nums[i] = nums[i], nums[val_pointer]
                k += 1
                val_pointer += 1
        return k
        