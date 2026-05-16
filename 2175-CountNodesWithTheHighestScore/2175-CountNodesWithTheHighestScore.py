# Last updated: 5/16/2026, 12:25:19 PM
class Solution:
    def __init__(self):
        self.tree = None
        self.scoreToCount = {}

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.tree = self.buildTree(parents)
        self.countNode(0)

        maxScore = 0

        for score in self.scoreToCount.keys():
            maxScore = max(maxScore, score)

        return self.scoreToCount[maxScore]
    
    def countNode(self, root):
        if root == -1:
            return 0

        n = len(self.tree)
        leftCount = self.countNode(self.tree[root][0])
        rightCount = self.countNode(self.tree[root][1])

        otherCount = n - leftCount - rightCount - 1

        score = max(leftCount, 1) * max(rightCount, 1) * max(otherCount, 1)
        if score in self.scoreToCount:
            self.scoreToCount[score] += 1
        else:
            self.scoreToCount[score] = 1
        
        return leftCount + rightCount + 1


    def buildTree(self, parents):
        n = len(parents)

        tree = [[-1, -1] for _ in range(n)]

        for i in range(1, n):
            parent_i = parents[i]
            if tree[parent_i][0] == -1:
                tree[parent_i][0] = i
            else:
                tree[parent_i][1] = i
        return tree