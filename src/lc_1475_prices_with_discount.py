class PricesWithDiscount():
    
    def __init__(self, prices):
        self.prices = prices

    def solve(self):
        
        prices      = self.prices
        arr_len     = len(prices)
        stack       = []
        #top of stack = stack[-1]

        for index in range(0,arr_len):
            if (len(stack) == 0) or  (prices[index] > prices[ stack[-1] ]):
                stack.append(index)
            else:    
                while (len(stack) > 0) and (prices[index] <= prices[ stack[-1] ]):
                    prices[ stack[-1] ] = prices[ stack[-1] ] - prices[index]
                    stack.pop()
                
                stack.append(index)

        return prices