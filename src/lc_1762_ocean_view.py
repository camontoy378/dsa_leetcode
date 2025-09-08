class OceanView():

    def __init__(self, heights):
        self.heights = heights

    def solve(self):

        num_heights = len(self.heights)
        tallest     = 0
        stack       = []
        output      = []

        for i in range(num_heights - 1, -1, -1):
            if self.heights[i] > tallest:
                tallest = self.heights[i]
                stack.append(i)
            
        while (len(stack) > 0):
            output.append(stack.pop())

        return output