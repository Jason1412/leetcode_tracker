# Last updated: 5/16/2026, 12:25:42 PM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        list_s = list(s)
        stack = []

        for i in range(len(list_s)):
            if list_s[i] == "(":
                stack.append(list_s[i])
            
            if list_s[i] == ")":
                if not stack:
                    list_s[i] = "*"
                else:
                    stack.pop()


        stack2 = []
        for i in range(len(list_s)-1, -1, -1):
            if list_s[i] == ")":
                stack2.append(list_s[i])

            if list_s[i] == "(":
                if not stack2:
                    list_s[i] = "*"
                else:
                    stack2.pop()

        return "".join([char for char in list_s if char != "*"])


        

            
