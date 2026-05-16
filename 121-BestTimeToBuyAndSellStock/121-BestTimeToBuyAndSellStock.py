# Last updated: 5/16/2026, 12:29:41 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        
        lower = prices[0]
        max_val = 0

        for i in range(1, len(prices)):
            profit = prices[i] - lower
            if profit > max_val:
                max_val = profit
            
            if prices[i] < lower:
                lower = prices[i]

        return max_val



# Method 2 ===========================================================
    # def maxProfit(self, prices: List[int]) -> int:   
    #     n = len(prices)
    #     # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
    #     dp_i_0, dp_i_1 = 0, float('-inf')
    #     for i in range(n):
    #         # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    #         dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]), max(dp_i_1, -prices[i])
    #     return dp_i_0



# Method 1 ===========================================================
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     dp = [[-1 for _ in range(2)] for _ in range(n)]

        
    #     # base case 
    #     # dp[-1][0] = 0
    #     # dp[-1][1] = - Inf
        

    #     for i in range(n):
    #         if i == 0:
    #             dp[0][0] = 0
    #             dp[0][1] = - prices[0]
    #         else:
    #             # print("i=", i)
    #             dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    #             dp[i][1] = max(dp[i-1][1], - prices[i])

    #     return dp[n-1][0]
        

    