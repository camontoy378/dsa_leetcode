import heapq

class SortColors():

    def __init__(self, nums):
        self.nums   = nums

    def solve(self):

        nums = self.nums

        count_colors = {}

        for color in nums:

            if color in count_colors:
                count_colors[color] += 1
            else:
                count_colors[color] = 1

        index = 0
        for color in range(3):
            if color in count_colors:
                while( count_colors[color] > 0 ):
                    nums[index] = color
                    count_colors[color] -= 1
                    index += 1 

        return nums
        