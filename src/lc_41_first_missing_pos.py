class Solution:

    def __init__(self):
        pass

    def firstMissingPositive(self, nums):

        is_1_seen = False

        #Set invalid numbers in array to 1
        for i in range(0,len(nums)):

            if(nums[i] == 1):
                is_1_seen = True

            elif ((nums[i] < 1) or (nums[i] > len(nums))):
                nums[i] = 1;

        if not is_1_seen:
            return 1

        #Use array as hash table and mark seen numbers as negative
        for i in range(0,len(nums)):
            if (abs(nums[i]) == len(nums)):
                nums[0] = abs(nums[i]) * -1
            else:
                nums[abs(nums[i])] = abs(nums[abs(nums[i])]) * -1

        #Search for missing positive
        for i in range(1,len(nums)):
            if (nums[i] > 0):
                return i

        #Search for missing positive
        if(nums[0] > 0):
            return len(nums)
        else:
            return len(nums) + 1
