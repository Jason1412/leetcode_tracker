# Last updated: 5/16/2026, 12:30:13 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        p = 0

        while p <= p2:
            if nums[p] == 0:
                self.swap(nums, p0, p)
                p0 += 1
            elif nums[p] == 2:
                self.swap(nums, p2, p)
                p2 -= 1
            elif nums[p] == 1:
                p += 1


            if p < p0:
                p = p0
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]