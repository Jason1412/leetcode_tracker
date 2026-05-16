# Last updated: 5/16/2026, 12:30:44 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        slow, fast = 0, 1

        while fast < len(nums):
            
            if slow < fast and nums[slow] == nums[fast]:
                fast += 1

            if slow < fast and fast < len(nums) and nums[slow] != nums[fast]:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1


        return slow + 1
            

