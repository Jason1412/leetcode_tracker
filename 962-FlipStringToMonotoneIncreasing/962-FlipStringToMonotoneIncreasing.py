# Last updated: 5/16/2026, 12:26:23 PM
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        dp = [-1 for _ in range(len(s))]

        # m --- number of times flip 1 to 0, at position i
        # n --- number of times flip 0 to 1, at position i
        m, n = 0, 0

        for i in range(len(s)):
            m += int(s[i])
            n += 1 - int(s[i])

            if i == 0:
                dp[i] = min(m, n)
            else:
                dp[i] = min(m, dp[i-1] + 1 - int(s[i]))


        return dp[-1]