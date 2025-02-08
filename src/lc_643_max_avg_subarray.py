
class MaxAvgSubarray():

    def __init__(self, nums_list, k):
        self.nums_list  = nums_list
        self.k          = k

    def solve(self):

        total = 0
        nums    = self.nums_list
        k       = self.k

        #Initial average
        for i in range(k):
            total += nums[i]

        avg         = total / k
        current_avg = avg
        max_avg     = avg

        #Max average
        for i in range(k, len(nums)):
            print(nums[i])
            print(nums[i-k])

            current_avg = current_avg + (nums[i]/k) - (nums[i-k]/k)
            max_avg = max(max_avg, current_avg)


        return max_avg