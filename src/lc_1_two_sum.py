class TwoSum:
    
    def __init__(self):
            pass
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:

          arr_hash = {}

          for i in range(len(nums)):
                 curr_num   = nums[i]
                 needed_num = target - curr_num

                 if( needed_num in arr_hash):
                       return [arr_hash[needed_num], i]
                 else:
                       #Save num and index in hash map
                       arr_hash[curr_num] = i
                 
          return [0,0]

