# Last updated: 5/16/2026, 12:29:06 PM
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        K = k
        N = len(prices)

        dp = [[[0 for _ in range(2)] for _ in range(K+1)] for _ in range(N)]

        for i in range(N):
            dp[i][0][1] = - sys.maxsize

        for i in range(N):
            for k in range(K, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = - prices[0]
                else: 
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                
        return dp[N-1][K][0]