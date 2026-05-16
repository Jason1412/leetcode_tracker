# Last updated: 5/16/2026, 12:26:03 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        res = 0
        slow, fast = 0, 0
        count = 0

        while fast < len(nums) and count <= k:
            if nums[fast] == 0:
                count += 1
            fast += 1
            
            while count > k:
                if nums[slow] == 0:
                    count -= 1
                slow += 1
            
            res = max(fast - slow, res)
            

        

        return res
