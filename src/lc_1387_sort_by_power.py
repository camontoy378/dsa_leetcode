import heapq

class SortByPower():

    def __init__(self, lo, hi, k):
        self.lo     = lo
        self.hi     = hi
        self.k      = k

    def get_integer_power(self, steps_dict, num):

        #Stop condition(s)
        if num == 1:
            return 0
        
        #If num in steps_dict then return num
        if num in steps_dict:
            return steps_dict[num] 
        
        #Recursion + work
        if (num % 2) == 0:

            new_num = num / 2
            
            result = 1 + self.get_integer_power(steps_dict, new_num)
            steps_dict[num] = result
            return result

        else:
            new_num = (3 * num) + 1

            result = 1 + self.get_integer_power(steps_dict, new_num)
            steps_dict[num] = result
            return result


    def solve(self):

        lo  = self.lo
        hi  = self.hi
        k   = self.k

        steps_dict  = {}
        min_heap_1  = []
        min_heap_2  = []

        for num in range(lo, hi + 1):
            
            steps = self.get_integer_power(steps_dict, num)

            #Sort power numbers
            heapq.heappush(min_heap_1,[steps, num])

        count = 0

        while min_heap_1:

            num_arr = heapq.heappop(min_heap_1)
            
            heapq.heappush(min_heap_2, num_arr[1])

            #Sort in heap 2 when power numbers are the same
            while (len(min_heap_1) > 0) and (num_arr[0] == min_heap_1[-1][0]):
                num_arr = heapq.heappop(min_heap_1)
                heapq.heappush(min_heap_2, num_arr[1])

            #Output sorted numbers
            while len(min_heap_2):
                num_arr_2 = heapq.heappop(min_heap_2)
                
                count += 1

                #Get kth value
                if count == k:
                    return num_arr_2

        return -1