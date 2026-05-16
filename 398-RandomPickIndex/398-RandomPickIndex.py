# Last updated: 5/16/2026, 12:28:10 PM
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.dict_nums = defaultdict(list)

        for i in range(len(nums)):
            self.dict_nums[nums[i]].append(i)


    def pick(self, target: int) -> int:
        return random.choice(self.dict_nums[target])




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)