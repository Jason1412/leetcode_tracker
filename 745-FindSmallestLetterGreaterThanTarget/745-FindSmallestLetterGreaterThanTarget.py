# Last updated: 5/16/2026, 12:27:00 PM
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if len(letters) == 0:
            return -1
        
        start = 0
        end = len(letters) - 1
        
        if target < letters[start]:
            return letters[start]
        
        if target >= letters[end]:
            return letters[start]
        
        while (start + 1) < end:
            mid = (end - start)//2 + start
            
            if letters[mid] < target:
                start = mid
            elif target < letters[mid]:
                end = mid
            elif target == letters[mid]:
                start = mid

        if (target < letters[end]) & (letters[start] <= target):
            return letters[end]
        else:
            return letters[start]
            
            
            
            