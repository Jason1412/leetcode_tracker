# Last updated: 5/16/2026, 12:29:05 PM
class Solution:

# Method 2 =========================================================
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        n = len(nums)

        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)

    
    def reverse(self, nums, start, end):
        start = start
        end = end

        while (start <= end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        




# Method 1 =========================================================
# pop, insert
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
        
    #     k_eff = k % len(nums)
        
    #     for i in range(k_eff):
    #         tmp = nums.pop()
    #         nums.insert(0, tmp)

    #     return nums