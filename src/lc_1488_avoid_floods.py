import heapq

class AvoidFloods():

    def __init__(self, rains):
        self.rains  = rains
    
    def middle(self, left_num, right_num):
        return int( (right_num + left_num) / 2)
    
    #Binary search algorithm
    def pop_index_of_next_available_dry_day(self, dry_arr, number):

        left_index      = 0
        right_index     = len(dry_arr) - 1
        middle_index    = self.middle(left_index, right_index)

        while True:
            if left_index == right_index:
                if number < dry_arr[left_index]:
                    #Return earliest dry day
                    return dry_arr.pop(left_index)
                else:
                    return 0
            elif number < dry_arr[middle_index]:
                right_index     = middle_index
                middle_index    = self.middle(left_index, right_index)
            elif number > dry_arr[middle_index]:
                left_index      = middle_index + 1
                middle_index    = self.middle(left_index, right_index)
            else:
                return 0



    def solve(self):

        rains               = self.rains
        full_lakes_hash     = {}
        dry_days_index_list = []
        output              = [1] * len(rains)
        
        for index in range(len(rains)):

            #Store indexes of dry days.
            if rains[index] == 0:
                dry_days_index_list.append(index)
                continue

            #Track full lake
            if rains[index] not in full_lakes_hash:
                full_lakes_hash[rains[index]] = index
                output[index] = -1
                continue

            #Check if any dry days available to dry/empty lake
            if (len(dry_days_index_list) == 0):
                return []

            next_available_dry_day_index = self.pop_index_of_next_available_dry_day(dry_days_index_list, full_lakes_hash[rains[index]])

            if next_available_dry_day_index > 0:
                output[next_available_dry_day_index] = rains[index]
                output[index] = -1
                full_lakes_hash.pop(rains[index])
                full_lakes_hash[rains[index]] = index

            else:
                return []
                    
        return output