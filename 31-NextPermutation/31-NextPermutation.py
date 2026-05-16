# Last updated: 5/16/2026, 12:30:41 PM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 1

        while i >= 1:
            if nums[i-1] >= nums[i]:
                i -= 1
            else:
                break
            
            if i == 0:
                nums.reverse()
                return nums
        
        # print("i=", i)

        # i - 1 --- position to swap
        # i --- position of the part to reverse

        j = len(nums) - 1

        while j >= i:
            if nums[j] > nums[i-1]:
                nums[j], nums[i-1] = nums[i-1], nums[j]
                break
            j -= 1
        
        # print("i=", i)
        # print("j=", j)
        # print("nums=", nums)
        
        nums[i:] = reversed(nums[i:])

        # print("nums=", nums)
        return nums
            


