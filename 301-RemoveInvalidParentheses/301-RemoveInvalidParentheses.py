# Last updated: 5/16/2026, 12:28:33 PM
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        invalidLeft = 0 
        invalidRight = 0

        for char in s:
            if char == '(':
                invalidLeft += 1

            if char == ')':
                if invalidLeft > 0:
                    invalidLeft -= 1
                else:
                    invalidRight += 1        

        self.res = []

        self.dfs(s, invalidLeft, invalidRight, 0)

        return self.res


    def dfs(self, s, invalidLeft, invalidRight, start):
        
        if invalidLeft == 0 and invalidRight == 0:
            if self.isValid(s):
                self.res.append(s)
            return

        if start > len(s)-1:
            return

        
        for i in range(start, len(s)):
            char = s[i]

            if i > start and s[i] == s[i-1]:
                continue

            if char == '(' and invalidLeft > 0:
                self.dfs(s[:i]+s[i+1:], invalidLeft-1, invalidRight, i)

            elif char == ')' and invalidRight > 0:
                self.dfs(s[:i]+s[i+1:], invalidLeft, invalidRight-1, i)

    




    


    def isValid(self, s):
        invalidLeft = 0
        invalidRight = 0

        for char in s:
            if char == "(":
                invalidLeft += 1
            
            if char == ")":
                if invalidLeft > 0:
                    invalidLeft -= 1
                else:
                    invalidRight += 1
        
        return invalidLeft == 0 and invalidRight == 0


