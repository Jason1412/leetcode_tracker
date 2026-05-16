# Last updated: 5/16/2026, 12:28:42 PM
class Solution:



    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):

            c = expression[i]

            if c == '-' or c == '+' or c == '*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                for l in left:
                    for r in right:
                        if c == '-':
                            res.append(l - r)
                        elif c == '+':
                            res.append(l + r)
                        elif c == '*':
                            res.append(l * r)

        if not res:
            res.append(int(expression))


        return res

