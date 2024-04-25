from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = min(prices)
        min_index = prices.index(min_price)

        if min_index + 1 >= len(prices):
            return 0  

        if prices[min_index + 1] >= min_price:
            max_price = max(prices[min_index + 1:])
            return max_price - min_price

        return 0



solution = Solution()
teste = list[7,5,4,3,2,1,0]
print(solution.maxProfit(teste))