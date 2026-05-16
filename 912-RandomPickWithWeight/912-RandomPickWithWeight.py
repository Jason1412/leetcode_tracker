# Last updated: 5/16/2026, 12:26:30 PM
from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [0 for _ in range(len(w)+1)]

        for i in range(len(w)):
            self.preSum[i+1] = self.preSum[i] + w[i]

        self.w = w

    def pickIndex(self) -> int:
        start = self.preSum[1]
        end = self.preSum[-1]

        rand_num = randint(1, end)

        # find the index of first number in self.preSum 
        # >= rand_num
        ind = self.bsearch(self.preSum, 1, len(self.preSum)-1, rand_num)

        return ind - 1
    
    def bsearch(self, arr, start, end, target):
        left = start
        right = end

        while (left + 1 < right):
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid
            elif arr[mid] > target:
                right = mid

        if arr[left] >= target:
            return left
        else:
            return right


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()