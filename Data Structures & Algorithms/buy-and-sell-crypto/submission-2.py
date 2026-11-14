class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # SLIDING WINDOW!!!!
        start = 0
        profit = 0

        # Window is as follows
        # buy is start of our window
        # end is current index
        # We move window if sell is smaller than buy


        for end in range(len(prices)):
            # Move window
            if prices[end] < prices[start]:
                start = end

            else:
                profit = max(profit, prices[end] - prices[start])

        return profit