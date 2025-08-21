class ClimbingStairs():

    def __init__(self, n):
        self.n = n

    def num_ways_climb_stairs(self, steps, values_list):
        
        #Don't calc recursively if values already stored.
        if values_list[steps] != -1:
            return values_list[steps]
        
        if steps <= 2:
            return steps

        sum = self.num_ways_climb_stairs(steps - 1, values_list) + self.num_ways_climb_stairs(steps - 2, values_list)

        #Store value. Can be referenced later.
        values_list[steps] = sum

        return sum 

    def solve(self):

        #Store values for each number of steps. Initialize values
        value_array = [-1] * (self.n + 1)

        result = self.num_ways_climb_stairs(self.n, value_array)

        return result