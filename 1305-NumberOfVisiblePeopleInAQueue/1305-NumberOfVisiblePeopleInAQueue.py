# Last updated: 5/16/2026, 12:25:43 PM
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        

        stack = []
        n = len(heights)
        res = []

        for i in range(n-1, -1, -1):
            count = 0

            if i == n-1:
                count = 0

            while stack and heights[i] > stack[-1]:
                count += 1
                stack.pop()
            
            if stack and heights[i] < stack[-1]:
                count += 1    

            stack.append(heights[i])
            
            res.append(count)

        res.reverse()
        return res