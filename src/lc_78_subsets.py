
class Subsets():

    def __init__(self, nums):
        self.nums   = nums

    def backtrack(self, index, cur_set, nums, output):
        
        if index >= len(nums):
            return output.append(cur_set)
        
        #Don't include
        self.backtrack(index + 1, cur_set.copy(), nums, output)
        
        #Include
        cur_set.append(nums[index])

        self.backtrack(index + 1, cur_set.copy(), nums, output)

        return output

    def solve(self):

        nums = self.nums

        index       = 0
        cur_set     = []
        output      = []

        return self.backtrack(index, cur_set, nums, output)        
    