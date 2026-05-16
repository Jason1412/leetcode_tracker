# Last updated: 5/16/2026, 12:25:30 PM
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x

        left, right = 0, 0
        max_len = - float(inf)
        window_sum = 0

        while right < n:
            window_sum += nums[right]
            right += 1


            while window_sum > target and left < right:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                max_len = max(max_len, right - left)


        if max_len == -float(inf):
            return -1
        else:
            return n - max_len