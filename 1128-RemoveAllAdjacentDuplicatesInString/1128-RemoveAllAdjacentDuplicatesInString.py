# Last updated: 5/16/2026, 12:25:55 PM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if len(stack) == 0 or stack[-1] != char:
                stack.append(char)

            elif stack[-1] == char:
                stack.pop()

        return ''.join(stack)