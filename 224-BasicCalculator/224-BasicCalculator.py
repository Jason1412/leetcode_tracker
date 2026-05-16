# Last updated: 5/16/2026, 12:28:51 PM
class Solution:
# Method 2 ==============================================================
    def calculate(self, s):
        stack = []
        result = 0
        num = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            if c == "+":
                result += num * sign
                sign = 1
                num = 0

            if c == "-":
                result += num * sign
                sign = -1
                num = 0

            if c == "(":
                stack.append(result)
                stack.append(sign) # sign for the value after result

                sign = 1
                num = 0 # 可有可无应该
                result = 0

            if c == ")":
                result += sign * num

                sign = stack[-1]
                result *= sign
                result += stack[-2]
                stack = stack[:-2]

                num = 0

        result += sign * num

        return result
                

                



# Method 1 ==============================================================
    # def calculate(self, s: str) -> int:

    #     leftToRight = {}
        
    #     stk = []

    #     for i in range(len(s)):
    #         c = s[i]
    #         if c == "(":
    #             stk.append(i)
    #         if c == ")":
    #             leftToRight[stk.pop()] = i

    #     # print(leftToRight)

    #     return self.plus_minus(s, 0, len(s)-1, leftToRight)


    # def plus_minus(self, s, start, end, leftToRight):
        
    #     stack = []
    #     num = 0
    #     sign = 1
    #     i = start

    #     while i <= end:
    #         c = s[i]

    #         if c == "(":
    #             num = self.plus_minus(s, i+1, leftToRight[i]-1, leftToRight)
    #             i = leftToRight[i] # This place cannot be i = leftToRight[i] + 1, because c here is still equal to "(", need to update c first.

    #         if c.isdigit():
    #             num = num * 10 + int(c)

    #         if c in "+-" or i == end:
    #             num *= sign
    #             stack.append(num)

    #             if c == "-":
    #                 sign = -1

    #             if c == "+":
    #                 sign = 1
    #             num = 0

    #         i += 1

    #         if c == " ":
    #             continue

            
    #     return sum(stack)
                

            