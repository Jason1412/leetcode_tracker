# Last updated: 5/16/2026, 12:29:18 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
    
        ind = self.bsearch(nums, 0, len(nums)-1)

        return ind

    def bsearch(self, nums, start, end):


        left = start
        right = end

        while (left + 1 < right):

            mid = (left + right) // 2

            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] >= nums[mid]:
                right = mid
            elif nums[mid] <= nums[mid+1]:
                left = mid
            
        
        if nums[left] > nums[right]:
            return left
        else:
            return right























    
    
    
    # def findPeakElement(self, nums: List[int]) -> int:
        
    #     if len(nums) == 1:
    #         return 0

    #     start = 0
    #     end = len(nums) - 1

    #     ind = self.bsearch(nums, start, end)

    #     return ind

    
    # def bsearch(self, nums, start, end):

        
    #     left = start
    #     right = end

    #     while (left + 1 < right):
    #         mid = (left + right) // 2

    #         if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
    #             return mid
    #         elif nums[mid] <= nums[mid-1]:
    #             right = mid
    #         elif nums[mid] <= nums[mid+1]:
    #             left = mid

    #         # Need to ensure the len > 3

    #     if nums[left] > nums[right]:
    #         return left
    #     else:
    #         return right