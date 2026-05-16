# Last updated: 5/16/2026, 12:29:38 PM
import sys
class Solution:

# Method 3 ==========================================================
# k iteration descending
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(N)]

        # for i in range(N):
        #     dp[i][0][1] = - sys.maxsize

        for i in range(N):
            for k in range(2, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = - prices[0]
                else: 
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                
        return dp[N-1][2][0]



# Method 2 ===========================================================
# i, k iteration in ascending order 
    # def maxProfit(self, prices: List[int]) -> int:
    #     N = len(prices)

    #     dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(N)]

    #     for i in range(N):
    #         dp[i][0][1] = - sys.maxsize

    #     for i in range(N):
    #         for k in range(1,3):
    #             if i - 1 == -1:
    #                 dp[i][k][0] = 0
    #                 dp[i][k][1] = - prices[0]
    #             else: 
    #                 dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    #                 dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                
    #     return dp[N-1][2][0]

# Method 1 ===========================================================
# My own base case
    # def maxProfit(self, prices: List[int]) -> int:
        
    #     N = len(prices)

    #     dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(N+1)]

    #     for k in range(3):
    #         dp[0][k][1] = - sys.maxsize

    #     for i in range(N+1):
    #         dp[i][0][1] = - sys.maxsize


    #     for i in range(1,N+1):
    #         for k in range(1,3):
    #             dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
    #             dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])
                
    #     return dp[N][2][0]