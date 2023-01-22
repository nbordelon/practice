# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        left = 0
        output = 0

        for x in range(1, len(prices)):

            if prices[x] < prices[left]:
                left = x
                
            profit = prices[x] - prices[left]
            output = max(profit,output)
            
        return output

if __name__ == '__main__':
    # Please separate inputs with an empty space. (1 2 3)
    usrInpt = list(map(int,(input("Enter your test case: ").strip().split())))
    print(Solution().maxProfit(usrInpt))