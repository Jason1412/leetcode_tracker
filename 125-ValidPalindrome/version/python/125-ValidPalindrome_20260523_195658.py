# Last updated: 5/23/2026, 7:56:58 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s_processed = []
4
5        for c in s:
6            if c.isalnum():
7                s_processed.append(c.lower())
8
9
10        s_str = ''.join(s_processed)
11
12        left = 0
13        right = len(s_str) - 1
14
15        while left <= right:
16            if s_str[left] != s_str[right]:
17                return False
18
19            left += 1
20            right -= 1
21
22        return True