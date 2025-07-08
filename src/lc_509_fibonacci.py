class FibonacciNumber():

    def __init__(self, n):
        self.n  = n

    def fib_sum(self,n):
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        return self.fib_sum(n - 1) + self.fib_sum(n - 2)


    def solve(self):
        return self.fib_sum(self.n)
        