# Last updated: 5/16/2026, 12:25:32 PM
class Solution:
    def minInsertions(self, s: str) -> int:
        

        stack = []
        num_insert = 0
        need_right = 0

        for char in s:

            if char == '(':
                need_right += 2
                if need_right % 2 == 1:
                    need_right -= 1
                    num_insert += 1
                
            if char == ')':
                need_right -= 1
                if need_right == -1:
                    num_insert += 1
                    need_right = 1

        return num_insert + need_right

