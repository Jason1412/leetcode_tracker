# Last updated: 5/16/2026, 12:29:26 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:


        self.track = []
        self.res = []
        self.wordDict = set(wordDict)

        self.dfs(s, 0)
        return self.res

    def dfs(self, s, i):

        if i == len(s):
            self.res.append(' '.join(self.track))
            return

        for j in range(i, len(s)+1):

            prefix = s[i:j]

            if prefix in self.wordDict:
                self.track.append(prefix)
                self.dfs(s, j)
                self.track.pop()

        return 



# Method 3 ========================================================
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
 

    #     self.track = []
    #     self.res = []
    #     self.wordDict = set(wordDict)

    #     self.dfs(s, 0)
    #     return self.res

    # def dfs(self, s, i):

    #     if i == len(s):
    #         self.res.append(' '.join(self.track))
    #         return

    #     for word in self.wordDict:

    #         l = len(word)

    #         if i + l <= len(s) and s[i:i+l] == word:
    #             self.track.append(s[i:i+l])
    #             self.dfs(s, i+l)
    #             self.track.pop()

    #     return 



# Method 2 ==========================================================
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    
#         self.wordDict = set(wordDict)

#         self.memo = [None for _ in range(len(s))]

#         return self.dp(s, 0)


#     def dp(self, s, i):
#         res = []

#         if i == len(s):
#             res.append("")
#             return res

#         if self.memo[i]:
#             return self.memo[i]


#         # for length in range(1, len(s)-i+1):
            
#         #     prefix = s[i:i+length]
#         for j in range(i+1, len(s)+1):
#             prefix = s[i:j]
#             if prefix in self.wordDict:    
                
#                 subproblem = self.dp(s, j)

#                 for sub in subproblem:
#                     if sub == '':
#                         res.append(prefix)
#                     else:
#                         res.append(prefix + " " + sub)

                
#         self.memo[i] = res 
#         return res



# # Method 1 ========================================================
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    
#         self.wordDict = set(wordDict)

#         self.memo = [None for _ in range(len(s))]

#         return self.dp(s, 0)


#     def dp(self, s, i):
#         res = []

#         if i == len(s):
#             res.append("")
#             return res

#         if self.memo[i]:
#             return self.memo[i]


#         for length in range(1, len(s)-i+1):
            
#             prefix = s[i:i+length]
#             if prefix in self.wordDict:    
                
#                 subproblem = self.dp(s, i+length)

#                 for sub in subproblem:
#                     if sub == '':
#                         res.append(prefix)
#                     else:
#                         res.append(prefix + " " + sub)

                
#         self.memo[i] = res 
#         return res