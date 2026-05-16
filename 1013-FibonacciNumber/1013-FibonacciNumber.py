# Last updated: 5/16/2026, 12:26:15 PM
class Solution:

# Method 3 =========================================
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        prev2 = 0
        prev1 = 1

        for i in range(2, n+1):
            out = prev1 + prev2
            prev2 = prev1
            prev1 = out
            

        return out


# Method 2 =========================================
    # def fib(self, n: int) -> int:
        
    #     if n == 0 or n == 1:
    #         return n
        
    
    #     data = [-1 for _ in range(n+1)]
    
    #     data[0] = 0
    #     data[1] = 1

    #     for i in range(2,n+1):
    #         data[i] = data[i-1] + data[i-2]

    #     return data[n]
        

        





# Method 1 =========================================
    # def fib(self, n: int) -> int:
    #     self.memo = [-1 for _ in range(n+1)]
    #     return self.dp(n)
    
    # Warning: 
    # 因为创建memo的时候需要知道n的值, 所以memo没法在__init__中创建,
    # 所以memo在fib()里面创建, 然后需要另一个function来完成recursion

    # def dp(self, n):     
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1

    #     if self.memo[n] != -1:
    #         return self.memo[n]

    #     self.memo[n] = self.dp(n-2) + self.dp(n-1)

    #     return self.memo[n]

