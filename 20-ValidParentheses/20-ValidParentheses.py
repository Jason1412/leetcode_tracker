# Last updated: 5/16/2026, 12:30:48 PM
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
                
            if c in ")]}":
                if stack:
                    left = stack.pop()
                    if left == self.findLeft(c):
                        continue
                    else:
                        return False

                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

    
    def findLeft(self, right):
        if right == ")":
            return "("
        if right == "]":
            return "["
        if right == "}":
            return "{"