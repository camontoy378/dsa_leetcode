class SingleNumber():

    def __init__(self, nums: list[int] ):
        self.nums   = nums

    def solve(self):

        nums  = self.nums

        nums_dict = {}

        for num in nums:

            if num in nums_dict:
                nums_dict.pop(num)
            else:
                nums_dict[num] = 1

        return nums_dict.popitem()[0]