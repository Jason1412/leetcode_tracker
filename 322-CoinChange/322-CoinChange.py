# Last updated: 5/16/2026, 12:28:27 PM
import sys
class Solution:
# Method 3 ====================================================
    def coinChange(self, coins: List[int], amount: int) -> int:

        self.memo = [amount + 100 for _ in range(amount+1)]

        self.memo[0] = 0

        for i in range(1, len(self.memo)):
            for coin in coins:
                if i - coin >= 0:
                    self.memo[i] = min(self.memo[i], 1+self.memo[i-coin])
                else:
                    continue
                
        if self.memo[amount] == amount + 100:
            return -1
        else:
            return self.memo[amount]



# Method 2 ====================================================
# Recursive + Memo
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     self.memo = [-666 for _ in range(amount+1)]

    #     return self.dp(coins, amount)



    # def dp(self, coins, amount):

    #     if amount == 0:
    #         self.memo[amount] = 0
    #         return 0
    #     if amount < 0:
    #         return -1
    #     if self.memo[amount] != -666:
    #         return self.memo[amount]

    #     res = sys.maxsize

    #     for coin in coins:
    #         tmp = self.dp(coins, amount - coin)
    #         if tmp == -1:
    #             continue

    #         res = min(res, 1 + tmp)
 
        
    #     if res == sys.maxsize:
    #         self.memo[amount] = -1
    #         return -1
    #     else:
    #         self.memo[amount] = res
    #         return res



# Method 1 ====================================================
# Recursive Method

    # def coinChange(self, coins: List[int], amount: int) -> int:
        
    #     if amount == 0:
    #         return 0

    #     if amount < 0:
    #         return -1

    #     res = sys.maxsize

    #     for coin in coins:
    #         tmp = self.coinChange(coins, amount-coin)
    #         if tmp == -1:
    #             continue

    #         res = min(res, 1+tmp)

    #     if res == sys.maxsize:
    #         return -1
    #     else:
    #         return res
