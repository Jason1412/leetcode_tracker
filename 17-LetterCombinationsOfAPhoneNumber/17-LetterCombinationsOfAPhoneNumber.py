# Last updated: 5/16/2026, 12:30:51 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            
            return []

        mappings = {2: 'abc',
                    3: 'def',
                    4: 'ghi',
                    5: 'jkl',
                    6: 'mno',
                    7: 'pqrs',
                    8: 'tuv',
                    9: 'wxyz'}


        self.res = []

        self.track = []

        self.dfs(digits, 0, mappings)

        return self.res

    def dfs(self, digits, start, mappings):

        n = len(digits)

        if len(self.track) == n:
            self.res.append(''.join(self.track))

        for i in range(start, n):

            for char in mappings[int(digits[i])]:

                self.track.append(char)

                self.dfs(digits, i + 1, mappings)

                self.track.pop()

        
        
