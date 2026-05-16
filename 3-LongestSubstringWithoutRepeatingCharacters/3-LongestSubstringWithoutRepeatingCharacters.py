# Last updated: 5/16/2026, 12:30:55 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = {}

        left, right = 0, 0
        maxLen = 0


        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            if window[c] == 1:
                maxLen = max(maxLen, right - left)

            while window[c] > 1:
                d = s[left]
                left += 1
                
                window[d] -= 1


        return maxLen