class MinSizeSubarraySum():
    
    def __init__(self, nums, target):
        self.nums   = nums
        self.target = target

    def solve(self):

        #Sliding Windows

        nums    = self.nums
        target  = self.target

        i = j = 0
        sum             = nums[j]
        MAX_ARRAY_SIZE  = 10**5 
        output          = MAX_ARRAY_SIZE + 1 

        print(f"Output = {output}")

        while ( j < len(nums) ):

            if (sum >= target):
                output = min( output, (j - i + 1))

                if (i == j) :
                    i += 1
                    j += 1
                    if ( j < len(nums) ):
                        sum = nums[j]
                else:
                    sum -= nums[i]
                    i += 1
            else:
                j   += 1
                if ( j < len(nums) ):
                    sum += nums[j]

        if (output == MAX_ARRAY_SIZE + 1):
            return 0
        else:
            return output
