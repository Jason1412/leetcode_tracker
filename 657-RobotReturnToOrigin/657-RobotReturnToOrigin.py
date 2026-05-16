# Last updated: 5/16/2026, 12:27:15 PM
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        x = 0
        y = 0
        for char in moves:
            if char == 'R':
                x += 1
            elif char == 'L':
                x -= 1
            elif char == 'U':
                y += 1
            elif char == 'D':
                y -= 1
        
        if x == 0 and y == 0:
            return True
        else:
            return False