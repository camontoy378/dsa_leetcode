class WhenBuySellStock():

    def __init__(self, prices):
        self.prices = prices

    def solve(self):

        min_buy     = self.prices[0]
        profit      = 0

        for todays_price in self.prices:
            if min_buy > todays_price:
                min_buy = todays_price

            if min_buy < todays_price:
                profit = max(profit, (todays_price - min_buy) )

        return profit
        