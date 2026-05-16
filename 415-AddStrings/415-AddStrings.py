# Last updated: 5/16/2026, 12:28:07 PM
class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        res = ""

        n1, n2 = len(num1), len(num2)

        i, j = n1-1, n2-1

        flag = 0
        while i >= 0 or j >= 0:
            a, b = 0, 0
            if i >= 0:
                a = int(num1[i])
                i -= 1
            if j >= 0:
                b = int(num2[j])
                j -= 1
            
            tmp = a + b + flag

            res = str(tmp % 10) + res
            flag = tmp // 10

        if flag == 1:
            res = str(flag) + res

        return res


# Method 1 ===========================================
    # def addStrings(self, num1: str, num2: str) -> str:
        
    #     out = []
    #     add_one = 0

    #     num1 = num1[::-1]
    #     num2 = num2[::-1]

    #     pt1, pt2 = 0, 0

    #     while pt1 < len(num1) and pt2 < len(num2):
    #         tmp_sum = int(num1[pt1]) + int(num2[pt2]) + add_one
    #         add_one = tmp_sum // 10
    #         digit = tmp_sum % 10
    #         out.append(digit)
            
    #         pt1 += 1
    #         pt2 += 1

    #     while pt1 < len(num1):
    #         tmp_sum = int(num1[pt1]) + add_one
    #         add_one = tmp_sum // 10
    #         digit = tmp_sum % 10
    #         out.append(digit)
            
    #         pt1 += 1
            

    #     while pt2 < len(num2):
    #         tmp_sum = int(num2[pt2]) + add_one
    #         add_one = tmp_sum // 10
    #         digit = tmp_sum % 10
    #         out.append(digit)

    #         pt2 += 1
        
    #     if add_one == 1:
    #         out.append(1)

    #     out.reverse()
    #     return "".join([str(d) for d in out])
            