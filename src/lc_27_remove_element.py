class RemoveElement():

    def __init__(self, nums, val):
        self.nums   = nums
        self.val    = val

    def remove_element(self, nums, val):

        #Right index
        j   = len(nums) - 1

        count_val = 0

        #Left index
        for i in range(len(nums)):

            if (i > j):
                break

            if nums[i] == val:

                while( ( j  > i) and (nums[j] == val)):
                    j -= 1

                if j > i:
                    nums[i]     = nums[j]
                    nums[j]     = val
                    j           -=1
                    count_val   += 1 

            else:
                count_val += 1

        return count_val

    def solve(self):

        nums    = self.nums
        val     = self.val

        count_val = self.remove_element(nums, val)

        return count_val