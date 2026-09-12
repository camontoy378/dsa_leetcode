class SummaryRanges():

    def __init__(self, nums):
        self.nums = nums

    def solve(self):

        nums = self.nums

        if nums == []:
            return nums

        l_num   = nums[0]
        output  = []

        for i in range( len(nums) ) :
            
            #Append number to output
            if ( (i + 1) >= len(nums) ):
                
                if ( l_num == nums[i] ):
                    output.append(str(l_num))
                else:
                    output.append(str(l_num) + "->" + str(nums[i]))
                    
            elif ( nums[i] != (nums[i + 1] - 1) ):

                if ( l_num == nums[i] ):
                    output.append(str(l_num))
                else:
                    output.append(str(l_num) + "->" + str(nums[i]))

                #Reset left number
                if ( (i + 1) < len(nums) ):
                    l_num = nums[i + 1]

        return output