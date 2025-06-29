class ContainsDuplicate():

    def __init__(self, nums_array):
        self.nums_array = nums_array

    def solve(self):

        seen_nums = []

        for num in self.nums_array:
            if num in seen_nums:
                return True
            
            seen_nums.append(num)

        return False
        