class RotateArray():

    def __init__(self, nums, k):
        self.nums   = nums
        self.k      = k

    def solve(self):

        nums    = self.nums
        k       = self.k

        num_mem = [0] * len(nums)

        for i in range(len(nums)):

            index_cur   = i
            num_cur     = nums[index_cur]
            
            index_next  = (index_cur + k) % len(nums)
            num_next    = nums[index_next]

            while (num_mem[index_next] < 1):

                #Replace num
                nums[index_next] = num_cur

                #Update table
                num_mem[index_next] = 1

                #Update indexes
                index_cur   = index_next
                num_cur     = num_next

                index_next  = (index_cur + k) % len(nums)
                num_next    = nums[index_next]


        return nums