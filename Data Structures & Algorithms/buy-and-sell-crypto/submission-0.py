class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimo = prices[0]
        profit=0
        for n in prices[1:]:
            minimo = min(minimo,n)
            profit = max(profit,n-minimo)
        return profit