# Last updated: 5/16/2026, 12:28:32 PM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sum = [0 for num in nums]

        for i in range(len(nums)):
            if i == 0:
                self.pre_sum[i] = nums[i]

            self.pre_sum[i] = self.pre_sum[i-1] + nums[i]
            

    def sumRange(self, left: int, right: int) -> int:

        return self.pre_sum[right] - self.pre_sum[left] + self.nums[left]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)