# Last updated: 5/16/2026, 12:28:37 PM
class Solution:
# Method 2 ==================================================
    def moveZeroes(self, nums: List[int]) -> None:
        slow, fast = 0, 0

        n = len(nums)

        if n == 1:
            return nums

        while fast < n:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                
            fast += 1
    
        while slow < n:
            nums[slow] = 0
            slow += 1

        return nums




# Method 1 ==================================================
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
        
    #     p0, p = 0, 0

    #     n = len(nums)

    #     if n == 1:
    #         return nums

    #     while p0 < n and p < n:
            
    #         while p0 < n and nums[p0] != 0:
    #             p0 += 1
            
    #         while p < n and nums[p] == 0:
    #             p += 1
            

    #         if p0 < n and p < n:
    #             if p0 < p:
    #                 nums[p0], nums[p] = nums[p], nums[p0]
    #             else:
    #                 p += 1
            

    #     return nums
            