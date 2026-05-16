# Last updated: 5/16/2026, 12:29:27 PM
class Solution:
# Method 2 ===================================================
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        self.wordDict = set(wordDict)

        self.memo = [-1 for _ in range(len(s))]

        return self.dp(s, 0)


    def dp(self, s, i):

        if i == len(s):
            return True

        if self.memo[i] != -1:
            return self.memo[i]


        for word in self.wordDict:
            l = len(word)
            if s[i:i+l] == word:
                
                subproblem = self.dp(s, i+l)

                if subproblem is True:
                    self.memo[i] = True
                    return True

        self.memo[i] = False
        return False



# Method 1 ====================================================
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
    #     self.wordDict = set(wordDict)

    #     self.memo = [-1 for _ in range(len(s))]

    #     return self.dp(s, 0)


    # def dp(self, s, i):

    #     if i == len(s):
    #         return True

    #     if self.memo[i] != -1:
    #         return self.memo[i]


    #     for length in range(1, len(s)-i+1):

    #         if s[i:i+length] in self.wordDict:
                
    #             subproblem = self.dp(s, i+length)

    #             if subproblem is True:
    #                 self.memo[i] = True
    #                 return True

    #     self.memo[i] = False
    #     return False