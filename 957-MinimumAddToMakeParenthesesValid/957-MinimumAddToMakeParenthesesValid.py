# Last updated: 5/16/2026, 12:26:24 PM
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        
        if not s:
            return 0


        stack = []

        need = 0
        for char in s:
            if char == '(':
                stack.append(char)

            if char == ')':
                if stack:
                    stack.pop()
                else:
                    need += 1

        return need + len(stack)
        
            