class PowerOfTwo():

    def __init__(self, n):
        self.n  = n

    def power_of_two(self, n):
        
        if n == 1.0:
            return True
        
        if n < 1.0:
            return False
        
        return self.power_of_two(n/2)

    def solve(self):

        return self.power_of_two(self.n)