# Last updated: 5/16/2026, 12:29:36 PM
from collections import defaultdict
class Solution:
    def __init__(self):
        self.adjList = defaultdict(list)
        self.currPath = []
        self.shortestPath = []
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        distance = {}

        self.bfs(beginWord, endWord, wordSet, distance)

        print(distance)
        print(self.adjList)

        self.currPath = [endWord]
        self.dfs(endWord, beginWord)

        return self.shortestPath


    def bfs(self, beginWord, endWord, wordSet, distance):

        queue = deque([beginWord])
        distance[beginWord] = 0
        wordSet.discard(beginWord)
        

        while queue:
            visited = []
            for _ in range(len(queue)):
                word = queue.popleft()
                neighbors = self.getNextWords(word, wordSet)
                for neighbor in neighbors:
                    self.adjList[neighbor].append(word)
                    visited.append(neighbor)

                    if neighbor not in distance:
                        queue.append(neighbor)
                        distance[neighbor] = distance[word] + 1
            for w in visited:
                wordSet.discard(w)


    def dfs(self, source, target):
        if source == target:
            tmp = self.currPath.copy()
            tmp.reverse()
            self.shortestPath.append(tmp)
            return

        if source not in self.adjList:
            return
        
        for word in self.adjList[source]:
            self.currPath.append(word)
            self.dfs(word, target)
            self.currPath.pop()


    def getNextWords(self, word, wordSet):

        n = len(word)
        out = []

        for i in range(n):
            left, right = word[:i], word[i+1:]

            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue
                new_word = left + c + right
                if new_word in wordSet:
                    out.append(new_word)

        return out

    