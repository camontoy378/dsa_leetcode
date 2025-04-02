import heapq

class TakeGifts():

    def __init__(self, gifts_array, k):
        self.gifts_array    = gifts_array
        self.k              = k

    def negate_array(self, array):

        return [-i for i in array]

    def solve(self):

        neg_gifts_array = self.negate_array(self.gifts_array)

        heapq.heapify(neg_gifts_array)

        for i in range(self.k):
            largest_pile = -heapq.heappop(neg_gifts_array)
            square_root_neg = -int(largest_pile ** (1/2))
            heapq.heappush(neg_gifts_array, square_root_neg)

        sum = 0
        for item in neg_gifts_array:
            sum += item

        return -sum