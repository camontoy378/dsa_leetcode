class ContainsDuplicate():

    def __init__(self, nums, k):
        self.nums   = nums
        self.k      = k

    def solve(self):

        nums        = self.nums
        k           = self.k

        nums_dict   = {}
        arr_size    = len(nums)

        for i in range(arr_size):
            print(f"i = {i}")

            if( nums[i] in nums_dict):

                #Test for duplicate within K
                if ( ( i - nums_dict[nums[i]][-1]) <= k):
                    return True
                else:
                    nums_dict[nums[i]].append(i)

            else:
                nums_dict[nums[i]] = [i]

        return False