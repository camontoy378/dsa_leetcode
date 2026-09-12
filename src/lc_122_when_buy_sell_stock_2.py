class WhenBuySellStockTwo():

    def __init__(self, prices):
        self.prices = prices

    def solve(self):

        prices = self.prices

        #Set initial values
        profit  = 0
        low     = prices[0] + 1 
        high    = prices[0] + 1

        for i in range(len(prices)):
            print(f"price = {prices[i]}")

            if prices[i] > high:
                high = prices[i]

            #Sell when prices drop or you reach last price
            if (prices[i] < high) or (i == len(prices) - 1):
                profit += (high - low)
                low = high = prices[i]

        return profit