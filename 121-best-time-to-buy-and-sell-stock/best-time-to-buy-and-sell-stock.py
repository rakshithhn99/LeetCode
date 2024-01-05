class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        rightMax = [0] * n
        currentMax = rightMax[n-1] = prices[n-1]

        for i in range(n-2,-1, -1):
            print(i)
            if prices[i] > currentMax:
                currentMax = prices[i]
            
            rightMax[i] = currentMax 
        
        profit = 0 
        for i in range(n):
            diff = rightMax[i] - prices[i] 
            if diff > profit:
                profit = diff 
        
        return profit

        