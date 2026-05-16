# Last updated: 5/16/2026, 12:25:53 PM
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        nums = [0] * 1001
        df = Difference(nums)

        for trip in trips:
            numPassengers = trip[0]
            i = trip[1]
            j = trip[2]

            df.increment(i, j-1, numPassengers)

        res = df.result()

        for i in range(len(res)):
            if capacity < res[i]:
                return False
            
        return True


class Difference:
    def __init__(self, nums):
        assert len(nums) > 0
        self.diff = [0] * len(nums)

        self.diff[0] = nums[0]

        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i-1]


    def increment(self, i, j, val):
        self.diff[i] += val
        
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val


    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]

        for i in range(1, len(self.diff)):
            res[i] = res[i-1] + self.diff[i]

        return res


    
