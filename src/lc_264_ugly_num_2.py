import heapq

class UglyNumTwo():

    def __init__(self, n):
        self.n  = n

    def solve(self):

        n = self.n
    
        #Setup
        prime_factors_limit = [2,3,5]
        heap_min = []
        count   = 0

        heapq.heappush(heap_min, 1)
        ugly_num = 1

        while count < n:
            
            ugly_num = heapq.heappop(heap_min)

            #Remove duplicates
            while (len(heap_min) > 0) and (ugly_num == heap_min[0]):
                heapq.heappop(heap_min)

            count += 1

            for num in prime_factors_limit:

                new_num = ugly_num * num

                heapq.heappush(heap_min, new_num)

        return ugly_num