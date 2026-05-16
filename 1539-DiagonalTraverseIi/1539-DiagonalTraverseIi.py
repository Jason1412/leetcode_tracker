# Last updated: 5/16/2026, 12:25:36 PM
from collections import defaultdict

class Solution:
# Method 1 ===============================================
    # def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
    #     dd = defaultdict(list)
        
    #     for i in range(len(nums)):
    #         for j in range(len(nums[i])):
    #             dd[i+j].append(nums[i][j])

    #     # for k, v in dd.items():
    #     #     v.reverse()
    #     #     out.extend(v)

    #     curr = 0
    #     out = []
    #     while curr in dd:
    #         dd[curr].reverse()
    #         out.extend(dd[curr])
    #         curr += 1


    #     return out

# Method 2 ===================================================
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        queue = deque([(0,0)])
        ans = []

        while queue:
            i, j = queue.popleft()
            ans.append((nums[i][j]))
            
            if i < len(nums) - 1 and j == 0:
                queue.append((i+1, j))

            if j < len(nums[i]) - 1:
                queue.append((i, j+1))

        return ans