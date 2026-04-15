class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0]=0

        for c in coins:
            dp[c] = 1
        
        for i in range(amount+1):
            if i not in dp:
                minimo = float('inf')
                for j in coins:
                    if i-j in dp:
                        minimo = min(minimo, dp[i-j])
                dp[i]= minimo+1
        
        result =dp[amount]
        return result if result!=float('inf') else -1