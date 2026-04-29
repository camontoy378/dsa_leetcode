class CoinChange():

    def __init__(self, coins, amount):
        self.coins  = coins
        self.amount = amount

    def get_num_coins(self, amount, num_coins, index, coins):
        
        #End conditions
        if amount < 0:
            num_coins   -= 1
            return False, num_coins
        if index < 0:
            num_coins = -1
            return False, num_coins
        if amount == 0:
            return True, num_coins
        
        #Work
        new_amount  = amount - coins[index]
        num_coins   += 1

        #If found keep going on same branch
        found, num_coins = self.get_num_coins(new_amount, num_coins, index, coins)

        #If not found, try different branch
        if not found:
            found, num_coins = self.get_num_coins(amount, num_coins, index - 1, coins)

        return found, num_coins

    def solve(self):

        coins       = self.coins
        amount      = self.amount

        num_coins   = 0
        index = len(coins) - 1

        found, amount = self.get_num_coins(amount, num_coins, index, sorted(coins))

        if found:
            return amount

        return -1