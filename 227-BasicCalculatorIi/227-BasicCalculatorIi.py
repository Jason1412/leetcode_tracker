# Last updated: 5/16/2026, 12:28:50 PM
class Solution:
    def calculate(self, s: str) -> int:
        

        stack = []
        num = 0

        sign = '+'

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = 10 * num + int(char)

            if (not char.isdigit() and char !=' ') or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)

                if sign == '-':
                    stack.append(-num)

                if sign == '*':
                    pre = stack.pop()
                    stack.append(pre * num)
                    print("pre=", pre)

                if sign == '/':
                    pre = stack.pop()
                    stack.append(int(pre / num))

                sign = char
                num = 0
            # print(stack)
        
        # print(stack)

        return sum(stack)

