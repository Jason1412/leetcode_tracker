# Last updated: 5/16/2026, 12:27:05 PM
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        dp = [[-1 for _ in range(2)] for _ in range(N)]

        for i in range(N):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = - prices[0]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]-fee)
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[N-1][0]



# Method 1 ============================================================
# Pay the fee when buying
    # def maxProfit(self, prices: List[int], fee: int) -> int:
    #     N = len(prices)

    #     dp = [[-1 for _ in range(2)] for _ in range(N)]

    #     for i in range(N):
    #         if i == 0:
    #             dp[i][0] = 0
    #             dp[i][1] = - prices[0] - fee
    #         else:
    #             dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    #             dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)

    #     return dp[N-1][0]