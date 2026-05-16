# Last updated: 5/16/2026, 12:25:43 PM
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = [['#', 0]]


        for char in s:

            if char == stack[-1][0]:
                if stack[-1][1] < k-1:
                    stack[-1][1] += 1
                
                elif stack[-1][1] == k-1:
                    stack.pop()

            else:
                stack.append([char, 1])

        
        out = []
        for i in range(1, len(stack)):
            out.append(stack[i][0] * stack[i][1])

        return ''.join(out)
