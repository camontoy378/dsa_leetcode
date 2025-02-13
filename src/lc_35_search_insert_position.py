
class SearchInsertPosition():

    def __init__(self, nums_list, target_num):
        self.nums_list  = nums_list
        self.target_num = target_num

    def solve(self):

        #Initialize pointers
        index_low   = 0
        index_high  = len(self.nums_list) - 1
        index_mid   = int((index_high - index_low)/2)

        
        #binary search
        while index_low <= index_high:

            if self.nums_list[index_mid] == self.target_num:
                return index_mid
            elif self.nums_list[index_low] == self.target_num:
                return index_low
            elif self.nums_list[index_high] == self.target_num:
                return index_high
            elif self.target_num < self.nums_list[index_mid]:
                index_high  = index_mid - 1
                index_mid   = int((index_high + index_low)/2)
            else:
                index_low   = index_mid + 1
                index_mid   = int((index_high + index_low)/2)

        if index_high == len(self.nums_list) - 1:
            return len(self.nums_list)
        elif self.target_num <= self.nums_list[index_low]:
            return index_low
        else:
            return index_low + 1