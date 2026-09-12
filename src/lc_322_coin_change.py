class CoinChange():

    def __init__(self, coins, amount):
        self.coins  = coins
        self.amount = amount

    def get_num_coins(self, amount, num_coins, coins, min_num_coins):
        
        #End conditions
        if amount < 0:
            return min_num_coins
        if amount == 0:
            min_num_coins = min(min_num_coins, num_coins)
            return min_num_coins
        
        #Work
        num_coins   += 1

        #Recursion
        for coin in coins:
            new_amount  = amount - coin
            min_num_coins = self.get_num_coins(new_amount, num_coins, coins, min_num_coins)

        return min_num_coins


    def solve(self):

        coins       = self.coins
        amount      = self.amount

        num_coins   = 0
        min_num_coins   = 10**4

        min_num_coins = self.get_num_coins(amount, num_coins, coins, min_num_coins)

        #if found:
        if min_num_coins != 10**4:
            return min_num_coins

        return -1