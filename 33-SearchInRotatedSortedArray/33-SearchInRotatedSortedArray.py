# Last updated: 5/16/2026, 12:30:40 PM
class Solution:

# Method 2 ================================================
    # def search(self, nums: List[int], target: int) -> int:

        # if target >= nums[0] and target >= nums[-1]:
        #     on_left = True
        # elif target >= nums[0] and target < nums[-1]:
        #     on_left = False
        # else:
        #     on_left = False

        
        # start = 0
        # end = len(nums) - 1

        # while (start + 1 < end):
        #     mid = (start + end) // 2

        #     if on_left:
        #         if nums[mid] <= nums[-1]:
        #             end = mid
        #         elif nums[mid] > nums[-1] and nums[mid] > target:
        #             end = mid
        #         elif nums[mid] > nums[-1] and nums[mid] < target:
        #             start = mid
        #         elif nums[mid] > nums[-1] and nums[mid] == target:
        #             return mid
            
        #     if not on_left:
        #         if nums[mid] > nums[-1]:
        #             start = mid
        #         elif nums[mid] <= nums[-1] and nums[mid] > target:
        #             end = mid
        #         elif nums[mid] <= nums[-1] and nums[mid] < target:
        #             start = mid
        #         elif nums[mid] <= nums[-1] and nums[mid] == target:
        #             return mid
        
        # if nums[start] == target:
        #     return start
        # elif nums[end] == target:
        #     return end
        # else:
        #     return -1
            




# Method 1 ================================================
# binary search twice
    def search(self, nums: List[int], target: int) -> int:
        
        ind_min = self.findMin(nums, nums[-1])
        if target <= nums[-1]:
            start = ind_min
            end = len(nums) - 1
            out = self.bsearch(nums, start, end, target)
        else:
            start = 0
            end = ind_min - 1
            out = self.bsearch(nums, start, end, target)
        return out


    def findMin(self, nums, target):

        start = 0
        end = len(nums) - 1

        while (start + 1 < end):
            mid = (start + end) // 2

            if nums[mid] < target:
                end = mid
            elif nums[mid] > target:
                start = mid
            elif nums[mid] ==  target:
                end = mid
        
        if nums[start] > nums[end]:
            return end
        else:
            return start

    def bsearch(self, nums, start, end, target):
        
        while (start + 1 < end):
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid 
            elif nums[mid] > target:
                end = mid
            elif nums[mid] == target:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
        
