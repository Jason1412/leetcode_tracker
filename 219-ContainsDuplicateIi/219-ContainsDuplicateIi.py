# Last updated: 5/16/2026, 12:28:53 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0
        window = set()

        while right < len(nums):
            
            if nums[right] in window:
                return True

            window.add(nums[right])
            right += 1

            if right - left > k:
                window.remove(nums[left])
                left += 1
        return False
            



# Method 1 ===========================================================
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
    #     numToInd = {}
    #     for i in range(len(nums)):
            
    #         if nums[i] in numToInd:
    #             diff = i - numToInd[nums[i]]
    #             if diff <= k:
    #                 return True
    #             else:
    #                 numToInd[nums[i]] = i
    #         else:
    #             numToInd[nums[i]] = i

    #     return False