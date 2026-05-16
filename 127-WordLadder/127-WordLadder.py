# Last updated: 5/16/2026, 12:29:35 PM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        dist = {beginWord: 1}
        queue = deque([beginWord])
        wordSet = set(wordList)

        while queue:
            word = queue.popleft()
            if word == endWord:
                return dist[word]

            for next_word in self.getNextWords(word):
                if next_word not in dist and next_word in wordSet:
                    queue.append(next_word)
                    dist[next_word] = dist[word] + 1
        
        return 0




    def getNextWords(self, word):

        n = len(word)
        out = []

        for i in range(n):
            left, right = word[:i], word[i+1:]

            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue
                out.append(left + c + right)

        return out
# Method 1 ===========================================================
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
    #     wordSet = set(wordList)

    #     if endWord not in wordSet:
    #         return 0

    #     queue = deque([beginWord])
        
    #     visited = set()
    #     visited.add(beginWord)

    #     steps = 0

    #     while queue:

    #         steps += 1
    #         for i in range(len(queue)):
    #             q = queue.popleft()
                


    #             for word in self.getNextWords(q):
                    
    #                 if word not in wordSet or word in visited:
    #                     continue
                    
    #                 if word == endWord: 
    #                     return steps + 1
    #                 queue.append(word)
    #                 visited.add(word)

    #     return 0


    # def getNextWords(self, word):

    #     n = len(word)
    #     out = []

    #     for i in range(n):
    #         left, right = word[:i], word[i+1:]

    #         for c in 'abcdefghijklmnopqrstuvwxyz':
    #             if c == word[i]:
    #                 continue
    #             out.append(left + c + right)

    #     return out